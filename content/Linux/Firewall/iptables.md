---
title: iptables
tags:
  - advanced
---

# iptables

## Parent
- [[Firewall]]

## Enfants
- [[Chains]]
- [[Rules]]
- [[NAT]]
- [[Forwarding]]

---

## Définition

iptables est l'interface classique pour configurer Netfilter, le framework de filtrage du kernel Linux. Bien que remplacé progressivement par nftables, iptables reste très répandu et sa compréhension est essentielle.

---

## Concepts

```
Tables → Chains → Rules

Tables :
  filter  → filtrage (INPUT, FORWARD, OUTPUT)
  nat     → NAT/masquerading (PREROUTING, POSTROUTING)
  mangle  → modification de paquets

Chains :
  INPUT    → paquets destinés à la machine locale
  OUTPUT   → paquets émis par la machine locale
  FORWARD  → paquets en transit (routeur)
  PREROUTING  → avant routage (DNAT)
  POSTROUTING → après routage (SNAT/masquerade)
```

---

## Commandes essentielles

```bash
# Voir les règles
iptables -L -v -n --line-numbers

# Politique par défaut
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Autoriser les connexions établies
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT   # loopback

# Autoriser SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Sauvegarder/restaurer
iptables-save > /etc/iptables/rules.v4
iptables-restore < /etc/iptables/rules.v4
```
