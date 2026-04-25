---
title: DNS Resolution
tags:
  - networking
  - intermediate
---

# DNS Resolution

## Définition

La résolution DNS est le processus par lequel un nom de domaine est traduit en adresse IP. Elle implique plusieurs acteurs : le client (resolver récursif), les serveurs racines, les serveurs TLD, et les serveurs autoritaires.

> [!note] Recursive vs Authoritative
> Le resolver récursif (8.8.8.8, 1.1.1.1) fait le travail de requêter les différents serveurs. Le serveur autoritaire est celui qui connaît la vraie réponse pour un domaine.

## Processus de résolution

```
Client
  │ "Quelle est l'IP de www.example.com ?"
  ↓
Resolver récursif (8.8.8.8)
  │ Cache miss → demande aux root servers
  ↓
Root server (.)
  │ "Demande au serveur .com"
  ↓
TLD server (.com)
  │ "Demande à ns1.registrar.com"
  ↓
Serveur autoritaire (ns1.registrar.com)
  │ "www.example.com → 93.184.216.34, TTL=3600"
  ↓
Resolver → met en cache → retourne au client
```

## Tracer une résolution

```bash
# Tracer toute la chaîne
dig +trace www.example.com

# Voir la réponse autoritaire
dig @ns1.registrar.com www.example.com

# Tester différents resolvers
dig @8.8.8.8 example.com         # Google
dig @1.1.1.1 example.com         # Cloudflare
dig @9.9.9.9 example.com         # Quad9
```

## Liens

- [[DNS]]
- [[TTL]]
- [[A record]]
