---
title: Silences
tags:
  - intermediate
---
# Silences

## Parent
- [[Alertmanager]]

---

## Définition

Les silences supprimant temporairement des alertes pendant une maintenance planifiée, un déploiement, ou une investigation. Un silence correspond à des labels précis et a une durée définie.

---

## Créer un silence via amtool

```bash
# Silencer toutes les alertes pendant 2h de maintenance
amtool silence add   --alertmanager.url=http://alertmanager:9093   alertname="HighCPUUsage"   instance="web-01.prod"   --duration=2h   --comment="Maintenance planifiée - remplacement disque"

# Silencer par regex
amtool silence add   --alertmanager.url=http://alertmanager:9093   instance=~"staging-.*"   --duration=4h   --comment="Staging en cours de refonte"

# Lister les silences actifs
amtool silence query --alertmanager.url=http://alertmanager:9093

# Expirer un silence
amtool silence expire --alertmanager.url=http://alertmanager:9093 <silence-id>
```

---

## Via l'API REST

```bash
curl -XPOST http://alertmanager:9093/api/v2/silences   -H 'Content-Type: application/json'   -d '{
    "matchers": [{"name":"alertname","value":"HighErrorRate","isRegex":false}],
    "startsAt": "2024-01-15T10:00:00Z",
    "endsAt": "2024-01-15T12:00:00Z",
    "createdBy": "alice",
    "comment": "Investigating incident #1234"
  }'
```

---

> [!tip]
> Toujours ajouter un commentaire explicatif aux silences (numéro d'incident, raison). Éviter les silences trop larges (`instance=~".*"`) qui masquent des alertes légitimes.
