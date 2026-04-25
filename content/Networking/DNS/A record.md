---
title: A record
tags:
  - networking
  - beginner
---

# A record

## Définition

Un A record (Address record) est le type de record DNS le plus fondamental. Il mappe un nom de domaine vers une adresse [[IPv4]].

> [!note] AAAA record
> L'AAAA record fait la même chose mais pour [[IPv6]]. Un domaine peut avoir plusieurs A records pour du [[Load balancing]] DNS (round-robin).

## Exemples

```
example.com.     300  IN  A  93.184.216.34
www.example.com. 300  IN  A  93.184.216.34
api.example.com. 60   IN  A  203.0.113.10
api.example.com. 60   IN  A  203.0.113.11  # Multi-A = round-robin DNS
```

## Créer et vérifier

```bash
# Vérifier un A record
dig example.com A
dig +short example.com A

# Depuis un DNS spécifique
dig @1.1.1.1 example.com A

# Via nslookup
nslookup example.com
```

## Wildcard A record

```
*.example.com. 300 IN A 93.184.216.34
# → Tous les sous-domaines non définis pointent vers cette IP
```

## Liens

- [[DNS]]
- [[CNAME]]
- [[TTL]]
