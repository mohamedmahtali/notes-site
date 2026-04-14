---
title: Foreground and background
tags:
  - beginner
---

# Foreground and background

## Parent
- [[Processes]]

---

## Définition

Un processus en **foreground** (avant-plan) est attaché au terminal et bloque la saisie. Un processus en **background** (arrière-plan) tourne de manière indépendante et laisse le terminal libre.

---

## Commandes

```bash
# Lancer en arrière-plan avec &
./script.sh &
# [1] 12345   ← job number + PID

# Voir les jobs en arrière-plan
jobs
# [1]  Running    ./script.sh &
# [2]+ Stopped    vim fichier.txt

# Mettre un processus foreground en pause
Ctrl+Z    # → SIGSTOP → état "Stopped"

# Reprendre en arrière-plan
bg %1     # bg %job_number

# Reprendre en avant-plan
fg %1

# Attendre la fin d'un job background
wait %1
wait      # attendre tous les jobs
```

---

## nohup – survivre à la déconnexion

```bash
# Sans nohup : le processus reçoit SIGHUP à la déconnexion SSH
./long-script.sh &

# Avec nohup : ignore SIGHUP, sortie dans nohup.out
nohup ./long-script.sh &

# Avec redirection explicite
nohup ./long-script.sh > output.log 2>&1 &
```

---

## disown

```bash
# Détacher un job du shell (ne reçoit plus les signaux du terminal)
./script.sh &
disown %1    # ou disown PID
```
