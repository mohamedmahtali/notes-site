---
title: TCP/IP
tags:
  - networking
  - beginner
---

# TCP/IP

## Définition

TCP/IP est la suite de protocoles qui constitue la base d'Internet. TCP (Transmission Control Protocol) garantit la livraison ordonnée des données. IP (Internet Protocol) gère l'adressage et le routage.

> [!tip] TCP vs UDP
> TCP = fiable mais plus lent (poignée de main, accusés de réception). UDP = rapide mais non fiable (pas de garantie de livraison). HTTP/HTTPS → TCP. DNS, streaming, jeux → UDP.

## TCP — Three-way handshake

```
Client          Serveur
  │── SYN ────────→│   "Je veux me connecter"
  │←── SYN-ACK ───│   "OK, je suis prêt"
  │── ACK ────────→│   "Compris, on commence"
  │                │
  │=== Données ===│
  │                │
  │── FIN ────────→│   "Je ferme la connexion"
  │←── FIN-ACK ───│
```

## Adressage IP

```bash
# Adresses IPv4 (32 bits)
192.168.1.100/24    # Adresse/masque
# → réseau : 192.168.1.0
# → broadcast : 192.168.1.255
# → plage hosts : 192.168.1.1 à .254

# Plages privées (RFC 1918)
10.0.0.0/8          # Classe A (16M hôtes)
172.16.0.0/12       # Classe B (1M hôtes)
192.168.0.0/16      # Classe C (65K hôtes)
```

## Ports courants

| Port | Protocole | Service |
|------|-----------|---------|
| 22 | TCP | [[SSH]] |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 8080 | TCP | HTTP alternatif |

## Outils de diagnostic TCP

```bash
# Connexions établies
ss -tnp state established
netstat -tn

# Suivre les paquets TCP
tcpdump -i eth0 port 80
tcpdump -i eth0 'tcp and host 8.8.8.8'

# Tester un port
nc -zv example.com 443
telnet example.com 80
```

## Liens

- [[OSI model]]
- [[DNS]]
- [[Networking]]
- [[Firewall]]
