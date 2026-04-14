---
title: Exporters
tags:
  - intermediate
---
# Exporters

## Parent
- [[Prometheus]]

---

## Définition

Les exporters sont des agents qui collectent des métriques depuis des systèmes qui n'exposent pas nativement le format Prometheus (serveurs Linux, bases de données, services tiers) et les convertissent en métriques Prometheus.

---

## Exporters courants

| Exporter | Cible | Port |
|---|---|---|
| node_exporter | Serveurs Linux | 9100 |
| blackbox_exporter | URLs, DNS, TCP | 9115 |
| postgres_exporter | PostgreSQL | 9187 |
| redis_exporter | Redis | 9121 |
| mysql_exporter | MySQL | 9104 |
| nginx_exporter | Nginx | 9113 |
| kube-state-metrics | Kubernetes objects | 8080 |

---

## Déployer node_exporter

```bash
# Sur chaque serveur Linux
docker run -d   --net="host"   --pid="host"   -v "/:/host:ro,rslave"   prom/node-exporter:latest   --path.rootfs=/host

# Sur Kubernetes (DaemonSet)
helm install node-exporter prometheus-community/prometheus-node-exporter   --namespace monitoring
```

---

## Blackbox exporter (monitoring externe)

```yaml
# Vérifier qu'une URL répond en HTTPS avec le bon certificat
scrape_configs:
  - job_name: 'blackbox-http'
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
        - https://myapp.com/health
        - https://api.myapp.com/health
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - target_label: __address__
        replacement: blackbox-exporter:9115
```
