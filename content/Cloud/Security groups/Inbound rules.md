---
title: Inbound rules
tags:
  - beginner
---
# Inbound rules

## Parent
- [[Security groups]]

---

## Définition

Les règles inbound contrôlent le trafic entrant vers une instance. Par défaut, tout le trafic entrant est bloqué — il faut explicitement autoriser chaque port/protocole nécessaire.

---

## Règles typiques par type de serveur

```
Web server (public) :
  TCP 80  → 0.0.0.0/0 (HTTP)
  TCP 443 → 0.0.0.0/0 (HTTPS)
  TCP 22  → 10.0.0.0/8 (SSH depuis le réseau interne)

App server (privé) :
  TCP 8080 → sg-loadbalancer (depuis le LB uniquement)
  TCP 22   → sg-bastion (depuis le bastion uniquement)

Database (privé) :
  TCP 5432 → sg-appserver (PostgreSQL depuis l'app uniquement)
```

---

## Principe du moindre privilège

> [!warning] Ne jamais exposer les ports admin
> - Jamais `0.0.0.0/0` sur le port 22 (SSH), 3306 (MySQL), 5432 (PostgreSQL)
> - Référencer des Security Groups plutôt que des IPs quand possible
> - Utiliser AWS Systems Manager Session Manager pour SSH sans port 22 exposé
