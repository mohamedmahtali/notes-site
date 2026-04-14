---
title: DNS Implémentation
tags:
  - intermediate
---

# DNS Implémentation

## Parent
- [[DNS]]

---

## Serveurs DNS courants

| Logiciel | Usage |
|---|---|
| BIND (named) | Standard historique, très configurable |
| Unbound | Résolveur récursif sécurisé |
| PowerDNS | API-driven, moderne |
| CoreDNS | Kubernetes DNS natif |
| dnsmasq | Légère résolution locale + DHCP |

---

## Configuration Linux client

```bash
# /etc/resolv.conf
nameserver 8.8.8.8
nameserver 1.1.1.1
search example.com   # domaine de recherche par défaut
```

---

## DNS populaires

```
8.8.8.8 / 8.8.4.4    → Google DNS
1.1.1.1 / 1.0.0.1    → Cloudflare (plus rapide)
9.9.9.9              → Quad9 (filtrage malware)
208.67.222.222       → OpenDNS
```

---

## CoreDNS (Kubernetes)

```yaml
# ConfigMap CoreDNS dans kube-system
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        kubernetes cluster.local in-addr.arpa ip6.arpa {
            pods insecure
            fallthrough in-addr.arpa ip6.arpa
        }
        forward . 8.8.8.8
        cache 30
    }
```
