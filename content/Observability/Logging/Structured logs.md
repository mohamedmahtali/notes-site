---
title: Structured logs
tags:
  - intermediate
---
# Structured logs

## Parent
- [[Logging]]

---

## Définition

Les logs structurés sont des logs au format JSON (ou autre format parsable) plutôt que du texte libre. Chaque champ est une clé-valeur indexable, ce qui permet des recherches et agrégations précises.

---

## Texte libre vs structuré

```
# Mauvais — texte libre (difficile à parser/rechercher)
2024-01-15 10:23:45 ERROR Failed to process order 12345 for user alice@example.com: DB timeout

# Bon — structuré JSON
{
  "timestamp": "2024-01-15T10:23:45Z",
  "level": "error",
  "message": "Failed to process order",
  "order_id": 12345,
  "user_email": "alice@example.com",
  "error": "DB timeout",
  "duration_ms": 5001,
  "service": "order-service",
  "trace_id": "4bf92f3577b34da6"
}
```

---

## Implémentation par langage

```python
# Python — structlog
import structlog
log = structlog.get_logger()
log.error("Failed to process order",
          order_id=12345,
          user_email="alice@example.com",
          duration_ms=5001)
```

```go
// Go — zerolog
log.Error().
    Int("order_id", 12345).
    Str("user_email", "alice@example.com").
    Int("duration_ms", 5001).
    Msg("Failed to process order")
```

---

> [!tip]
> Toujours inclure : timestamp (UTC), level, message, service, trace_id. Les trace_id permettent de corréler les logs entre microservices pour reconstituer une requête distribuée.
