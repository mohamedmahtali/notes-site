---
title: Application logs
tags:
  - intermediate
---

# Application logs

## Parent
- [[Logs]]

---

## Définition

Les logs applicatifs sont produits par les applications elles-mêmes. Ils documentent les requêtes, les erreurs, les transactions, et les événements métier. Leur format et destination dépendent de la configuration de l'application.

---

## Conventions

```bash
# Logs standard pour les services Linux
/var/log/<service>/access.log   # requêtes réussies
/var/log/<service>/error.log    # erreurs

# Exemples
/var/log/nginx/access.log
/var/log/nginx/error.log
/var/log/mysql/error.log
/var/log/postgresql/postgresql.log
```

---

## Formats courants

```bash
# Format Combined Log (nginx/apache)
192.168.1.5 - - [15/Jan/2024:10:00:00] "GET /api/users HTTP/1.1" 200 1234

# JSON (applications modernes)
{"timestamp":"2024-01-15T10:00:00Z","level":"ERROR","msg":"DB timeout","service":"api"}

# Syslog format
Jan 15 10:00:00 hostname appname[PID]: message
```

---

## Logger en JSON (recommandé)

```python
# Python avec structlog
import structlog
log = structlog.get_logger()
log.error("db_timeout", database="postgres", timeout=30, user_id=123)
```

---

> [!tip] Standardiser les logs applicatifs
> Logs JSON structurés + timestamps ISO 8601 + niveau de log → facilite le parsing par ELK, Loki, ou CloudWatch.
