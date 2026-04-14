---
title: Assume breach
tags: [security, advanced]
---

# Assume breach

## Définition

"Assume breach" (supposer la compromission) est un principe Zero Trust qui part du postulat que votre réseau est déjà compromis ou le sera. La sécurité est conçue pour limiter les dégâts, pas seulement prévenir l'intrusion.

> [!note] Changement de mentalité
> On ne demande plus "comment éviter la compromission ?" mais "que se passe-t-il si on est compromis, et comment limiter les dégâts ?". C'est la base de la défense en profondeur.

## Principes de conception

```
✓ Segmentation réseau micro-granulaire
✓ Logging et monitoring de TOUT le trafic interne
✓ Accès juste-à-temps (JIT) et juste-assez (JEA)
✓ Chiffrement de bout en bout (même interne)
✓ Rotation régulière des credentials
✓ Plan de réponse aux incidents testé régulièrement
```

## Réponse aux incidents

```bash
# Isoler un pod compromis immédiatement
kubectl label pod suspicious-pod quarantine=true

# Network policy pour isoler
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: quarantine
spec:
  podSelector:
    matchLabels:
      quarantine: "true"
  policyTypes: [Ingress, Egress]
  # Pas de règles = tout bloqué
```

## Liens

- [[Zero trust]]
- [[Verify explicitly]]
- [[Least privilege access]]
