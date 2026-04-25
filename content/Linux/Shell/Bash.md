---
title: Bash
tags:
  - beginner
---

# Bash

---

## Définition

Bash (Bourne Again [[Shell]]) est le shell par défaut sur la majorité des distributions [[Linux]]. C'est le langage de scripting incontournable pour l'automatisation système, les [[Pipeline]] CI/CD, et l'administration Linux.

---

## Script de base

```bash
#!/usr/bin/env bash
set -euo pipefail   # options de sécurité recommandées

# set -e : arrêt sur erreur
# set -u : erreur si variable non définie
# set -o pipefail : erreur si pipe échoue

echo "Démarrage du script"

# Variables
APP_NAME="mon-app"
VERSION="${1:-latest}"   # argument $1 ou "latest" par défaut

# Conditions
if [[ -f "/etc/app.conf" ]]; then
    echo "Config trouvée"
else
    echo "Config manquante" >&2
    exit 1
fi

# Boucle
for service in nginx postgres redis; do
    systemctl status "$service" || echo "$service: DOWN"
done

echo "Script terminé avec succès"
```

---

## Raccourcis essentiels

```bash
Ctrl+C   # interrompre
Ctrl+Z   # mettre en pause (bg/fg pour reprendre)
Ctrl+R   # recherche dans l'historique
!!       # répéter la dernière commande
!$       # dernier argument de la commande précédente
```
