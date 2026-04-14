---
title: apply
tags:
  - beginner
---
# apply

## Parent
- [[kubectl]]

---

## Définition

`kubectl apply` crée ou met à jour des ressources depuis des manifests YAML/JSON. C'est la commande déclarative recommandée — elle compare l'état désiré (fichier) avec l'état actuel et fait les modifications nécessaires.

---

## Utilisation

```bash
# Appliquer un fichier
kubectl apply -f deployment.yaml

# Appliquer un dossier (tous les .yaml)
kubectl apply -f ./k8s/

# Appliquer récursivement
kubectl apply -R -f ./k8s/

# Voir ce qui va changer (dry-run)
kubectl apply -f deployment.yaml --dry-run=client
kubectl diff -f deployment.yaml    # diff plus lisible

# Depuis stdin
cat deployment.yaml | kubectl apply -f -

# Depuis une URL
kubectl apply -f https://raw.githubusercontent.com/.../manifest.yaml
```

---

## apply vs create vs replace

| Commande | Description | Recommandé |
|---|---|---|
| `apply` | Crée ou met à jour de façon déclarative | ✅ Oui |
| `create` | Crée seulement (échoue si existe) | Non |
| `replace` | Remplace entièrement (peut causer des interruptions) | Non |

---

## Server-side apply (K8s 1.18+)

```bash
kubectl apply --server-side -f deployment.yaml
# Plus précis pour la gestion des champs — recommandé pour les opérateurs
```

---

> [!tip]
> Toujours utiliser `kubectl diff -f` avant `kubectl apply -f` en production pour voir exactement ce qui va changer.
