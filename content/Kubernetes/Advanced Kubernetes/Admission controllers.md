---
title: Admission controllers
tags:
  - advanced
---
# Admission controllers

---

## Définition

Les Admission Controllers sont des plugins qui interceptent les requêtes API [[Kubernetes]] avant la persistance dans [[etcd]]. Ils peuvent valider (rejeter) ou muter (modifier) les ressources à la création/modification.

---

## Types

| Type | Rôle |
|---|---|
| Validating | Valide et accepte/rejette la ressource |
| Mutating | Modifie la ressource avant persistance |

---

## Admission controllers natifs courants

```bash
# Voir les AC actifs
kube-apiserver --help | grep enable-admission-plugins

# Importants par défaut :
# NamespaceLifecycle  — refuse les ressources dans les namespaces en suppression
# LimitRanger         — applique les LimitRanges
# ServiceAccount      — injecte le SA par défaut
# PodSecurity         — applique les Pod Security Standards
# ResourceQuota       — enforce les ResourceQuotas
```

---

## Webhook admission controllers

```yaml
# Validating webhook — exemple: vérifier que les images viennent du registry approuvé
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: image-policy
webhooks:
- name: image-policy.mycompany.com
  rules:
  - apiGroups: [""]
    apiVersions: ["v1"]
    operations: ["CREATE"]
    resources: ["pods"]
  clientConfig:
    service:
      name: image-policy-webhook
      namespace: kube-system
      path: /validate
  admissionReviewVersions: ["v1"]
  sideEffects: None
  failurePolicy: Fail   # rejeter si le webhook est indisponible
```

---

## Outils populaires

```
OPA/Gatekeeper  — politiques en Rego (vérifier labels, images, etc.)
Kyverno         — politiques en YAML natif K8s
Falco           — détection d'intrusion runtime
```

---

> [!tip]
> Configurer `failurePolicy: Ignore` pour les webhooks non-critiques en dev. En production, `Fail` garantit les politiques mais nécessite que le webhook soit HA.
