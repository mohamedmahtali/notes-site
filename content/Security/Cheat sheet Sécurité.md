---
title: Cheat sheet Sécurité
tags:
  - security
  - intermediate
---

# Cheat sheet Sécurité

## OpenSSL

```bash
# Générer une clé privée RSA
openssl genrsa -out key.pem 4096

# Créer un certificat auto-signé
openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout key.pem -out cert.pem -days 365 \
  -subj "/CN=localhost"

# Générer un CSR
openssl req -newkey rsa:2048 -nodes \
  -keyout server.key -out server.csr

# Inspecter un certificat
openssl x509 -in cert.pem -text -noout
openssl x509 -in cert.pem -noout -dates

# Tester TLS d'un serveur
openssl s_client -connect example.com:443
echo | openssl s_client -connect example.com:443 2>/dev/null \
  | openssl x509 -noout -dates
```

## Vault CLI

```bash
# Auth
export VAULT_ADDR='https://vault.internal'
vault login -method=ldap username=user
vault token lookup

# KV secrets
vault kv put secret/myapp key=value
vault kv get secret/myapp
vault kv get -field=key secret/myapp
vault kv delete secret/myapp

# Policies
vault policy list
vault policy read myapp-policy
vault policy write myapp-policy policy.hcl

# Dynamic secrets
vault read database/creds/readonly
vault read aws/creds/s3-readonly
```

## Trivy (scanning)

```bash
# Image
trivy image nginx:latest
trivy image --severity HIGH,CRITICAL nginx:latest
trivy image --ignore-unfixed nginx:latest
trivy image --format json nginx:latest

# Filesystem
trivy fs .
trivy fs --security-checks vuln,secret .

# IaC
trivy config ./terraform/
trivy config ./k8s/
```

## Kubernetes RBAC

```bash
# Vérifier ses permissions
kubectl auth can-i create pods
kubectl auth can-i --list
kubectl auth can-i list secrets --as=alice

# Qui a cluster-admin ?
kubectl get clusterrolebindings -o json \
  | jq '.items[] | select(.roleRef.name=="cluster-admin") | .subjects'

# Créer un role minimal
kubectl create role pod-reader \
  --verb=get,list,watch --resource=pods

kubectl create rolebinding pod-reader-binding \
  --role=pod-reader --user=alice
```

## Gitleaks (détection de secrets)

```bash
# Scanner un repo
gitleaks detect --source .

# Scanner les commits
gitleaks detect --source . --log-opts="HEAD~10..HEAD"

# Pre-commit hook
gitleaks protect --staged
```

## Liens

- [[Security]]
- [[TLS]]
- [[Vault]]
- [[RBAC]]
- [[Image scanning]]
- [[Vulnerability scanning]]
