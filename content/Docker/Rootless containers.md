---
title: Rootless containers
tags:
  - advanced
---

# Rootless containers

---

## Définition

Les conteneurs rootless permettent d'exécuter le daemon [[Docker]] et les conteneurs sans privilèges root sur l'hôte. Le daemon s'exécute sous un utilisateur normal, réduisant drastiquement la surface d'attaque en cas d'évasion de conteneur.

---

## Pourquoi c'est important

> [!tip] Sécurité renforcée
> En mode rootless, même si un attaquant s'échappe du conteneur, il n'obtient que les droits de l'utilisateur qui exécute le daemon — pas root sur l'hôte.

---

## Installation (rootless Docker)

```bash
# Installer le script rootless
dockerd-rootless-setuptool.sh install

# Configurer l'environnement
export DOCKER_HOST=unix:///run/user/1000/docker.sock

# Démarrer le daemon rootless
systemctl --user start docker

# Vérifier
docker info | grep "rootless"
```

---

## Alternatives

```bash
# Podman (rootless par défaut)
podman run -d nginx
podman ps

# Podman est compatible avec les commandes Docker
alias docker=podman
```

---

## Limitations du mode rootless

| Limitation | Détail |
|---|---|
| Réseau | Certains drivers réseau non disponibles |
| Performance | Légèrement inférieure (user [[Namespaces]]) |
| [[Ports]] < 1024 | Non exposables sans configuration supplémentaire |
| [[Overlay]] FS | Peut nécessiter une configuration [[Kernel]] |

---

> [!note]
> Podman est souvent préféré pour les environnements rootless car il est conçu pour ça dès le départ. Docker rootless est une option mais nécessite plus de configuration.
