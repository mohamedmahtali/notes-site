---
title: Logging
tags:
  - intermediate
---
# Logging

---

## Définition

Les logs sont des enregistrements textuels d'événements dans un système. Ils répondent à "pourquoi" un problème s'est produit — complément des métriques qui répondent à "combien". Les logs modernes sont structurés (JSON) et centralisés.

---

## Niveaux de log

| Niveau | Usage |
|---|---|
| DEBUG | Diagnostic détaillé (dev uniquement) |
| INFO | Événements normaux du business |
| WARNING | Situation anormale mais non bloquante |
| ERROR | Erreur récupérable |
| CRITICAL | Erreur fatale, service indisponible |

---

## Pourquoi c'est important

> [!tip] Les logs pour le "pourquoi"
> Quand [[Prometheus]] détecte une anomalie (spike d'erreurs), les logs permettent de comprendre pourquoi : quelle requête a échoué, quelle exception a été levée, quel utilisateur était concerné.

---

## Logs structurés (JSON)

```python
# Python — structlog
import structlog

log = structlog.get_logger()

log.info("request.received",
    method="POST",
    path="/api/orders",
    user_id="usr_123",
    duration_ms=42
)
# → {"event": "request.received", "method": "POST", "path": "/api/orders",
#     "user_id": "usr_123", "duration_ms": 42, "timestamp": "..."}
```

```go
// Go — slog (stdlib depuis Go 1.21)
import "log/slog"

slog.Info("request received",
    "method", "POST",
    "path", "/api/orders",
    "user_id", "usr_123",
    "duration_ms", 42,
)
```

> [!tip] Champ `trace_id` obligatoire
> Toujours inclure un `trace_id` (corrélation ID) dans les logs. Il permet de retrouver tous les logs liés à une seule requête dans un système distribué.

## Stacks de centralisation

| Stack | Composants | Usage |
|-------|-----------|-------|
| **ELK** | Elasticsearch + Logstash + Kibana | Recherche full-text puissante |
| **EFK** | Elasticsearch + Fluentd + Kibana | K8s natif (Fluentd DaemonSet) |
| **Loki + [[Grafana]]** | Loki + Promtail + Grafana | Léger, orienté labels (comme Prometheus) |
| **CloudWatch** | [[AWS]] natif | Simple si tout est sur AWS |

## Collecte dans Kubernetes (Promtail)

```yaml
# DaemonSet Promtail — collecte les logs de tous les pods
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: promtail
spec:
  template:
    spec:
      containers:
      - name: promtail
        image: grafana/promtail:latest
        args:
        - -config.file=/etc/promtail/config.yaml
        volumeMounts:
        - name: varlog
          mountPath: /var/log
          readOnly: true
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```

## Requêtes LogQL (Loki)

```logql
# Tous les logs ERROR du namespace production
{namespace="production"} |= "ERROR"

# Taux d'erreurs par app (sur 5 min)
rate({namespace="production"} |= "ERROR" [5m])

# Parser le JSON et filtrer par champ
{app="myapp"} | json | status_code >= 500

# Top des paths les plus en erreur
topk(10, sum by (path) (rate({app="myapp"} | json | status_code >= 500 [5m])))
```

> [!note]
> Voir [[Structured logs]] pour le format JSON, [[Centralized logging]] pour la collecte, [[Loki]] pour la stack Grafana.
