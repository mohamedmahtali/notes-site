---
title: htop
tags:
  - beginner
---

# htop

---

## Définition

`htop` est une version améliorée et interactive de `top`, avec une interface colorée, des barres de progression, et une navigation à la souris. Il n'est pas toujours installé par défaut mais est disponible dans tous les gestionnaires de paquets.

---

## Installation et utilisation

```bash
# Installer
apt-get install htop    # Debian/Ubuntu
yum install htop        # CentOS/RHEL
brew install htop       # macOS

# Lancer
htop
htop -u www-data        # filtrer par utilisateur
htop -p 1234            # surveiller un PID
```

---

## Raccourcis htop

```
F1/h     → aide
F2       → configurer
F3/      → rechercher
F4       → filtrer
F5       → arbre de processus
F6       → trier par colonne
F9       → kill (menu de signaux)
F10/q    → quitter
Espace   → taguer un processus
u        → filtrer par utilisateur
t        → basculer vue arbre
```

---

## Avantages sur top

- Barres CPU par core (vue d'ensemble immédiate)
- Défilement avec les flèches
- Kill avec sélection du signal
- Vue en arbre des processus (hiérarchie parent/enfant)
- Refresh plus rapide par défaut (1 sec)
