---
title: Forwarding
tags:
  - advanced
---

# Forwarding

## Parent
- [[iptables]]

---

## Définition

Le forwarding IP permet à une machine Linux d'agir comme routeur — retransmettre des paquets d'une interface réseau à une autre. Utilisé pour les VPN, NAT, containers, et la mise en réseau avancée.

---

## Activer le forwarding

```bash
# Temporaire
echo 1 > /proc/sys/net/ipv4/ip_forward

# Permanent (/etc/sysctl.conf ou /etc/sysctl.d/99-ip-forward.conf)
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1

# Appliquer
sysctl -p
```

---

## Règles iptables pour le forwarding

```bash
# Autoriser le forward entre deux réseaux
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

# Avec état (recommandé)
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -m state --state NEW -j ACCEPT
```

---

> [!note]
> Docker active automatiquement le forwarding IP et crée des règles iptables pour ses réseaux. Kubernetes fait de même. Ne pas désactiver accidentellement le forwarding sur des serveurs qui font tourner des containers.
