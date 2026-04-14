---
title: Terraform apply
tags:
  - beginner
---
# Terraform apply

## Parent
- [[Terraform]]

---

## Définition

`terraform apply` exécute les changements planifiés pour créer, modifier ou supprimer des ressources. Il affiche d'abord le plan et demande confirmation (sauf si `-auto-approve` est utilisé).

---

## Utilisation

```bash
# Apply avec confirmation manuelle
terraform apply

# Apply automatique (CI/CD)
terraform apply -auto-approve

# Apply d'un plan sauvegardé
terraform plan -out=tfplan
terraform apply tfplan

# Apply sur une ressource spécifique
terraform apply -target=aws_instance.web

# Apply avec variables
terraform apply -var="environment=prod" -var-file=prod.tfvars
```

---

## Workflow CI/CD recommandé

```yaml
# GitHub Actions
- name: Terraform Plan
  run: terraform plan -out=tfplan

- name: Upload plan
  uses: actions/upload-artifact@v4
  with:
    name: tfplan
    path: tfplan

# Job séparé après approbation
- name: Terraform Apply
  run: terraform apply -auto-approve tfplan
```

---

## Après l'apply

```bash
# Voir les outputs
terraform output
terraform output web_ip    # output spécifique

# Voir l'état
terraform show

# Lister les ressources gérées
terraform state list
```

---

> [!warning]
> Ne jamais utiliser `-auto-approve` sans avoir relu le plan. En CI/CD, sauvegarder le plan et appliquer exactement ce plan — pas un nouveau plan qui pourrait avoir changé entre-temps.
