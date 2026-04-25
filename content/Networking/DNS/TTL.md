---
title: TTL (DNS)
tags:
  - networking
  - beginner
---

# TTL (Time To Live) — DNS

## Définition

Le TTL DNS définit combien de temps (en secondes) un resolver peut mettre en cache un record DNS avant de le re-demander au serveur autoritaire. Un TTL bas = propagation rapide mais plus de requêtes. Un TTL haut = moins de requêtes mais changements lents.

> [!tip] Stratégie de migration
> Avant de migrer un service (changer l'IP d'un A record), baisser le TTL à 60s quelques heures avant. Après migration, remonter à 3600s. Cela garantit une propagation rapide des changements.

## Valeurs courantes

| TTL | Durée | Usage |
|-----|-------|-------|
| 60 | 1 minute | Migration imminente |
| 300 | 5 minutes | Changements fréquents |
| 3600 | 1 heure | Standard |
| 86400 | 24 heures | Records stables (MX, NS) |

## Vérifier le TTL d'un record

```bash
# Le TTL apparaît dans la réponse dig (3e colonne)
dig example.com A
# example.com.  3600  IN  A  93.184.216.34
#               ^^^^
#               TTL en secondes

# Voir le TTL résiduel (dans le cache d'un resolver)
dig @8.8.8.8 example.com A
```

## Liens

- [[DNS]]
- [[A record]]
- [[CNAME]]
- [[Resolution]]
