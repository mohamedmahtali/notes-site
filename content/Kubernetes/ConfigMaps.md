---
title: ConfigMaps
tags:
  - beginner
---
# ConfigMaps

## Parent
- [[Kubernetes]]

## Enfants
- [[Environment injection]]
- [[Mounted configuration]]

---

## Définition

Un ConfigMap stocke des données de configuration non-sensibles sous forme de paires clé-valeur. Il découple la configuration du code de l'application, permettant de changer la config sans rebuilder l'image.

---

## Création

```bash
# Depuis des valeurs littérales
kubectl create configmap app-config   --from-literal=DATABASE_URL=postgresql://db:5432/myapp   --from-literal=LOG_LEVEL=info

# Depuis un fichier
kubectl create configmap nginx-config --from-file=nginx.conf

# Depuis un répertoire
kubectl create configmap app-configs --from-file=./config/
```

---

## YAML

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # Clé-valeur simples
  LOG_LEVEL: "info"
  MAX_CONNECTIONS: "100"
  # Fichier multi-ligne
  config.yaml: |
    server:
      port: 8080
      timeout: 30s
    database:
      pool_size: 10
```

---

## Injecter dans un pod

```yaml
spec:
  containers:
  - name: app
    envFrom:
    - configMapRef:
        name: app-config      # toutes les clés comme variables env
```

---

> [!note]
> Voir [[Environment injection]] et [[Mounted configuration]] pour les deux façons d'utiliser un ConfigMap.
