---
title: Signals
tags:
  - intermediate
---
# Signals

## Parent
- [[Processes]]

## Enfants
- [[SIGTERM]]
- [[SIGKILL]]
- [[SIGHUP]]

---

## Définition

Les signaux sont des notifications asynchrones envoyées à un processus pour lui communiquer un événement (arrêt demandé, rechargement de config, erreur fatale). Chaque signal a un numéro et un comportement par défaut.

---

## Signaux essentiels

| Signal | Numéro | Comportement par défaut | Capturable |
|--------|--------|------------------------|------------|
| SIGTERM | 15 | Arrêt propre | ✅ Oui |
| SIGKILL | 9 | Arrêt immédiat | ❌ Non |
| SIGHUP | 1 | Rechargement de config | ✅ Oui |
| SIGINT | 2 | Interruption (Ctrl+C) | ✅ Oui |
| SIGSTOP | 19 | Pause du processus | ❌ Non |
| SIGCONT | 18 | Reprendre après pause | ✅ Oui |

---

## Envoyer des signaux

```bash
# Par PID
kill -15 1234        # SIGTERM (graceful)
kill -9 1234         # SIGKILL (force)
kill -1 1234         # SIGHUP (reload)

# Par nom de processus
pkill nginx           # SIGTERM à tous les processus nginx
pkill -HUP nginx      # SIGHUP à nginx (reload config)
killall node          # SIGTERM à tous les processus node

# Depuis le terminal
Ctrl+C               # SIGINT
Ctrl+Z               # SIGTSTP (suspend)
```

---

> [!tip]
> Toujours essayer SIGTERM avant SIGKILL. SIGTERM laisse le processus se terminer proprement (flush des buffers, fermeture des connexions). SIGKILL ne peut pas être ignoré mais laisse les ressources dans un état sale.
