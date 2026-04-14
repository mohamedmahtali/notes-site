---
title: On demand resources
tags:
  - beginner
---
# On demand resources

## Parent
- [[Cloud computing]]

---

## Définition

Les ressources à la demande sont provisionnées en quelques secondes/minutes et libérées quand elles ne sont plus nécessaires. Pas de contrat à long terme, pas de capacité réservée à l'avance.

---

## Pourquoi c'est important

> [!tip] De 0 à 1000 serveurs en minutes
> Le provisionnement traditionnel prend des semaines (commande, livraison, rack, câblage). Le cloud : une API call, et la ressource est prête en 30 secondes. C'est ce qui rend les architectures élastiques possibles.

---

## Modèles de tarification

| Modèle | Description | Économies |
|---|---|---|
| On-Demand | Payer à l'heure/seconde | 0% (baseline) |
| Reserved Instances | Engagement 1-3 ans | -30% à -60% |
| Spot/Preemptible | Capacité excédentaire | -60% à -90% |
| Savings Plans | Engagement de dépense | -20% à -40% |

---

```bash
# Lancer une instance EC2 à la demande
aws ec2 run-instances   --image-id ami-0abcdef1234567890   --instance-type t3.micro   --count 1

# Terminer quand plus nécessaire
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```
