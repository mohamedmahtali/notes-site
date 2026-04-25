---
title: Local state
tags:
  - beginner
---
# Local state

---

## Définition

Par défaut, [[Terraform]] stocke le state localement dans `terraform.tfstate`. Simple pour le développement, mais dangereux en équipe — chaque développeur a son propre state, les conflits sont fréquents.

---

## Quand l'utiliser

- Développement local solo
- Environnements de test éphémères
- Apprentissage de Terraform

---

## Problèmes du local state en équipe

```
Développeur A : terraform apply → state local A
Développeur B : terraform apply → state local B
                                   → créé en double !
```

---

## Structure du fichier state

```json
{
  "version": 4,
  "terraform_version": "1.6.0",
  "resources": [
    {
      "type": "aws_instance",
      "name": "web",
      "instances": [
        {
          "attributes": {
            "id": "i-1234567890abcdef0",
            "instance_type": "t3.medium",
            "public_ip": "54.123.45.67"
          }
        }
      ]
    }
  ]
}
```

---

> [!warning]
> Ne jamais committer `terraform.tfstate` dans [[Git]] — il peut contenir des données sensibles (IPs, ARNs, parfois des valeurs de [[Variables]]). L'ajouter au `.gitignore`.
