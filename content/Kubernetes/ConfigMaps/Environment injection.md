---
title: Environment injection
tags:
  - beginner
---
# Environment injection

## Parent
- [[ConfigMaps]]

---

## Définition

L'injection d'environnement permet d'utiliser les valeurs d'un ConfigMap comme variables d'environnement dans les containers. Pratique pour les applications qui lisent leur config depuis les variables d'env.

---

## Toutes les clés du ConfigMap

```yaml
spec:
  containers:
  - name: app
    envFrom:
    - configMapRef:
        name: app-config        # toutes les clés → variables env
    - secretRef:
        name: app-secrets       # combiner avec secrets
```

---

## Clés spécifiques

```yaml
spec:
  containers:
  - name: app
    env:
    - name: LOG_LEVEL           # nom de la variable env
      valueFrom:
        configMapKeyRef:
          name: app-config      # nom du ConfigMap
          key: LOG_LEVEL        # clé dans le ConfigMap
    - name: DB_URL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DATABASE_URL
```

---

> [!warning]
> Les variables d'environnement injectées depuis un ConfigMap ne sont **pas mises à jour automatiquement** si le ConfigMap change. Le pod doit être redémarré pour prendre en compte les nouvelles valeurs.
> Pour les mises à jour dynamiques, utiliser les volumes montés ([[Mounted configuration]]).
