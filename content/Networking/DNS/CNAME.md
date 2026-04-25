---
title: CNAME
tags:
  - networking
  - beginner
---

# CNAME (Canonical Name)

## Définition

Un CNAME record crée un alias d'un nom de domaine vers un autre. Au lieu de pointer vers une IP, il pointe vers un autre nom de domaine (le "canonical name").

> [!warning] CNAME et apex domain
> Un CNAME ne peut PAS être créé pour un apex domain (example.com). Il faut un A record pour l'apex. Les CDNs contournent cela avec des records ALIAS ou ANAME.

## Exemples

```
www.example.com.  300 IN CNAME example.com.
docs.example.com. 300 IN CNAME readthedocs.io.
mail.example.com. 300 IN CNAME mailgun.org.
```

## Chaîne de CNAME

```
www.example.com → example.com → 93.184.216.34
                    (A record)
```

## Vérifier un CNAME

```bash
dig www.example.com CNAME
dig +short www.example.com    # Suit la chaîne jusqu'à l'IP finale

# nslookup
nslookup -type=CNAME www.example.com
```

## Liens

- [[DNS]]
- [[A record]]
- [[TTL]]
