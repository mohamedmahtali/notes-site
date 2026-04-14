---
title: kube-proxy
tags:
  - advanced
---
# kube-proxy

## Parent
- [[Node]]

---

## Définition

kube-proxy tourne sur chaque node et maintient les règles réseau (iptables ou IPVS) pour implémenter les Services Kubernetes. Il fait le lien entre les ClusterIPs virtuelles et les IPs réelles des pods.

---

## Comment ça fonctionne

```
Service ClusterIP: 10.96.0.1:80
    ↓ kube-proxy crée des règles iptables
Requête vers 10.96.0.1:80
    → DNAT vers un pod endpoint: 10.244.1.5:8080
    (load balancing round-robin entre les endpoints)
```

---

## Modes de fonctionnement

| Mode | Mécanisme | Performance |
|---|---|---|
| iptables (défaut) | Règles iptables PREROUTING | Bon jusqu'à ~1000 services |
| IPVS | Kernel load balancer | Meilleur pour gros clusters |
| nftables | Successeur iptables (K8s 1.29+) | Moderne et performant |

---

```bash
# Vérifier kube-proxy
kubectl get pods -n kube-system | grep kube-proxy
kubectl logs -n kube-system kube-proxy-xxxxx

# Voir les règles iptables créées par kube-proxy
iptables -t nat -L KUBE-SERVICES -n | head -20

# Mode IPVS
ipvsadm -Ln
```

---

> [!note]
> Avec des CNI comme Cilium, kube-proxy peut être entièrement remplacé par eBPF — plus performant et avec de meilleures capacités d'observabilité.
