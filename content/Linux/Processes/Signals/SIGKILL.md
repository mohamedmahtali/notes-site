---
title: SIGKILL
tags:
  - intermediate
---

# SIGKILL

## Parent
- [[Signals]]

---

## Définition

SIGKILL (signal 9) est le signal d'arrêt immédiat et forcé. Il **ne peut pas être intercepté, ignoré, ou bloqué** par le processus. Le kernel tue le processus instantanément sans lui laisser faire de nettoyage.

---

## Utilisation

```bash
# Tuer immédiatement
kill -9 PID
kill -KILL PID

# Tuer tous les processus d'un nom
killall -9 processus-bloqué

# Combinaison : essayer propre d'abord, forcer si nécessaire
kill PID
sleep 5
kill -9 PID 2>/dev/null || true
```

---

## SIGTERM vs SIGKILL

| | SIGTERM | SIGKILL |
|---|---|---|
| Peut être intercepté | ✅ Oui | ❌ Non |
| Nettoyage possible | ✅ Oui | ❌ Non |
| Risque de corruption | Faible | ⚠️ Possible |
| À utiliser | En premier | Si SIGTERM échoue |

---

## Risques de SIGKILL

> [!warning]
> SIGKILL peut laisser des ressources en état inconsistant :
> - Fichiers partiellement écrits
> - Connexions DB non fermées proprement
> - Fichiers de lock non supprimés
> - Transactions non commitées

Toujours essayer SIGTERM en premier et donner un délai (5-30s) avant SIGKILL.
