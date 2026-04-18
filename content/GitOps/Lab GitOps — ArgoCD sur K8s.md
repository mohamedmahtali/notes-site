---
title: "Lab GitOps — ArgoCD sur K8s"
tags: [gitops, intermediate]
---

# Lab GitOps — ArgoCD sur K8s

## Objectif

Installer ArgoCD sur un cluster Kubernetes local, déployer une application depuis Git, tester la réconciliation automatique et le rollback GitOps.

> [!note] Prérequis
> - Cluster Kubernetes local (kind, k3d, minikube)
> - kubectl configuré
> - Compte GitHub avec un repo public ou privé

---

## Étape 1 — Préparer le repo GitOps

Créer un repo GitHub avec la structure :

```
gitops-lab/
└── apps/
    └── webapp/
        ├── deployment.yaml
        ├── service.yaml
        └── configmap.yaml
```

```yaml
# apps/webapp/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  namespace: webapp
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
          image: nginx:1.25
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: 50m
              memory: 32Mi
```

```yaml
# apps/webapp/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp
  namespace: webapp
spec:
  selector:
    app: webapp
  ports:
    - port: 80
      targetPort: 80
```

```bash
git add . && git commit -m "Initial webapp manifests"
git push origin main
```

---

## Étape 2 — Installer ArgoCD

```bash
kubectl create namespace argocd
kubectl apply -n argocd   -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Attendre que les pods soient prêts
kubectl wait --for=condition=Ready pods --all -n argocd --timeout=120s

# Exposer l'UI
kubectl port-forward svc/argocd-server -n argocd 8080:443 &

# Récupérer le mot de passe admin
ARGOCD_PWD=$(kubectl -n argocd get secret argocd-initial-admin-secret   -o jsonpath="{.data.password}" | base64 -d)
echo "Password: $ARGOCD_PWD"
```

---

## Étape 3 — Connecter le repo et créer l'Application

```bash
# Login CLI
argocd login localhost:8080   --username admin   --password $ARGOCD_PWD   --insecure

# Créer l'application
argocd app create webapp   --repo https://github.com/TON_USERNAME/gitops-lab   --path apps/webapp   --dest-server https://kubernetes.default.svc   --dest-namespace webapp   --sync-policy automated   --auto-prune   --self-heal

# Vérifier
argocd app list
argocd app get webapp
```

---

## Étape 4 — Tester la réconciliation

```bash
# Modifier manuellement un pod (dérive intentionnelle)
kubectl scale deployment webapp -n webapp --replicas=5

# Observer : ArgoCD doit revenir à 2 replicas (selfHeal=true)
watch kubectl get pods -n webapp
```

---

## Étape 5 — Déployer une nouvelle version via Git

```bash
# Modifier l'image dans le YAML
# image: nginx:1.25 → nginx:1.26

git add apps/webapp/deployment.yaml
git commit -m "chore: upgrade nginx to 1.26"
git push origin main

# Observer le sync automatique (max 3 minutes par défaut)
argocd app get webapp --watch

# Ou forcer le sync immédiatement
argocd app sync webapp
```

---

## Étape 6 — Rollback

```bash
# Voir l'historique
argocd app history webapp

# Rollback à la révision précédente
argocd app rollback webapp 1

# Vérifier l'image
kubectl get deployment webapp -n webapp -o jsonpath='{.spec.template.spec.containers[0].image}'
```

---

## Vérification finale

- [ ] ArgoCD UI accessible sur https://localhost:8080
- [ ] Application webapp en état `Synced` et `Healthy`
- [ ] Scale manuel à 5 replicas → ArgoCD revient à 2 (selfHeal)
- [ ] Push d'un nouveau tag image → déploiement automatique
- [ ] Rollback via `argocd app rollback` fonctionnel

## Liens

- [[GitOps]]
- [[ArgoCD]]
- [[Applications]]
- [[Sync policies]]
- [[Kubernetes]]
