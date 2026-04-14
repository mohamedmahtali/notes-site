---
title: NAT
tags:
  - advanced
---

# NAT

## Parent
- [[iptables]]

---

## Définition

NAT (Network Address Translation) traduit les adresses IP dans les paquets. Utilisé pour partager une IP publique entre plusieurs machines privées (MASQUERADE/SNAT) ou rediriger des connexions vers des machines internes (DNAT).

---

## MASQUERADE (sortie internet)

```bash
# Permettre aux machines du réseau local d'accéder à internet
# via l'interface eth0 (IP publique)

echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
```

---

## DNAT (redirection de port)

```bash
# Rediriger le port 80 de l'hôte vers un conteneur sur :8080
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT   --to-destination 172.17.0.2:8080

# Port forwarding SSH (externe:2222 → interne:22)
iptables -t nat -A PREROUTING -p tcp --dport 2222 -j DNAT   --to-destination 192.168.1.10:22
```

---

## SNAT (IP fixe)

```bash
# Remplacer l'IP source par une IP fixe spécifique
iptables -t nat -A POSTROUTING -o eth0 -j SNAT   --to-source 203.0.113.10
```
