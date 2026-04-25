---
title: Firewall
tags:
  - intermediate
---

# Firewall

---

## Définition

Le firewall [[Linux]] filtre le trafic réseau entrant et sortant selon des règles. Le [[Kernel]] Linux utilise Netfilter comme framework de filtrage. Les outils utilisateur (iptables, nftables, ufw) créent des règles dans Netfilter.

---

## Couches

```
Applications (nginx, sshd)
       ↓
Netfilter (kernel)
  ├── iptables  (ancienne interface)
  ├── nftables  (nouvelle interface, depuis 2014)
  └── ufw       (frontend simplifié pour iptables)
```

---

## Choisir son outil

| Outil | Usage | Niveau |
|---|---|---|
| [[ufw]] | Serveurs simples, débutants | Facile |
| [[iptables]] | Configuration complexe, scripts | Avancé |
| [[nftables]] | Moderne, remplacera iptables | Avancé |

---

## Règles fondamentales

```bash
# Politique par défaut recommandée
# - Tout bloquer en entrée par défaut
# - Autoriser les connexions établies
# - Ouvrir seulement ce qui est nécessaire (22, 80, 443)

# Vérifier l'état du firewall
ufw status         # si ufw utilisé
iptables -L -v -n  # si iptables utilisé
nft list ruleset   # si nftables utilisé
```
