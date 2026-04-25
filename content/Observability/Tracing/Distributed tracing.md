---
title: Distributed tracing
tags:
  - advanced
---
# Distributed tracing

---

## Définition

Le [[Tracing]] distribué relie les [[Spans]] de plusieurs [[Services]] en une trace unique pour reconstituer le parcours complet d'une requête. Chaque service propage le contexte de trace dans les headers HTTP.

---

## Architecture

```
Request → Service A (span A)
               → Service B (span B, parent: A)
                    → DB query (span DB, parent: B)
               → Service C (span C, parent: A)
                    → Redis (span Redis, parent: C)

Trace complète : A + B + DB + C + Redis
Latence totale : max(B+DB, C+Redis)
```

---

## Propagation du contexte

```
HTTP Headers :
  traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
              │  │                                │                 │
              │  trace-id (16 bytes)              parent-span-id    flags
              version
```

---

## Instrumentation automatique

```python
# Python — OpenTelemetry auto-instrumentation
opentelemetry-instrument   --traces_exporter jaeger_thrift   --exporter_jaeger_endpoint http://jaeger:14268/api/traces   python myapp.py
```

---

## Dans Grafana (Tempo)

```logql
# Lier logs et traces dans Grafana
# Cliquer sur un trace_id dans les logs → ouvrir dans Tempo
{app="myapp"} | json | trace_id != ""
```
