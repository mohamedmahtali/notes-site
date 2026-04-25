---
title: NodePort
tags:
  - beginner
---
# NodePort

---

## Définition

NodePort [[EXPOSE]] le service sur un port statique (30000-32767) de chaque [[Node]] du [[Cluster]]. Toute requête vers `<node-IP>:<nodePort>` est routée vers le service. Accessible depuis l'extérieur du cluster sans load balancer [[Cloud]].

---

## Manifeste

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-nodeport
spec:
  type: NodePort
  selector:
    app: myapp
  ports:
  - port: 80           # port ClusterIP interne
    targetPort: 8080   # port du container
    nodePort: 30080    # port exposé sur les nodes (30000-32767)
                       # si omis, Kubernetes en choisit un aléatoire
```

---

## Accès

```bash
# Accessible depuis n'importe quel node
curl http://<node-ip>:30080

# Sur Minikube
minikube service myapp-nodeport --url

# Voir le NodePort assigné
kubectl get svc myapp-nodeport
# NAME              TYPE       CLUSTER-IP   EXTERNAL-IP   PORT(S)
# myapp-nodeport    NodePort   10.96.1.5    <none>        80:30080/TCP
```

---

> [!warning]
> NodePort est principalement pour le développement et les tests. En production, utiliser [[LoadBalancer]] (cloud) ou [[Ingress]] (plus flexible, moins coûteux que plusieurs LoadBalancers).
