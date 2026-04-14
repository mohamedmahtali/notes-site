---
title: PaaS
tags:
  - beginner
---
# PaaS

## Parent
- [[Cloud]]

---

## Définition

Platform as a Service : le provider gère l'infrastructure ET le runtime (OS, serveur web, base de données). Tu ne gères que le code de ton application. Focus sur le développement, pas sur l'infra.

---

## Exemples PaaS

| Provider | Service |
|---|---|
| AWS | Elastic Beanstalk, RDS, Lambda |
| GCP | App Engine, Cloud SQL, Cloud Run |
| Azure | App Service, Azure SQL, Azure Functions |
| Heroku | Heroku Dynos |

---

## Avantages vs IaaS

| Aspect | IaaS | PaaS |
|---|---|---|
| Gestion OS | Toi | Provider |
| Scaling | Manuel/ASG | Automatique |
| Patchs sécurité | Toi | Provider |
| Time-to-deploy | Minutes à heures | Secondes |

---

## Exemple Google Cloud Run (PaaS)

```bash
# Déployer une image Docker sans gérer de serveur
gcloud run deploy myapp   --image gcr.io/my-project/myapp:latest   --platform managed   --region europe-west1   --allow-unauthenticated   --min-instances 0   --max-instances 100
```

---

> [!tip]
> Le PaaS est idéal pour les applications stateless. Pour les applications stateful ou avec des dépendances système spécifiques, IaaS ou containers sont préférables.
