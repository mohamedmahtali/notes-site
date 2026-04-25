---
title: Log retention
tags:
  - intermediate
---
# Log retention

---

## Définition

La rétention des logs définit combien de temps les logs sont conservés avant d'être supprimés. Elle dépend des exigences légales, de compliance, et du coût de stockage.

---

## Stratégie de rétention

```yaml
# Loki — configuration de rétention
limits_config:
  retention_period: 30d    # global

# Par tenant/stream
ruler_storage:
  retention:
    - period: 90d
      selector: '{namespace="production", app="payment-service"}'
    - period: 7d
      selector: '{namespace="dev"}'
    - period: 30d   # défaut
```

---

## Exigences légales courantes

| Contexte | Rétention minimale |
|---|---|
| RGPD (UE) | Selon la donnée (pas de minimum fixe) |
| PCI-DSS | 12 mois (3 mois accessibles) |
| SOC 2 | Variable selon le contrôle |
| Logs de sécurité | 1-7 ans selon secteur |

---

## Architecture tiered

```
Hot (0-7 jours)    → stockage rapide (SSD) — recherche fréquente
Warm (7-30 jours)  → stockage medium (HDD)
Cold (30j-1 an)    → object storage (S3/GCS) — faible coût
Archive (1 an+)    → Glacier — accès rare, très faible coût
```

---

> [!tip]
> Séparer les logs par criticité : les logs de sécurité (authentification, accès, modifications) nécessitent une rétention longue. Les logs de debug peuvent être supprimés après 7 jours.
