---
title: Shell
tags:
  - beginner
---

# Shell

---

## Définition

Un shell est l'interface de ligne de commande qui interprète les commandes saisies par l'utilisateur et les exécute via le [[Kernel]]. C'est l'outil central du travail en [[Linux]] — scripts d'automatisation, administration système, et [[Pipeline]] CI/CD en dépendent.

---

## Shells courants

| Shell | Fichier config | Particularités |
|---|---|---|
| [[Bash]] | `~/.bashrc`, `~/.bash_profile` | Standard Linux, plus répandu |
| [[Zsh]] | `~/.zshrc` | Autocomplétion avancée, oh-my-zsh |
| [[POSIX shell\|sh]] | Varies | Compatible POSIX, scripts portables |
| `fish` | `~/.config/fish/` | Syntaxe user-friendly |
| `dash` | — | Ultra-léger, utilisé par Ubuntu pour /bin/sh |

---

## Concepts fondamentaux

```bash
# Variables
NOM="Mohamed"
echo "Bonjour $NOM"

# Redirection
commande > fichier.txt    # stdout vers fichier
commande >> fichier.txt   # append
commande 2> erreurs.txt   # stderr
commande &> tout.txt      # stdout + stderr

# Pipes
cat access.log | grep "404" | wc -l

# Substitution de commande
DATE=$(date +%Y-%m-%d)
echo "Aujourd'hui : $DATE"

# Codes de sortie
ls /existe && echo "OK"   # && : seulement si succès
ls /noexist || echo "KO"  # || : seulement si échec
```

---

> [!tip]
> Shebang line : la première ligne d'un script indique quel interpréteur utiliser :
> ```bash
> #!/bin/bash     # Bash explicite
> #!/usr/bin/[[ENV]] bash   # Bash via PATH (plus portable)
> #!/bin/sh       # POSIX sh
> ```
