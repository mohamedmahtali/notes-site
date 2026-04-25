#!/usr/bin/env python3
"""
Phase 2 - Enrichissement des liens contextuels
Pour chaque note, détecte les premières occurrences de termes connus
et ajoute des [[wikilinks]] dans le corps du texte.

Règles :
- Ignore : frontmatter, blocs de code, headings, liens existants
- Lie chaque terme au maximum une fois par document (première occurrence)
- Termes longs traités en premier (évite les sous-matchs)
- (?<!\\[) évite de matcher à l'intérieur de [[liens]] nouvellement créés
"""

import re
import sys
from pathlib import Path

VOCAB_EXCLUDE_STEMS = {'index', 'about', 'roadmap', 'archi'}
VOCAB_EXCLUDE_PATTERNS = ['cheat sheet', 'lab —', 'lab ']
MIN_TERM_LEN = 3

# Termes trop génériques pour être liés automatiquement
VOCAB_BLACKLIST = {
    # Verbes ou mots courants en français/anglais
    'compile', 'production', 'applications', 'application', 'stages',
    'agents', 'agent', 'alerts', 'alert', 'apply', 'annotations',
    # Termes trop courts ou ambigus
    'add', 'run', 'steps', 'step', 'jobs', 'job', 'tags', 'labels',
    'logs', 'log', 'links', 'link', 'images', 'image',
    # Concepts trop larges pour être liés en contexte général
    'approvals', 'environments', 'targets', 'rules', 'allow rules',
    'availability target',
}


def build_vocabulary(content_dir: Path) -> dict[str, str]:
    """Construit {terme_lower: nom_canonique} depuis les noms de fichiers"""
    vocab = {}
    for md_file in content_dir.rglob('*.md'):
        stem = md_file.stem
        stem_lower = stem.lower()
        if stem_lower in VOCAB_EXCLUDE_STEMS:
            continue
        if stem_lower in VOCAB_BLACKLIST:
            continue
        if any(p in stem_lower for p in VOCAB_EXCLUDE_PATTERNS):
            continue
        if len(stem) < MIN_TERM_LEN:
            continue
        vocab[stem_lower] = stem
    return vocab


def build_patterns(vocab: dict[str, str]) -> list[tuple]:
    """Compile les regex, triées par longueur décroissante (termes longs en premier)"""
    patterns = []
    for term_lower, canonical in sorted(vocab.items(), key=lambda x: len(x[0]), reverse=True):
        escaped = re.escape(term_lower)
        # Pour les termes simples (un mot sans espace ni tiret), on accepte le pluriel en 's'
        if ' ' in term_lower or '-' in term_lower:
            pat = re.compile(rf'(?<!\[)\b{escaped}\b', re.IGNORECASE)
        else:
            pat = re.compile(rf'(?<!\[)\b{escaped}s?\b', re.IGNORECASE)
        patterns.append((term_lower, canonical, pat))
    return patterns


def split_frontmatter(content: str) -> tuple[str, str]:
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return f'---{parts[1]}---', parts[2]
    return '', content


def collect_existing_links(body: str) -> set[str]:
    """Retourne l'ensemble des termes déjà liés (en minuscules)"""
    linked = set()
    for m in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]])?\]\]', body):
        linked.add(m.group(1).strip().lower())
    return linked


def enrich_line(line: str, patterns: list[tuple], linked: set) -> str:
    """Traite une ligne texte : protège code inline et liens, enrichit le reste"""
    protect = re.compile(r'(`[^`\n]+`|\[\[[^\]]+\]\])')
    parts = protect.split(line)

    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            result.append(part)  # Segment protégé, on ne touche pas
            continue

        # Segment texte libre : appliquer les patterns dans l'ordre
        for term_lower, canonical, pattern in patterns:
            if term_lower in linked:
                continue

            def make_replacer(c: str, t: str):
                def replacer(m):
                    linked.add(t)
                    return f'[[{c}]]'
                return replacer

            new_part = pattern.sub(make_replacer(canonical, term_lower), part, count=1)
            if new_part != part:
                part = new_part

        result.append(part)

    return ''.join(result)


