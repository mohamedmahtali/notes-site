---
title: Terraform outputs
tags:
  - beginner
---
# Terraform outputs

## Parent
- [[Terraform]]

---

## Définition

Les outputs Terraform exposent des valeurs de l'infrastructure déployée : IPs, ARNs, URLs, IDs. Ils permettent de partager des informations entre modules et de les utiliser dans des scripts.

---

## Définition des outputs

```hcl
# outputs.tf
output "web_public_ip" {
  description = "IP publique du serveur web"
  value       = aws_instance.web.public_ip
}

output "load_balancer_dns" {
  description = "DNS du load balancer"
  value       = aws_lb.main.dns_name
}

output "db_endpoint" {
  description = "Endpoint de la base de données"
  value       = aws_db_instance.main.endpoint
  sensitive   = true    # masqué dans les logs terraform
}

output "kubeconfig_command" {
  description = "Commande pour configurer kubectl"
  value       = "aws eks update-kubeconfig --name ${aws_eks_cluster.main.name} --region ${var.region}"
}
```

---

## Utiliser les outputs

```bash
# Afficher tous les outputs
terraform output

# Output spécifique
terraform output web_public_ip

# Format JSON
terraform output -json

# Dans un script
IP=$(terraform output -raw web_public_ip)
ssh ec2-user@$IP
```
