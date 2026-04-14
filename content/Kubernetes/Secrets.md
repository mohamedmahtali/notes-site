---
title: Secrets
tags:
  - intermediate
---
# Secrets

## Parent
- [[Kubernetes]]

## Enfants
- [[Opaque secrets]]
- [[TLS secrets]]
- [[External secrets]]

---

## Définition

Les Secrets Kubernetes stockent des données sensibles (mots de passe, tokens, certificats) encodées en base64. Ils suivent les mêmes patterns d'injection que les ConfigMaps mais avec des protections supplémentaires (RBAC, chiffrement etcd).

---

## Pourquoi c'est important

> [!warning] base64 ≠ chiffrement
> Les données dans un Secret sont encodées en base64, pas chiffrées. N'importe qui avec accès en lecture au Secret peut décoder les données. La vraie protection vient du RBAC (limiter l'accès aux Secrets) et du chiffrement au repos dans etcd.

---

## Types de Secrets

| Type | Usage |
|---|---|
| `Opaque` | Données génériques (défaut) |
| `kubernetes.io/tls` | Certificats TLS |
| `kubernetes.io/dockerconfigjson` | Credentials registry Docker |
| `kubernetes.io/service-account-token` | Tokens SA |

---

## Création

```bash
# Depuis des valeurs
kubectl create secret generic db-secret   --from-literal=username=admin   --from-literal=password=s3cr3t

# Depuis des fichiers
kubectl create secret generic tls-cert   --from-file=tls.crt=./cert.pem   --from-file=tls.key=./key.pem

# TLS secret
kubectl create secret tls myapp-tls   --cert=./cert.pem   --key=./key.pem
```

---

> [!tip]
> En production, utiliser [[External secrets]] (External Secrets Operator + AWS Secrets Manager / HashiCorp Vault) pour éviter de stocker les secrets dans le cluster ou dans git.
