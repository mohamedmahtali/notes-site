---
title: DNS
tags:
  - networking
  - beginner
---

# DNS (Domain Name System)

## Définition

Le DNS est le système qui traduit les noms de domaine lisibles (example.com) en adresses IP (93.184.216.34). C'est l'annuaire d'Internet — sans lui, il faudrait mémoriser des IPs.

> [!tip] Pourquoi c'est important
> Presque tous les problèmes de connectivité commencent par le DNS. "Ça ne marche pas" est souvent une résolution DNS qui échoue, un TTL trop long après une migration, ou un record mal configuré.

## Types de records

| Record | Usage | Exemple |
|--------|-------|---------|
| `A` | Domaine → [[IPv4]] | example.com → 93.184.216.34 |
| `AAAA` | Domaine → [[IPv6]] | example.com → 2606:2800::1 |
| `CNAME` | Alias vers un autre domaine | www → example.com |
| `MX` | Serveur mail | → mail.example.com |
| `TXT` | Texte libre (SPF, DKIM...) | "v=spf1 include:..." |
| `NS` | Serveurs de noms | → ns1.registrar.com |
| `PTR` | IP → domaine (reverse DNS) | 34.216.184.93.in-addr.arpa |
| `SRV` | Service locator | _https._tcp → [[Host]]:443 |

## Hiérarchie DNS

```
. (root)
└── .com (TLD)
    └── example.com (domaine)
        ├── www.example.com
        └── api.example.com
```

## Commandes de diagnostic

```bash
# Résolution simple
dig example.com
dig example.com A
dig example.com MX

# Requête vers un serveur DNS spécifique
dig @8.8.8.8 example.com

# Résolution inverse
dig -x 93.184.216.34

# Tracer la chaîne de résolution
dig +trace example.com

# Plus simple
nslookup example.com
host example.com
```

## Liens

- [[A record]]
- [[CNAME]]
- [[TTL]]
- [[Resolution]]
- [[Networking]]
