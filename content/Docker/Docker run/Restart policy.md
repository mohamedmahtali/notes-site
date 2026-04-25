---
title: Restart policy
tags:
  - intermediate
---

# Restart policy

---

## Définition

La [[restart]] policy définit le comportement de [[Docker]] quand un conteneur s'arrête (crash, OOM, reboot du daemon). Elle est configurée avec `--restart` au lancement.

---

## Politiques disponibles

| Policy | Comportement |
|---|---|
| `no` | Ne jamais redémarrer (défaut) |
| `always` | Toujours redémarrer, même après `docker stop` + `docker daemon restart` |
| `unless-stopped` | Toujours redémarrer, sauf arrêt manuel explicite |
| `on-failure[:N]` | Redémarrer seulement si code de sortie ≠ 0, max N fois |

---

## Commandes

```bash
# Toujours redémarrer (services critiques)
docker run -d --restart=always mon-app

# Redémarrer sauf arrêt manuel (recommandé)
docker run -d --restart=unless-stopped mon-app

# Réessayer max 3 fois en cas de crash
docker run -d --restart=on-failure:3 mon-app

# Voir la restart policy d'un conteneur
docker inspect mon-app | grep RestartPolicy
```

---

## En Docker Compose

```yaml
services:
  api:
    restart: unless-stopped
  worker:
    restart: on-failure
```

---

> [!tip]
> Pour les [[Services]] de production, `unless-stopped` est le meilleur compromis : redémarre automatiquement après un crash ou un reboot, mais s'arrête proprement quand tu fais `docker stop`.
