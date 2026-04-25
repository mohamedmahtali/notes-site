---
title: Multi tenancy
tags:
  - advanced
---
# Multi tenancy

---

## Définition

Le multi-tenancy [[Kubernetes]] permet à plusieurs équipes ou clients de partager un même [[Cluster]] en toute isolation. Les [[Namespaces]] combinés avec [[RBAC]], NetworkPolicies, et ResourceQuotas constituent les briques de base de cette isolation.

---

## Isolation multi-tenant

```
Cluster K8s
├── Namespace: team-alpha
│   ├── RBAC: alpha-devs peuvent deploy dans team-alpha uniquement
│   ├── NetworkPolicy: team-alpha ne peut pas parler à team-beta
│   └── ResourceQuota: max 10 CPU, 20Gi RAM
├── Namespace: team-beta
│   ├── RBAC: beta-devs peuvent deploy dans team-beta uniquement
│   └── ResourceQuota: max 5 CPU, 10Gi RAM
└── Namespace: shared-infra
    └── Services partagés (Prometheus, Ingress controller)
```

---

## Configuration type

```bash
# Créer le namespace avec labels
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Namespace
metadata:
  name: team-alpha
  labels:
    team: alpha
    tier: tenant
EOF

# RBAC — accès limité au namespace
kubectl create rolebinding alpha-devs   --clusterrole=edit   --group=team-alpha-devs   --namespace=team-alpha
```

---

## Network isolation

```yaml
# Bloquer tout le trafic inter-namespace par défaut
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
  namespace: team-alpha
spec:
  podSelector: {}
  policyTypes: [Ingress]
```

---

> [!note]
> Pour une isolation forte (multi-tenant [[SaaS]]), envisager des outils comme Loft, Capsule, ou vCluster qui ajoutent une couche de virtualisation au-dessus des namespaces.
