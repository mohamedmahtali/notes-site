---
title: LoadBalancer
tags:
  - intermediate
---
# LoadBalancer

## Parent
- [[Services]]

---

## Définition

Un Service LoadBalancer provisionne automatiquement un load balancer externe via le cloud provider (AWS ELB, GCP Load Balancer, Azure LB). Il expose le service avec une IP publique et gère la distribution du trafic.

---

## Manifeste

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-lb
  annotations:
    # Annotations spécifiques AWS
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
    service.beta.kubernetes.io/aws-load-balancer-internal: "false"
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - port: 443
    targetPort: 8443
    protocol: TCP
```

---

## Voir l'IP externe

```bash
kubectl get svc myapp-lb -w
# NAME        TYPE           CLUSTER-IP    EXTERNAL-IP      PORT(S)
# myapp-lb    LoadBalancer   10.96.1.5     <pending>        443:32567/TCP
# myapp-lb    LoadBalancer   10.96.1.5     54.123.45.67     443:32567/TCP
```

---

## Inconvénient

> [!warning] Un LoadBalancer = un LB cloud = coût
> Chaque Service de type LoadBalancer crée un load balancer cloud séparé (et facturé). Pour exposer plusieurs services HTTP/HTTPS, utiliser [[Ingress]] — un seul LB, routing basé sur les paths/hostnames.
