---
title: Variables
tags:
  - beginner
---

# Variables

## Parent
- [[Bash]]

---

## Définition

Les variables Bash stockent des valeurs (chaînes, nombres) pour les réutiliser dans un script. Elles sont non-typées par défaut — toute valeur est traitée comme une chaîne sauf si spécifié autrement.

---

## Syntaxe

```bash
# Assignation (pas d'espaces autour de =)
NOM="Mohamed"
AGE=30
FICHIER="/var/log/app.log"

# Lecture
echo "$NOM"
echo "${NOM}"          # syntaxe avec accolades (recommandée)
echo "${NOM:-inconnu}" # valeur par défaut si vide

# Variables d'environnement
export DB_HOST="localhost"   # disponible pour les processus enfants
printenv DB_HOST

# Variables spéciales
echo "$0"   # nom du script
echo "$1"   # premier argument
echo "$@"   # tous les arguments
echo "$#"   # nombre d'arguments
echo "$?"   # code de sortie de la dernière commande
echo "$$"   # PID du script actuel
```

---

## Manipulation de chaînes

```bash
CHAINE="bonjour monde"

echo "${#CHAINE}"              # longueur : 13
echo "${CHAINE^}"              # Bonjour monde (majuscule 1er)
echo "${CHAINE^^}"             # BONJOUR MONDE
echo "${CHAINE/monde/world}"   # bonjour world (remplacer)
echo "${CHAINE:0:7}"           # bonjour (sous-chaîne)
echo "${CHAINE##* }"           # monde (après dernier espace)

FICHIER="/opt/app/config.json"
echo "${FICHIER##*/}"          # config.json (basename)
echo "${FICHIER%/*}"           # /opt/app (dirname)
echo "${FICHIER%.json}"        # /opt/app/config (sans extension)
```
