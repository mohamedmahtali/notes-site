---
title: TCP and UDP
tags:
  - beginner
---

# TCP and UDP

---

## Définition

TCP et UDP sont les deux protocoles de transport principaux au-dessus d'IP. TCP est orienté connexion et fiable ; UDP est sans connexion et rapide.

---

## TCP (Transmission Control Protocol)

```
- Connexion en 3 phases (SYN → SYN-ACK → ACK)
- Garantit la livraison et l'ordre des paquets
- Contrôle de flux et congestion
- Plus lent mais fiable
```

**Usages** : HTTP/HTTPS, [[SSH]], FTP, emails, bases de données

---

## UDP (User Datagram Protocol)

```
- Sans connexion (fire-and-forget)
- Pas de garantie de livraison ni d'ordre
- Très rapide, overhead minimal
- L'application gère la fiabilité si besoin
```

**Usages** : [[DNS]], streaming vidéo, jeux en ligne, VoIP, DHCP

---

## Comparaison

| Critère | TCP | UDP |
|---|---|---|
| Connexion | Orienté connexion | Sans connexion |
| Fiabilité | ✅ Garantie | ❌ Non garantie |
| Ordre | ✅ Garanti | ❌ Non garanti |
| Vitesse | Plus lent | Plus rapide |
| Header | 20+ octets | 8 octets |

---

## Vérifier les connexions

```bash
# Voir les connexions TCP établies
ss -tnp

# Voir les ports UDP en écoute
ss -unp

# Tester un port TCP
nc -zv 192.168.1.10 80
telnet 192.168.1.10 80
```
