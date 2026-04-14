---
title: Rules
tags:
  - advanced
---

# Rules

## Parent
- [[iptables]]

---

## Définition

Les règles iptables définissent les conditions de filtrage et les actions (ACCEPT, DROP, REJECT, LOG). Elles sont évaluées dans l'ordre — la première règle qui correspond s'applique.

---

## Syntaxe

```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

-A INPUT    : ajouter à la chain INPUT
-p tcp      : protocole TCP
--dport 80  : port destination 80
-j ACCEPT   : action = ACCEPT
```

---

## Actions (targets)

```
ACCEPT  → laisser passer
DROP    → silencieusement rejeter
REJECT  → rejeter avec erreur ICMP
LOG     → logger sans agir (puis continuer)
DNAT    → modifier l'IP destination
SNAT    → modifier l'IP source
MASQUERADE → SNAT avec IP dynamique
RETURN  → revenir à la chain parent
```

---

## Exemples

```bash
# Autoriser les pings
iptables -A INPUT -p icmp -j ACCEPT

# Bloquer une IP
iptables -A INPUT -s 203.0.113.10 -j DROP

# Logger les drops
iptables -A INPUT -j LOG --log-prefix "DROPPED: "
iptables -A INPUT -j DROP

# Rate limiting SSH
iptables -A INPUT -p tcp --dport 22 -m recent --set
iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 4 -j DROP
```
