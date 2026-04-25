---
title: Layer 7
tags:
  - intermediate
---
# Layer 7

---

## Définition

Un load balancer Layer 7 (application) inspecte le contenu des requêtes HTTP/HTTPS pour router le trafic. Il peut router par path, hostname, headers, ou cookies — essentiel pour les architectures microservices.

---

## Fonctionnalités L7

- **[[Routing]] basé sur le path** : `/api/*` → service API, `/` → frontend
- **Routing basé sur le hostname** : `api.myapp.com` → service API
- **SSL termination** : déchiffre HTTPS au LB, HTTP en interne
- **Sticky sessions** : même client → même backend
- **WAF** : Web Application [[Firewall]] intégré
- **Authentication** : Cognito, OIDC

---

## AWS ALB — règles de routing

```json
{
  "Conditions": [
    {"Field": "host-header", "Values": ["api.myapp.com"]},
    {"Field": "path-pattern", "Values": ["/v2/*"]}
  ],
  "Actions": [
    {"Type": "forward", "TargetGroupArn": "arn:aws:...api-v2-tg..."}
  ],
  "Priority": 10
}
```

---

```bash
# Ajouter une règle de routing
aws elbv2 create-rule   --listener-arn arn:aws:elasticloadbalancing:...   --priority 10   --conditions '[{"Field":"path-pattern","Values":["/api/*"]}]'   --actions '[{"Type":"forward","TargetGroupArn":"arn:aws:..."}]'
```
