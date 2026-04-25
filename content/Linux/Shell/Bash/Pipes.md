---
title: Pipes
tags:
  - beginner
---

# Pipes

---

## Définition

Un pipe (`|`) connecte la sortie standard ([[stdout]]) d'une commande à l'entrée standard ([[stdin]]) de la suivante. C'est la philosophie Unix : des outils simples qui font une seule chose bien, chaînés pour accomplir des tâches complexes.

---

## Utilisation

```bash
# Compter les lignes d'erreur
grep "ERROR" /var/log/app.log | wc -l

# Top 5 des IPs dans les logs
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -5

# Chercher un processus
ps aux | grep nginx | grep -v grep

# Filtrer et reformater
cat /etc/passwd | cut -d: -f1 | sort

# Pipeline plus complexe
docker ps --format "{{.Names}}" |   xargs -I {} docker inspect {} |   jq '.[].State.Status'
```

---

## xargs – transformer un pipe en arguments

```bash
# Supprimer tous les fichiers .tmp
find . -name "*.tmp" | xargs rm

# Avec un placeholder
find . -name "*.log" | xargs -I {} mv {} /archive/

# Paralléliser
cat urls.txt | xargs -P 4 -I {} curl -o /dev/null -s {}
```

---

## tee – lire ET écrire

```bash
# Afficher ET sauvegarder
./deploy.sh | tee deploy.log

# Afficher ET passer au pipe suivant
cat data.csv | tee data-backup.csv | grep "France"
```
