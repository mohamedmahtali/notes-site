---
title: "Lab Kubernetes — App avec HPA et Ingress"
tags:
  - kubernetes
  - intermediate
---

# Lab Kubernetes — App avec HPA et Ingress

## Objectif

Déployer une application sur Kubernetes avec : Deployment, Service, Ingress, ConfigMap, HPA ([[Autoscaling]]), et observer le comportement sous charge.

> [!note] Prérequis
> - [[Cluster]] Kubernetes local (kind, minikube, k3d)
> - [[kubectl]] configuré
> - [[Metrics]]-server installé (pour HPA)

---

## Étape 1 — Préparer le cluster

```bash
# Avec kind (recommandé)
cat > kind-config.yaml << 'EOF'
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 80
        hostPort: 80
  - role: worker
  - role: worker
EOF

kind create cluster --config kind-config.yaml

# Installer metrics-server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl patch deployment metrics-server -n kube-system   --type='json'   -p='[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
```

---

## Étape 2 — Créer le namespace et les ressources

```bash
kubectl create namespace lab
kubectl config set-context --current --namespace=lab
```

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: lab
data:
  APP_ENV: "production"
  LOG_LEVEL: "info"
  MAX_CONNECTIONS: "100"
```

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  namespace: lab
spec:
  replicas: 2
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: webapp
          image: nginx:alpine
          ports:
            - containerPort: 80
          envFrom:
            - configMapRef:
                name: app-config
          resources:
            requests:
              cpu: "100m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "128Mi"
          readinessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 10
```

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp
  namespace: lab
spec:
  selector:
    app: webapp
  ports:
    - port: 80
      targetPort: 80
```

```bash
kubectl apply -f configmap.yaml -f deployment.yaml -f service.yaml
kubectl get pods -w  # Attendre que les pods soient Running
```

---

## Étape 3 — Configurer l'Ingress

```bash
# Installer nginx-ingress
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl wait --namespace ingress-nginx   --for=condition=ready pod   --selector=app.kubernetes.io/component=controller   --timeout=90s
```

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp
  namespace: lab
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: webapp.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: webapp
                port:
                  number: 80
```

```bash
kubectl apply -f ingress.yaml

# Tester (ajouter dans /etc/hosts : 127.0.0.1 webapp.local)
curl http://webapp.local
```

---

## Étape 4 — HPA (Horizontal Pod Autoscaler)

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp
  namespace: lab
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: webapp
  minReplicas: 2
  maxReplicas: 8
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
```

```bash
kubectl apply -f hpa.yaml
kubectl get hpa -w
```

---

## Étape 5 — Test de charge

```bash
# Générer de la charge
kubectl run load-test --image=busybox --restart=Never -it --rm --   sh -c "while true; do wget -q -O- http://webapp.lab.svc.cluster.local; done"

# Observer l'autoscaling dans un autre terminal
watch kubectl get hpa,pods -n lab
```

---

## Vérification finale

- [ ] Pods en Running avec 2 replicas minimum
- [ ] Service accessible via `kubectl port-forward`
- [ ] Ingress répond sur `webapp.local`
- [ ] HPA actif (`kubectl get hpa`)
- [ ] Sous charge : HPA scale vers plus de replicas
- [ ] Sans charge : retour à 2 replicas (après ~5min)

## Liens

- [[Kubernetes]]
- [[Pods]]
- [[Services]]
- [[HPA]]
- [[Ingress]]
- [[ConfigMaps]]
