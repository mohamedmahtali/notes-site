---
title: Init containers
tags:
  - intermediate
---
# Init containers

## Parent
- [[Pods]]

---

## Définition

Les init containers sont des containers qui s'exécutent séquentiellement avant les containers principaux du pod. Ils doivent tous réussir (code de sortie 0) avant que les containers applicatifs démarrent. Utilisés pour la configuration initiale et les checks de dépendances.

---

## Cas d'usage

- Attendre qu'une base de données soit prête
- Copier des fichiers de configuration
- Initialiser un volume partagé
- Migrer un schéma de base de données
- Récupérer des secrets depuis un vault

---

## Manifeste

```yaml
spec:
  initContainers:
  - name: wait-for-db
    image: busybox:1.35
    command: ['sh', '-c', 'until nc -z postgres 5432; do echo waiting for db; sleep 2; done']

  - name: run-migrations
    image: myapp:1.0
    command: ['python', 'manage.py', 'migrate']
    env:
    - name: DATABASE_URL
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: url

  containers:
  - name: app
    image: myapp:1.0
    # démarre seulement après les 2 init containers
```

---

## Partage de données

```yaml
spec:
  initContainers:
  - name: download-config
    image: alpine
    command: ['wget', '-O', '/config/app.conf', 'http://config-server/config']
    volumeMounts:
    - name: config
      mountPath: /config
  containers:
  - name: app
    image: myapp:1.0
    volumeMounts:
    - name: config
      mountPath: /etc/app
  volumes:
  - name: config
    emptyDir: {}
```
