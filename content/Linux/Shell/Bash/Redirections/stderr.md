---
title: stderr
tags:
  - beginner
---

# stderr

---

## Définition

`stderr` (standard error, fd 2) est le [[Flux]] de sortie d'erreur. Séparé de [[stdout]], il permet de distinguer les messages d'erreur de la sortie normale. Les messages d'erreur d'un script bien écrit vont sur stderr.

---

## Utilisation

```bash
# Écrire sur stderr dans un script
echo "Erreur : fichier manquant" >&2

# Rediriger stderr vers un fichier
ls /noexiste 2> erreurs.txt

# Rediriger stderr vers stdout (pour piper)
./script.sh 2>&1 | grep "ERROR"

# Séparer stdout et stderr
./script.sh > output.log 2> errors.log

# Ignorer stderr
find / -name "*.conf" 2>/dev/null

# Tout capturer
./deploy.sh &> full.log
```

---

> [!tip] Convention de scripting
> Les messages d'usage et d'erreur doivent toujours aller sur stderr :
> ```[[Bash]]
> echo "Usage: $0 <fichier>" >&2
> exit 1
> ```
> Ça permet de piper la sortie utile sans polluer avec les erreurs.
