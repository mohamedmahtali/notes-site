---
title: Advanced Kubernetes
tags:
  - advanced
---
# Advanced Kubernetes

---

## Définition

Les fonctionnalités avancées de [[Kubernetes]] permettent de contrôler finement le placement des [[Pods]], l'isolation réseau, la disponibilité lors des maintenances, et la validation des ressources à la création.

---

## Vue d'ensemble

| Fonctionnalité | Objectif |
|---|---|
| [[Taints and tolerations]] | Réserver des [[Node]] pour certains workloads |
| [[Affinity and anti-affinity]] | Colocaliser ou séparer les pods |
| [[Network policies]] | Micro-segmentation réseau |
| [[Pod disruption budgets]] | Garantir la disponibilité lors des maintenances |
| [[Admission controllers]] | Valider/muter les ressources à la création |

---

## Quand utiliser quoi

```
"Ce node est réservé aux GPU" → Taint + Toleration
"Ces 3 pods doivent être sur des nodes différents" → Anti-affinity
"Ce service ne peut pas parler à cet autre" → NetworkPolicy
"Jamais moins de 2 pods disponibles lors d'une mise à jour" → PodDisruptionBudget
"Toutes les images doivent venir de notre registry" → AdmissionController
```
