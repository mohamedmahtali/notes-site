---
title: Git ignore
tags:
  - intermediate
---
# Git ignore

## Parent
- [[Git]]

## Enfants
- [[Global ignore]]
- [[Project ignore]]

## Concepts liés
- [[Global ignore]]
- [[Project ignore]]
- [[Artifacts]]

---

## Définition

`.gitignore` est un fichier de configuration qui indique à Git quels fichiers et dossiers **ne pas tracker**. Les fichiers ignorés n'apparaissent pas dans `git status` et ne sont jamais committés accidentellement.

---

## Pourquoi c'est important

> [!warning] Ne jamais committer
> - `node_modules/`, `.venv/` → dépendances reconstituables
> - `.env`, `*.key` → secrets et credentials
> - `dist/`, `build/` → artefacts générés
> - `.DS_Store`, `.idea/` → fichiers d'OS/IDE

---

## Niveaux de gitignore

| Niveau | Fichier | Scope | Versionné |
|---|---|---|---|
| [[Project ignore\|Projet]] | `.gitignore` | Ce dépôt uniquement | ✅ Oui |
| [[Global ignore\|Global]] | `~/.gitignore_global` | Tous les dépôts | ❌ Non |
| Dépôt | `.git/info/exclude` | Ce dépôt, non partagé | ❌ Non |

---

## Syntaxe rapide

```gitignore
node_modules/    # dossier entier
*.log            # tous les .log
.env             # fichier exact
!.env.example    # exception (ne pas ignorer)
/dist/           # seulement à la racine
**/temp/         # temp/ dans n'importe quel sous-dossier
```

---

## Arrêter de tracker un fichier déjà commité

```bash
echo ".env" >> .gitignore
git rm --cached .env
git commit -m "chore: untrack .env file"
```

---

> [!tip]
> [gitignore.io](https://www.toptal.com/developers/gitignore) génère automatiquement un `.gitignore` adapté à ton stack (Node, Python, Java, etc.).
