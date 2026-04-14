---
title: CRD
tags:
  - advanced
---
# CRD

## Parent
- [[Operators]]

---

## Définition

Une Custom Resource Definition (CRD) étend l'API Kubernetes en définissant de nouveaux types de ressources. Après création d'un CRD, les utilisateurs peuvent créer des instances (Custom Resources) avec `kubectl apply` comme pour n'importe quelle ressource native.

---

## Créer un CRD

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.mycompany.com
spec:
  group: mycompany.com
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              engine:
                type: string
                enum: [postgres, mysql]
              version:
                type: string
              storage:
                type: string
  scope: Namespaced
  names:
    plural: databases
    singular: database
    kind: Database
    shortNames: [db]
```

---

## Créer une Custom Resource

```yaml
# Après création du CRD, l'API accepte ce type
apiVersion: mycompany.com/v1
kind: Database
metadata:
  name: production-db
spec:
  engine: postgres
  version: "15"
  storage: 100Gi
```

---

```bash
kubectl get databases
kubectl describe database production-db
kubectl get db   # avec le shortName
```
