---
title: Well known ports
tags:
  - beginner
---

# Well known ports

## Parent
- [[Ports]]

---

## Définition

Les well-known ports (0-1023) sont assignés aux services standards par l'IANA. Ils nécessitent des privilèges root pour être utilisés (ou `CAP_NET_BIND_SERVICE`).

---

## Ports courants à connaître

| Port | Protocole | Service |
|---|---|---|
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 8080 | TCP | HTTP alternatif |
| 27017 | TCP | MongoDB |

---

## Services courants hors well-known

| Port | Service |
|---|---|
| 2222 | SSH alternatif |
| 3000 | Node.js dev |
| 5000 | Flask dev |
| 8443 | HTTPS alternatif |
| 9090 | Prometheus |
| 9100 | Node exporter |
| 16443 | Kubernetes API |

---

```bash
# Voir tous les services connus
cat /etc/services | grep -E "^(ssh|http|https|mysql|postgres)"
```
