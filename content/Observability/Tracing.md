---
title: Tracing
tags:
  - advanced
---
# Tracing

## Parent
- [[Observability]]

## Enfants
- [[Distributed tracing]]
- [[Spans]]
- [[Trace context]]
- [[OpenTelemetry]]

---

## Définition

Le tracing distribué suit le chemin d'une requête à travers plusieurs services dans une architecture microservices. Il permet de mesurer la latence de chaque composant et d'identifier où se situe un goulot d'étranglement.

---

## Pourquoi c'est important

> [!note] Quand les métriques ne suffisent pas
> Les métriques indiquent que la latence est haute ; les logs indiquent qu'il y a des erreurs ; le tracing indique QUEL service, QUELLE opération, et COMBIEN DE TEMPS prend chaque étape d'une requête.

---

## Outils

| Outil | Description |
|---|---|
| Jaeger | Tracing distribué open-source (CNCF) |
| Zipkin | Tracing open-source (Twitter) |
| Tempo | Tracing scalable par Grafana |
| Datadog APM | Solution commerciale intégrée |
| AWS X-Ray | Solution AWS native |

---

## Flux d'une trace

```
Client → API Gateway (span 1, 10ms)
    → Auth Service (span 2, 5ms)
    → User Service (span 3, 50ms)
        → PostgreSQL (span 4, 40ms) ← goulot !
    → Response (total: 70ms)
```

---

> [!note]
> Voir [[Distributed tracing]], [[Spans]], [[OpenTelemetry]] pour les concepts et l'implémentation.
