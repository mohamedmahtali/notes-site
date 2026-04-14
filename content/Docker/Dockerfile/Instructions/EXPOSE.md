---
title: EXPOSE
tags:
  - beginner
---

# EXPOSE

## Parent
- [[Instructions]]

---

## Définition

`EXPOSE` documente le(s) port(s) sur lesquels le conteneur écoute. C'est une **documentation**, pas une ouverture réelle de port. Le port n'est accessible depuis l'hôte que si mappé avec `-p` dans `docker run`.

---

## Syntaxe

```dockerfile
EXPOSE 3000
EXPOSE 8080/tcp
EXPOSE 53/udp
EXPOSE 3000 8080   # plusieurs ports
```

---

## EXPOSE vs -p

```bash
# EXPOSE dans le Dockerfile → documentation seulement
EXPOSE 3000

# -p au runtime → ouvre vraiment le port sur l'hôte
docker run -p 8080:3000 mon-app
#              hôte:conteneur
```

| Paramètre | Effet |
|---|---|
| `EXPOSE` seul | Visible avec `docker inspect`, utilisé par `--publish-all` |
| `-p 8080:3000` | Mappe le port 3000 du conteneur sur 8080 de l'hôte |
| `-P` | Mappe automatiquement tous les ports `EXPOSE` |

---

> [!note]
> `EXPOSE` est utile pour la documentation et pour les outils qui lisent les métadonnées de l'image (Docker Compose, Kubernetes). C'est une bonne pratique de toujours le mettre même si ce n'est pas obligatoire.
