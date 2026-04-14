---
title: TTL
tags:
  - beginner
---

# TTL

## Parent
- [[DNS]]

---

## Définition

TTL (Time To Live) est la durée en secondes pendant laquelle un enregistrement DNS peut être mis en cache par les résolveurs. Après expiration, le résolveur doit requêter à nouveau le serveur autoritatif.

---

## Impact du TTL

| TTL | Durée | Impact |
|---|---|---|
| 60 | 1 min | Changements quasi-instantanés, charges serveur élevées |
| 300 | 5 min | Bon compromis pour les migrations |
| 3600 | 1h | Standard pour la plupart des records |
| 86400 | 24h | MX, NS stables — changements lents |

---

## Stratégie de migration

```bash
# Avant un changement d'IP (migration de serveur)
# 1. Réduire le TTL 24h à l'avance
old TTL 86400 → nouveau TTL 300

# 2. Effectuer le changement d'IP
A record : old-ip → new-ip

# 3. Attendre la propagation (max TTL précédent = 24h)
# 4. Remonter le TTL une fois stable
TTL 300 → TTL 3600
```

---

## Vérifier le TTL

```bash
dig google.com A
# google.com. 299 IN A 142.250.185.78
#             ^^^ TTL restant en cache
```
