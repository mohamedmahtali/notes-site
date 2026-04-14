---
title: stdout
tags:
  - beginner
---

# stdout

## Parent
- [[Redirections]]

---

## Définition

`stdout` (standard output, fd 1) est le flux de sortie normale d'une commande. Par défaut, il s'affiche dans le terminal. Il peut être redirigé vers un fichier ou vers l'entrée d'une autre commande.

---

## Utilisation

```bash
# Rediriger vers un fichier (écrase)
echo "Hello" > fichier.txt
ls -la > listing.txt

# Append (ajouter sans écraser)
echo "nouvelle ligne" >> fichier.txt
./deploy.sh >> deploy.log

# Piper vers une autre commande
ls | sort | head -5

# tee : afficher ET sauvegarder
./script.sh | tee output.log

# /dev/null : jeter la sortie
apt-get install -y curl > /dev/null
```
