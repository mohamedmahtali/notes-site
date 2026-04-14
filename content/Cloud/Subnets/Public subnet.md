---
title: Public subnet
tags:
  - beginner
---
# Public subnet

## Parent
- [[Subnets]]

---

## Définition

Un subnet public est un sous-réseau dont la route table contient une route vers un Internet Gateway. Les ressources peuvent recevoir une IP publique et être accessibles depuis internet.

---

## Ressources dans un subnet public

- **Load Balancers** — point d'entrée du trafic
- **NAT Gateways** — pour donner accès internet aux subnets privés
- **Bastion hosts** — point d'accès SSH vers les ressources privées
- **WAF** — Web Application Firewall

---

```yaml
# Terraform — subnet public avec IGW
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "eu-west-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet-1a"
    "kubernetes.io/role/elb" = "1"  # tag pour EKS
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}
```
