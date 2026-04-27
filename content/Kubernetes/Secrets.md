---
title: Secrets
tags:
  - intermediate
---
# Secrets

## Définition

Les Secrets [[Kubernetes]] stockent des données sensibles (mots de passe, tokens, certificats) encodées en base64. Ils suivent les mêmes patterns d'injection que les [[ConfigMaps]] mais avec des protections supplémentaires ([[RBAC]], chiffrement [[etcd]]).

> [!warning] base64 ≠ chiffrement
> Les données dans un Secret sont encodées en base64, pas chiffrées. N'importe qui avec accès en lecture au Secret peut décoder les données. La vraie protection vient du RBAC (limiter l'accès aux Secrets) et du chiffrement au repos dans etcd.

## Types de Secrets

| Type | Usage |
|---|---|
| `Opaque` | Données génériques (défaut) |
| `kubernetes.io/tls` | Certificats TLS |
| `kubernetes.io/dockerconfigjson` | Credentials registry Docker |
| `kubernetes.io/service-account-token` | Tokens SA |

## Création

```bash
# Depuis des valeurs littérales
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=s3cr3t

# Depuis des fichiers
kubectl create secret generic tls-cert \
  --from-file=tls.crt=./cert.pem \
  --from-file=tls.key=./key.pem

# TLS secret
kubectl create secret tls myapp-tls \
  --cert=./cert.pem --key=./key.pem

# Vérifier (les valeurs sont en base64)
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d
```

## Injection dans les Pods

Deux méthodes : variables d'environnement ou volume monté.

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: app
      image: my-app:1.0

      # Méthode 1 : variables d'environnement
      env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password

      # Méthode 2 : volume monté (préférable pour les certificats)
      volumeMounts:
        - name: tls-certs
          mountPath: /etc/ssl/app
          readOnly: true

  volumes:
    - name: tls-certs
      secret:
        secretName: myapp-tls
```

Préférer les volumes pour les certificats (rechargement à chaud possible) et les env vars pour les credentials simples.

## Limiter l'accès avec RBAC

```yaml
# Role : lecture seule sur les secrets d'un namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: secret-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]
    resourceNames: ["db-secret"]   # secret spécifique uniquement
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-secret-reader
  namespace: production
subjects:
  - kind: ServiceAccount
    name: app-sa
roleRef:
  kind: Role
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

Règle : donner accès à un secret **nommé** précisément, jamais `resources: ["secrets"]` avec `resourceNames: []` (accès à tous les secrets).

## Chiffrement au repos (etcd)

Par défaut les Secrets sont stockés en clair dans etcd (juste base64). Pour activer le chiffrement :

```yaml
# /etc/kubernetes/encryption-config.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources: [secrets]
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: <base64-encoded-32-byte-key>
      - identity: {}   # fallback pour les secrets non chiffrés
```

Sur les clusters managés (EKS, GKE, AKS), activer l'option "envelope encryption" depuis la console.

## Secrets en production : External Secrets Operator

Stocker des secrets dans etcd reste risqué. La solution production est d'utiliser un gestionnaire de secrets externe :

```
AWS Secrets Manager / HashiCorp Vault / GCP Secret Manager
              ↓
    External Secrets Operator (ESO)
              ↓
    Secret Kubernetes (synchronisé, TTL configurable)
              ↓
         Pod
```

```yaml
# ExternalSecret : pull depuis AWS Secrets Manager
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: db-secret   # Secret K8s créé automatiquement
  data:
    - secretKey: password
      remoteRef:
        key: prod/db/credentials
        property: password
```

## Explorer

- **[[ConfigMaps]]** — même pattern d'injection mais pour les données non sensibles
- **[[RBAC]]** — contrôle d'accès aux Secrets
- **[[etcd]]** — stockage sous-jacent, chiffrement au repos
- **[[External secrets]]** — ESO + AWS Secrets Manager / Vault
