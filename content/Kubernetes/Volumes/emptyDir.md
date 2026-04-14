---
title: emptyDir
tags:
  - beginner
---
# emptyDir

## Parent
- [[Volumes]]

---

## Définition

`emptyDir` est un volume vide créé quand un pod démarre. Il est partagé entre tous les containers du pod et est supprimé quand le pod est supprimé. Utilisé pour le partage de données inter-containers et le cache temporaire.

---

## Cas d'usage

- Partager des fichiers entre containers (app + sidecar)
- Cache de build temporaire
- Répertoire de travail partagé
- tmpfs en mémoire pour les données sensibles éphémères

---

## Manifeste

```yaml
spec:
  containers:
  - name: app
    volumeMounts:
    - name: shared-data
      mountPath: /data
  - name: sidecar
    volumeMounts:
    - name: shared-data
      mountPath: /input
      readOnly: true

  volumes:
  - name: shared-data
    emptyDir: {}          # stocké sur le disque du node

  - name: fast-cache
    emptyDir:
      medium: Memory      # stocké en RAM (tmpfs)
      sizeLimit: 512Mi    # limite la taille

  - name: build-cache
    emptyDir:
      sizeLimit: 2Gi      # limite sur disque
```

---

> [!warning]
> Les données dans `emptyDir` sont perdues quand le pod est supprimé (pas au redémarrage du container). Pour de la persistance, utiliser un [[Persistent volume claims|PVC]].
