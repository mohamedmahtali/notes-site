---
title: restart
tags:
  - beginner
---

# restart

---

## Définition

`docker restart` arrête puis redémarre un conteneur. Équivalent à `docker stop` + `docker start`. Utile pour appliquer des changements de configuration ou relancer un conteneur bloqué.

---

## Commandes

```bash
# Redémarrer un conteneur
docker restart mon-app

# Avec timeout personnalisé
docker restart --time 5 mon-app

# Redémarrer plusieurs conteneurs
docker restart app1 app2
```

---

## Restart policy (automatique)

```bash
# Configurer un redémarrage automatique
docker run -d --restart=always mon-app
docker run -d --restart=on-failure:3 mon-app  # max 3 tentatives
docker run -d --restart=unless-stopped mon-app
```

| Policy | Comportement |
|---|---|
| `no` | Jamais redémarrer (défaut) |
| `always` | Toujours redémarrer |
| `on-failure` | Seulement si code de sortie ≠ 0 |
| `unless-stopped` | Toujours sauf arrêt manuel |
