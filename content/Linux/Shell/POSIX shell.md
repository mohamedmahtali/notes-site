---
title: POSIX shell
tags:
  - intermediate
---

# POSIX shell

---

## Définition

POSIX (Portable Operating System Interface) est un standard qui définit l'interface du [[Shell]]. Un script POSIX-compatible fonctionne sur n'importe quel shell conforme ([[Bash]], dash, sh, ksh). Utile pour les scripts qui doivent tourner dans des environnements minimaux (conteneurs Alpine, /bin/sh).

---

## Différences avec Bash

```bash
# ❌ Bash-only → ✅ POSIX

# Tableaux
arr=(a b c)           # ❌ Bash
# → utiliser des variables séparées ou des fichiers

# [[ ]] double brackets
[[ -f fichier ]]      # ❌ Bash
[ -f fichier ]        # ✅ POSIX

# Substitution de processus
diff <(cmd1) <(cmd2)  # ❌ Bash
# → utiliser des fichiers temporaires

# local dans les fonctions
local var=valeur      # ❌ non-POSIX (supporté par dash mais pas garanti)
```

---

## Script POSIX

```sh
#!/bin/sh
# Script POSIX-compatible

set -e

# Test
if [ -f "/etc/config" ]; then
    echo "Config trouvée"
fi

# Boucle
for i in 1 2 3 4 5; do
    echo "Iteration $i"
done

# Fonctions
greet() {
    echo "Bonjour $1"
}
greet "monde"
```

---

> [!tip]
> Pour les scripts [[Docker]] (Alpine), utiliser `#!/bin/sh` et éviter les constructions Bash-spécifiques. Pour les scripts CI/CD sur des serveurs standard, `#!/bin/bash` est acceptable.
