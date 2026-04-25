---
title: Terraform destroy
tags:
  - intermediate
---
# Terraform destroy

---

## Définition

`terraform destroy` supprime toutes les ressources gérées par [[Terraform]] dans le workspace courant. Opération destructive et irréversible — à utiliser avec précaution.

---

## Utilisation

```bash
# Destroy avec confirmation (affiche le plan de destruction)
terraform destroy

# Destroy automatique (CI/CD, environnements temporaires)
terraform destroy -auto-approve

# Destroy d'une ressource spécifique
terraform destroy -target=aws_instance.web

# Voir ce qui sera détruit avant
terraform plan -destroy
```

---

## Destroy partiel avec remove

```bash
# Retirer une ressource de l'état sans la détruire (K8s 1.17+)
terraform state rm aws_instance.web

# Importer une ressource existante sans la détruire
terraform import aws_instance.web i-1234567890abcdef0
```

---

## Protection contre la destruction accidentelle

```hcl
resource "aws_db_instance" "prod" {
  # ...
  lifecycle {
    prevent_destroy = true    # terraform destroy échouera
  }
}
```

---

> [!warning]
> `terraform destroy` en production est presque toujours une erreur. Protéger les ressources critiques avec `prevent_destroy = true`. En CI/CD, n'automatiser le destroy que pour les environnements de test/review.
