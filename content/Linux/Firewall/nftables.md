---
title: nftables
tags:
  - advanced
---

# nftables

## Parent
- [[Firewall]]

---

## Définition

nftables est le successeur moderne de iptables/ip6tables/arptables. Plus performant, plus expressif, et avec une syntaxe unifiée pour IPv4/IPv6. C'est l'outil par défaut dans Debian 10+, RHEL 8+.

---

## Commandes essentielles

```bash
# Voir les règles
nft list ruleset

# Voir une table spécifique
nft list table inet filter

# Vider toutes les règles
nft flush ruleset

# Sauvegarder/restaurer
nft list ruleset > /etc/nftables.conf
nft -f /etc/nftables.conf
```

---

## Configuration de base

```nft
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
    chain input {
        type filter hook input priority 0; policy drop;

        # Connexions établies
        ct state established,related accept

        # Loopback
        iif lo accept

        # SSH, HTTP, HTTPS
        tcp dport { 22, 80, 443 } accept

        # ICMP
        ip protocol icmp accept
        ip6 nexthdr ipv6-icmp accept
    }

    chain forward {
        type filter hook forward priority 0; policy drop;
    }

    chain output {
        type filter hook output priority 0; policy accept;
    }
}
```

---

> [!tip]
> nftables unifie IPv4 et IPv6 dans une seule configuration (`inet` couvre les deux). Avec iptables, il fallait deux configurations séparées.
