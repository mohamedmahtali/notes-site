---
title: Troubleshooting
tags:
  - intermediate
---

# Troubleshooting

---

## Définition

Le troubleshooting réseau est le processus de diagnostic et résolution des problèmes de connectivité. Une approche méthodique couche par couche (physique → IP → transport → application) est plus efficace que de tester au hasard.

---

## Approche en couches

```
1. Interface active ?          ip link show
2. IP configurée ?             ip addr show
3. Gateway accessible ?        ping gateway
4. DNS résolu ?                dig google.com
5. Cible accessible ?          ping cible
6. Port ouvert ?               nc -zv cible port
7. Service répond ?            curl http://cible
```

---

## Outils essentiels

```bash
# Connectivité
ping 8.8.8.8           # ICMP (couche 3)
ping6 2001:4860::      # ICMP IPv6

# Chemin réseau
traceroute 8.8.8.8     # via UDP
traceroute -T 8.8.8.8  # via TCP (passe mieux les firewalls)
mtr 8.8.8.8            # traceroute + ping interactif

# Connexions et ports
ss -tlnp               # ports en écoute
ss -tnp                # connexions établies
netstat -tlnp          # ancienne syntaxe

# DNS
dig google.com         # résolution complète
dig +short google.com  # IP seulement

# HTTP
curl -v https://api.example.com       # requête HTTP verbeuse
curl -I https://api.example.com       # headers seulement
wget --spider https://api.example.com # vérifier accessibilité
```
