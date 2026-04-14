---
title: Volumes
tags:
  - intermediate
---
# Volumes

## Parent
- [[Kubernetes]]

## Enfants
- [[emptyDir]]
- [[hostPath]]
- [[Persistent volumes]]
- [[Persistent volume claims]]

---

## Définition

Les volumes Kubernetes permettent aux containers de persister des données et de les partager entre containers d'un même pod. Contrairement aux layers Docker, les volumes survivent aux redémarrages du container (mais pas forcément à la suppression du pod).

---

## Types de volumes

| Type | Durée de vie | Usage |
|---|---|---|
| `emptyDir` | Durée du pod | Partage inter-containers, cache temporaire |
| `hostPath` | Permanente (node) | Accès au filesystem du node |
| `configMap` / `secret` | Durée du pod | Injecter de la configuration |
| `persistentVolumeClaim` | Indépendante du pod | Stockage persistant production |
| `emptyDir (Memory)` | Durée du pod | tmpfs en mémoire (très rapide) |

---

## Exemple

```yaml
spec:
  containers:
  - name: app
    volumeMounts:
    - name: data
      mountPath: /var/data
    - name: config
      mountPath: /etc/config
      readOnly: true
    - name: cache
      mountPath: /tmp/cache
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: my-pvc
  - name: config
    configMap:
      name: app-config
  - name: cache
    emptyDir:
      medium: Memory     # tmpfs
      sizeLimit: 256Mi
```

---

> [!note]
> Voir [[Persistent volumes]] et [[Persistent volume claims]] pour le stockage durable en production.
