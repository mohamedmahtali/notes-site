---
title: stdin
tags:
  - beginner
---

# stdin

## Parent
- [[Redirections]]

---

## Définition

`stdin` (standard input, fd 0) est le flux d'entrée d'une commande. Par défaut, il vient du clavier. Il peut être redirigé depuis un fichier ou depuis la sortie d'une commande précédente.

---

## Utilisation

```bash
# Depuis un fichier
sort < liste.txt
wc -l < access.log

# Depuis un heredoc (texte inline)
cat << 'EOF'
ligne 1
ligne 2
EOF

# Avec psql, mysql
psql -U user dbname < migration.sql
mysql -u root -p mydb < dump.sql

# read lit depuis stdin
echo "Entrez votre nom :"
read NOM
echo "Bonjour $NOM"

# Lire depuis un pipe
echo "bonjour" | tr 'a-z' 'A-Z'
```
