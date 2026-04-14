---
title: Opaque secrets
tags:
  - intermediate
---
# Opaque secrets

## Parent
- [[Secrets]]

---

## Définition

Le type `Opaque` est le type de Secret par défaut pour les données arbitraires. Les valeurs sont stockées en base64 (encodage, pas chiffrement). C'est le type utilisé pour les mots de passe, API keys, et connexions.

---

## Créer un Secret Opaque

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
  namespace: production
type: Opaque
data:
  username: YWRtaW4=          # base64("admin")
  password: czNjcjN0          # base64("s3cr3t")
# Ou utiliser stringData (Kubernetes encode automatiquement)
stringData:
  username: admin
  password: s3cr3t
```

---

## Utiliser dans un pod

```yaml
# Via variables d'environnement
env:
- name: DB_USER
  valueFrom:
    secretKeyRef:
      name: db-credentials
      key: username
- name: DB_PASS
  valueFrom:
    secretKeyRef:
      name: db-credentials
      key: password

# Via volume (mise à jour automatique)
volumes:
- name: db-creds
  secret:
    secretName: db-credentials
```

---

```bash
# Décoder une valeur
kubectl get secret db-credentials -o jsonpath='{.data.password}' | base64 -d

# Ne pas logger les secrets
kubectl get secret db-credentials -o yaml
# → les valeurs apparaissent encodées (base64)
```
