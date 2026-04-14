---
title: Shared responsibility model
tags:
  - intermediate
---
# Shared responsibility model

## Parent
- [[Cloud computing]]

---

## Définition

Le modèle de responsabilité partagée définit ce que le cloud provider gère versus ce que le client doit gérer. La frontière dépend du modèle de service (IaaS/PaaS/SaaS).

---

## Responsabilités

```
                    IaaS        PaaS        SaaS
Applications       CLIENT      CLIENT      PROVIDER
Runtime/OS         CLIENT      PROVIDER    PROVIDER
Virtualisation     PROVIDER    PROVIDER    PROVIDER
Infra physique     PROVIDER    PROVIDER    PROVIDER
Sécurité données   CLIENT      CLIENT      PARTAGÉ
Identité/accès     CLIENT      CLIENT      CLIENT
```

---

## Pourquoi c'est important

> [!warning] "Security OF the cloud" vs "Security IN the cloud"
> AWS/GCP/Azure sécurisent l'infrastructure physique et la virtualisation. Mais toi tu es responsable de : configurer les security groups, chiffrer les données, gérer les permissions IAM, patcher les OS (IaaS), et protéger tes applications.

---

## Ce que ça implique en pratique

```bash
# Le provider gère : hardware, hyperviseur, réseau physique
# Toi tu gères :
# - Chiffrement des données au repos et en transit
aws s3api put-bucket-encryption --bucket my-bucket   --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'

# - Accès IAM (principe du moindre privilège)
# - Configuration des security groups
# - Mises à jour de l'OS (IaaS)
# - Backup des données
```
