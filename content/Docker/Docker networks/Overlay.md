---
title: Overlay
tags:
  - advanced
---

# Overlay

## Parent
- [[Docker networks]]

---

## Définition

Le driver `overlay` crée un réseau distribué qui s'étend sur plusieurs hôtes Docker (Swarm). Il encapsule le trafic réseau entre hôtes via VXLAN, permettant aux conteneurs sur des machines différentes de communiquer comme s'ils étaient sur le même réseau local.

---

## Prérequis

```bash
# Docker Swarm doit être initialisé
docker swarm init

# Les ports suivants doivent être ouverts entre les hôtes
# TCP 2377 : gestion du cluster
# TCP/UDP 7946 : communication entre nœuds
# UDP 4789 : trafic overlay (VXLAN)
```

---

## Créer un réseau overlay

```bash
# Créer un réseau overlay dans Swarm
docker network create   --driver overlay   --attachable   mon-overlay-net

# Déployer un service sur ce réseau
docker service create   --name api   --network mon-overlay-net   --replicas 3   mon-app:latest
```

---

## En Docker Compose (Swarm mode)

```yaml
networks:
  backend:
    driver: overlay
    attachable: true

services:
  api:
    image: mon-app
    networks:
      - backend
    deploy:
      replicas: 3
```

---

> [!note]
> Les réseaux overlay sont spécifiques à Docker Swarm. Pour Kubernetes, les réseaux inter-pods sont gérés par des plugins CNI (Calico, Flannel, Cilium).
