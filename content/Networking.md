---
title: Networking
tags: [networking, intermediate]
---

# Networking (Réseau)

## Définition

Le networking couvre l'ensemble des concepts, protocoles et outils permettant la communication entre systèmes. En DevOps, la compréhension du réseau est essentielle pour diagnostiquer des pannes, configurer des load balancers, sécuriser des communications et architecturer des systèmes distribués.

> [!tip] Pourquoi c'est important
> La plupart des incidents en production ont une composante réseau : latence, DNS mal configuré, firewall bloquant un port, certificat expiré. Maîtriser le réseau permet de diagnostiquer et résoudre ces problèmes rapidement.

## Modèle OSI simplifié

```
Couche 7 — Application  (HTTP, HTTPS, DNS, SMTP)
Couche 4 — Transport     (TCP, UDP) — ports
Couche 3 — Réseau        (IP) — adresses
Couche 2 — Liaison       (Ethernet, MAC)
Couche 1 — Physique      (câbles, Wi-Fi)
```

## Concepts fondamentaux

- **[[DNS]]** — Résolution de noms de domaine en adresses IP
- **[[TCP IP]]** — Protocoles de communication fondamentaux
- **[[OSI model]]** — Modèle de référence en couches
- **[[Load balancing]]** — Distribution du trafic entre serveurs
- **[[Reverse proxy]]** — Nginx, HAProxy, Traefik
- **[[VPN]]** — Tunnels sécurisés entre réseaux

## Commandes de diagnostic

```bash
# DNS
dig example.com
nslookup example.com 8.8.8.8
host -t MX example.com

# Connectivité
ping -c 3 8.8.8.8
traceroute google.com
mtr google.com              # ping + traceroute en temps réel

# Ports & connexions
ss -tlnp                    # Ports en écoute
netstat -an | grep ESTABLISHED
telnet example.com 443      # Tester un port
nc -zv example.com 80 443   # Scanner des ports

# HTTP
curl -I https://example.com
curl -w "\nTime: %{time_total}s\n" https://example.com
```

## Liens

- [[DNS]]
- [[TCP IP]]
- [[OSI model]]
- [[Load balancing]]
- [[Reverse proxy]]
- [[VPN]]
