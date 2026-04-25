---
title: Service accounts
tags:
  - intermediate
---
# Service accounts

---

## Définition

Les Service Accounts sont des identités pour les [[Pods]] dans [[Kubernetes]]. Quand une application dans un pod a besoin d'appeler l'API Kubernetes (lister des pods, lire des [[Secrets]]), elle utilise un Service Account pour s'authentifier.

---

## Service account par défaut

```bash
# Chaque namespace a un SA "default"
kubectl get serviceaccount -n production
# NAME      SECRETS   AGE
# default   0         30d

# Le pod utilise "default" si non spécifié
# Le token est monté automatiquement dans le pod
ls /var/run/secrets/kubernetes.io/serviceaccount/
# ca.crt  namespace  token
```

---

## Créer et utiliser un SA

```yaml
# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: myapp
  namespace: production

# Pod qui utilise ce SA
spec:
  serviceAccountName: myapp
  automountServiceAccountToken: true  # false si le pod n'appelle pas l'API
```

---

## RBAC pour le SA

```yaml
# Role
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: myapp-role
  namespace: production
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]

# Binding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: myapp-rolebinding
  namespace: production
subjects:
- kind: ServiceAccount
  name: myapp
  namespace: production
roleRef:
  kind: Role
  name: myapp-role
  apiGroup: rbac.authorization.k8s.io
```

---

> [!tip]
> Toujours créer un ServiceAccount dédié par application (jamais utiliser `default`). Configurer `automountServiceAccountToken: false` sur les pods qui n'appellent pas l'API K8s.
