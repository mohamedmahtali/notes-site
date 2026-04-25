---
title: CNAME
tags:
  - beginner
---

# CNAME

---

## Définition

Un CNAME (Canonical Name) est un alias qui pointe vers un autre nom de domaine (pas une IP). Il est utilisé pour que plusieurs noms pointent vers le même serveur sans dupliquer l'IP.

---

## Exemples

```
alias           TTL   type   cible
blog.example.com 300  CNAME  www.example.com
ftp.example.com  300  CNAME  www.example.com
cdn.example.com  300  CNAME  example.cdn-provider.net
```

---

## Commandes

```bash
dig blog.example.com CNAME
# blog.example.com. 300 IN CNAME www.example.com.

# Résolution complète (suit les CNAME)
dig blog.example.com
```

---

## Règles importantes

> [!warning]
> - Un CNAME ne peut pas coexister avec d'autres records sur le même nom (sauf DNSSEC)
> - La racine d'un domaine (`example.com`) ne peut pas être un CNAME → utiliser un ALIAS/ANAME ou un [[A record]]
> - Les CNAME peuvent chaîner : `a → b → c → IP` (mais éviter les chaînes longues)
