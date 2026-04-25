---
title: Conditions
tags:
  - beginner
---

# Conditions

---

## Définition

Les conditions [[Bash]] permettent d'exécuter du code selon des critères : existence de fichiers, comparaisons de chaînes, comparaisons numériques, codes de sortie.

---

## Syntaxe

```bash
# if/elif/else
if [[ condition ]]; then
    commandes
elif [[ autre_condition ]]; then
    commandes
else
    commandes
fi

# Test sur une seule ligne
[[ -f fichier ]] && echo "existe" || echo "manquant"
```

---

## Tests de fichiers

```bash
[[ -f fichier ]]   # existe et est un fichier
[[ -d dossier ]]   # existe et est un dossier
[[ -e chemin ]]    # existe (fichier ou dossier)
[[ -r fichier ]]   # lisible
[[ -w fichier ]]   # inscriptible
[[ -x fichier ]]   # exécutable
[[ -s fichier ]]   # existe et non vide
```

---

## Comparaisons

```bash
# Chaînes
[[ "$A" == "$B" ]]    # égal
[[ "$A" != "$B" ]]    # différent
[[ -z "$A" ]]         # vide
[[ -n "$A" ]]         # non vide
[[ "$A" =~ ^[0-9]+$ ]] # regex match

# Nombres (utiliser (( )) ou -eq/-ne/-lt/-gt)
[[ $N -eq 5 ]]   # égal
[[ $N -ne 5 ]]   # différent
[[ $N -lt 10 ]]  # inférieur
[[ $N -gt 0 ]]   # supérieur
(( N > 0 && N < 10 ))  # arithmétique directe
```

---

## Exemple pratique

```bash
#!/bin/bash
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <fichier>" >&2
    exit 1
fi

if [[ ! -f "$1" ]]; then
    echo "Fichier introuvable: $1" >&2
    exit 2
fi

echo "Traitement de $1"
```
