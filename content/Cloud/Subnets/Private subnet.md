---
title: Private subnet
tags:
  - beginner
---
# Private subnet

---

## Définition

Un subnet privé n'a pas de route vers un [[Internet [[Gateway]]]] — les ressources sont inaccessibles directement depuis internet. Elles peuvent accéder à internet en sortie via un [[NAT gateway]] dans le subnet public.

---

## Ressources dans un subnet privé

- **Serveurs applicatifs** — [[EC2]], [[EKS]] worker [[Node]]
- **Bases de données** — RDS, ElastiCache
- **[[Services]] internes** — microservices sans exposition publique
- **Lambdas avec accès [[VPC]]** — pour accéder aux ressources privées

---

```yaml
# Terraform — subnet privé avec NAT GW
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.3.0/24"
  availability_zone = "eu-west-1a"

  tags = {
    Name = "private-subnet-1a"
    "kubernetes.io/role/internal-elb" = "1"  # tag pour EKS internal LB
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main.id
  }
}
```
