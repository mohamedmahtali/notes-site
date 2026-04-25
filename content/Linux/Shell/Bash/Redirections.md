---
title: Redirections
tags:
  - beginner
---

# Redirections

---

## Définition

Les redirections [[Bash]] dirigent les [[Flux]] d'entrée/sortie des commandes vers des fichiers ou d'autres commandes. Trois flux standard : [[stdin]] (0), [[stdout]] (1), [[stderr]] (2).

---

## Référence rapide

```bash
commande > fichier       # stdout → fichier (écrase)
commande >> fichier      # stdout → fichier (append)
commande 2> erreurs      # stderr → fichier
commande 2>> erreurs     # stderr → fichier (append)
commande &> tout         # stdout + stderr → fichier
commande > /dev/null     # supprimer stdout
commande 2>/dev/null     # supprimer stderr
commande &>/dev/null     # supprimer tout

commande < fichier       # stdin depuis fichier
commande <<EOF           # heredoc
texte multiligne
EOF

commande 2>&1            # stderr vers stdout (pour piper)
```

---

## Exemples pratiques

```bash
# Logger stdout et stderr séparément
./script.sh > output.log 2> error.log

# Logger tout ensemble
./script.sh &> app.log

# Piper stderr
./script.sh 2>&1 | grep "ERROR"

# Heredoc pour passer du texte multilignes
cat << 'EOF' > config.yaml
database:
  host: localhost
  port: 5432
EOF

# Supprimer les messages inutiles
docker build . 2>/dev/null
```
