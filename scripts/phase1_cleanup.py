#!/usr/bin/env python3
"""
Phase 1 - Nettoyage du vault Obsidian/Quartz
- Supprime les sections ## Parent, ## Enfants, ## Concepts liés (redondantes avec backlinks)
- Supprime les sections ## Liens vides sur les notes feuilles
- Homogénéise les tags en format liste YAML
- Nettoie les lignes vides excessives
"""

import re
import os
import sys
from pathlib import Path

SECTIONS_TO_REMOVE = ['Parent', 'Enfants', 'Concepts liés']


def remove_sections(content: str, sections: list[str]) -> str:
    """Supprime les sections ## et leur contenu (listes de liens) jusqu'au prochain ## ou ---"""
    lines = content.split('\n')
    result = []
    in_section = False

    for line in lines:
        heading = line[3:].rstrip() if line.startswith('## ') else None

        if heading in sections:
            in_section = True
            continue

        if in_section:
            # La section se termine au prochain heading ou séparateur
            if line.startswith('#') or line == '---':
                in_section = False
                result.append(line)
            # Sinon on skip (contenu de la section à supprimer)
            continue

        result.append(line)

    return '\n'.join(result)


def remove_empty_liens(content: str) -> str:
    """Supprime ## Liens seulement si la section n'a aucun item de liste"""
    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        if lines[i] == '## Liens':
            # Chercher si la section a du contenu (items de liste)
            j = i + 1
            has_content = False
            while j < len(lines):
                l = lines[j]
                if l.startswith('## ') or l.startswith('# ') or l == '---':
                    break
                if l.startswith('- ') or l.startswith('* '):
                    has_content = True
                    break
                j += 1

            if has_content:
                result.append(lines[i])  # Garder la section
        else:
            result.append(lines[i])
        i += 1

    return '\n'.join(result)


def normalize_tags(content: str) -> str:
    """Convertit tags: [a, b] → format liste YAML, uniquement dans le frontmatter"""
    if not content.startswith('---'):
        return content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return content

    frontmatter = parts[1]
    body = parts[2]

    def to_list(match):
        tags = [t.strip() for t in match.group(1).split(',')]
        return 'tags:\n' + '\n'.join(f'  - {t}' for t in tags)

    frontmatter = re.sub(r'^tags: \[([^\]]+)\]$', to_list, frontmatter, flags=re.MULTILINE)

    return f'---{frontmatter}---{body}'


def cleanup_blank_lines(content: str) -> str:
    """Remplace 3+ lignes vides consécutives par 2"""
    return re.sub(r'\n{3,}', '\n\n', content)


def process_file(filepath: Path, dry_run: bool = False) -> tuple[bool, list[str]]:
    """Traite un fichier. Retourne (modifié, liste_des_changements)"""
    text = filepath.read_text(encoding='utf-8')
    original = text
    changes = []

    new_text = remove_sections(text, SECTIONS_TO_REMOVE)
    if new_text != text:
        removed = [s for s in SECTIONS_TO_REMOVE if f'## {s}' in text]
        changes.append(f"sections supprimées: {removed}")
        text = new_text

    new_text = remove_empty_liens(text)
    if new_text != text:
        changes.append("## Liens vide supprimé")
        text = new_text

    new_text = normalize_tags(text)
    if new_text != text:
        changes.append("tags normalisés")
        text = new_text

    new_text = cleanup_blank_lines(text)
    if new_text != text:
        changes.append("lignes vides nettoyées")
        text = new_text

    if text != original:
        if not dry_run:
            filepath.write_text(text, encoding='utf-8')
        return True, changes

    return False, []


def main():
    dry_run = '--dry-run' in sys.argv
    sample = '--sample' in sys.argv

    content_dir = Path('content')
    all_files = sorted(content_dir.rglob('*.md'))

    if sample:
        # Tester sur quelques fichiers représentatifs
        sample_files = [
            content_dir / 'CI-CD/Pipeline.md',
            content_dir / 'Kubernetes/Cluster/Control plane.md',
            content_dir / 'Security/Zero trust.md',
            content_dir / 'Docker/Dockerfile/Multi stage builds.md',
            content_dir / 'Networking.md',
        ]
        all_files = [f for f in sample_files if f.exists()]

    mode = "DRY-RUN" if dry_run else "LIVE"
    scope = "SAMPLE" if sample else f"ALL ({len(all_files)} fichiers)"
    print(f"\n{'='*60}")
    print(f"Phase 1 Cleanup — {mode} — {scope}")
    print(f"{'='*60}\n")

    modified = 0
    for filepath in all_files:
        changed, changes = process_file(filepath, dry_run=dry_run)
        if changed:
            modified += 1
            rel = filepath.relative_to(content_dir)
            print(f"  ✓ {rel}")
            for c in changes:
                print(f"      → {c}")

    print(f"\n{'='*60}")
    action = "seraient modifiés" if dry_run else "modifiés"
    print(f"Résultat : {modified}/{len(all_files)} fichiers {action}")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