def enrich_body(body: str, patterns: list[tuple], current_stem: str) -> str:
    lines = body.split('\n')
    result = []
    in_code_block = False

    # Pré-initialiser avec les termes déjà liés + le terme de la note elle-même
    linked = collect_existing_links(body)
    linked.add(current_stem.lower())

    for line in lines:
        stripped = line.strip()

        # Toggle bloc de code fenced
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # Ignorer : headings, lignes vides, séparateurs
        if stripped.startswith('#') or not stripped or stripped == '---':
            result.append(line)
            continue

        result.append(enrich_line(line, patterns, linked))

    return '\n'.join(result)


def process_file(filepath: Path, patterns: list[tuple], dry_run: bool = False) -> tuple[bool, int]:
    content = filepath.read_text(encoding='utf-8')
    frontmatter, body = split_frontmatter(content)

    new_body = enrich_body(body, patterns, filepath.stem)

    if new_body == body:
        return False, 0

    added = len(re.findall(r'\[\[', new_body)) - len(re.findall(r'\[\[', body))

    if not dry_run:
        filepath.write_text(frontmatter + new_body, encoding='utf-8')

    return True, added


def show_diff_sample(filepath: Path, patterns: list[tuple], n_lines: int = 8):
    """Affiche quelques lignes avant/après pour vérification visuelle"""
    content = filepath.read_text(encoding='utf-8')
    frontmatter, body = split_frontmatter(content)
    new_body = enrich_body(body, patterns, filepath.stem)

    old_lines = body.split('\n')
    new_lines = new_body.split('\n')

    shown = 0
    for old, new in zip(old_lines, new_lines):
        if old != new and shown < n_lines:
            print(f"  - {old.strip()}")
            print(f"  + {new.strip()}")
            print()
            shown += 1


def main():
    dry_run = '--dry-run' in sys.argv
    sample = '--sample' in sys.argv
    show_diff = '--diff' in sys.argv

    content_dir = Path('content')
    vocab = build_vocabulary(content_dir)
    patterns = build_patterns(vocab)

    print(f"\nVocabulaire : {len(vocab)} termes")

    all_files = sorted(content_dir.rglob('*.md'))

    if sample:
        sample_files = [
            content_dir / 'CI-CD/Pipeline.md',
            content_dir / 'Kubernetes/Cluster/Control plane.md',
            content_dir / 'Security/Zero trust.md',
            content_dir / 'GitOps/ArgoCD.md',
            content_dir / 'Infrastructure as Code/Terraform.md',
        ]
        all_files = [f for f in sample_files if f.exists()]

    mode = 'DRY-RUN' if dry_run else 'LIVE'
    scope = f'SAMPLE ({len(all_files)} fichiers)' if sample else f'ALL ({len(all_files)} fichiers)'
    print(f'Mode : {mode} — {scope}')
    print('=' * 60)

    total_modified = 0
    total_added = 0

    for filepath in all_files:
        if show_diff and sample:
            rel = filepath.relative_to(content_dir)
            print(f'\n>>> {rel}')
            show_diff_sample(filepath, patterns)

        modified, added = process_file(filepath, patterns, dry_run=dry_run)
        if modified:
            total_modified += 1
            total_added += added
            rel = filepath.relative_to(content_dir)
            if not show_diff:
                print(f'  +{added:3d} liens  {rel}')

    print('=' * 60)
    action = 'seraient modifiés' if dry_run else 'modifiés'
    print(f'Résultat : {total_modified}/{len(all_files)} fichiers {action}, {total_added} liens ajoutés')

    if not dry_run and total_added > 0:
        all_md = list(content_dir.rglob('*.md'))
        new_total = sum(
            len(re.findall(r'\[\[', f.read_text(encoding='utf-8'))) for f in all_md
        )
        print(f'Densité  : {new_total / len(all_md):.1f} liens/fichier (avant : 4.3)')


if __name__ == '__main__':
    main()
