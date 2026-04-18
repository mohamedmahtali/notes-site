---
title: Vertical scaling
tags:
  - beginner
---
# Vertical scaling

## Parent
- [[Autoscaling]]

---

## Définition

Le scaling vertical (scale up/down) change le type d'instance pour une instance plus ou moins puissante. Nécessite généralement un redémarrage. Limité par les tailles d'instances disponibles.

---

## Quand utiliser

- Bases de données (souvent difficiles à scaler horizontalement)
- Applications legacy non-distribuées
- Workloads avec état qui ne peuvent pas être facilement répliqués

---

```bash
# AWS — redimensionner une instance EC2
# 1. Arrêter l'instance
aws ec2 stop-instances --instance-ids i-abc123

# 2. Changer le type
aws ec2 modify-instance-attribute   --instance-id i-abc123   --instance-type '{"Value":"m5.xlarge"}'

# 3. Redémarrer
aws ec2 start-instances --instance-ids i-abc123

# RDS — scaling vertical sans interruption (quelques minutes)
aws rds modify-db-instance   --db-instance-identifier mydb   --db-instance-class db.r5.xlarge   --apply-immediately
```

---

## Kubernetes — VPA (Vertical Pod Autoscaler)

Le VPA ajuste automatiquement les `requests` et `limits` des conteneurs selon la consommation réelle.

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: myapp-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  updatePolicy:
    updateMode: "Auto"    # Off | Initial | Recreate | Auto
  resourcePolicy:
    containerPolicies:
    - containerName: myapp
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 4
        memory: 4Gi
```

```bash
# Voir les recommandations VPA (sans les appliquer)
kubectl describe vpa myapp-vpa
# → Recommends: cpu=250m, memory=512Mi
```

> [!warning] VPA et HPA ne se combinent pas sur CPU/mémoire
> HPA scale le nombre de replicas sur CPU. VPA ajuste les requests CPU. Les utiliser ensemble sur la même métrique crée des conflits. Solution : HPA sur métriques custom (RPS), VPA pour CPU/mémoire.

> [!tip]
> Pour RDS, le scaling vertical est l'approche principale. Un Multi-AZ RDS effectue le resize avec failover automatique — downtime de ~1-2 minutes.
