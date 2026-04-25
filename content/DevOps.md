---
title: DevOps
tags:
  - beginner
---
# DevOps

---

---

## Définition

**DevOps** est une approche d’ingénierie logicielle qui vise à **rapprocher le développement logiciel (Dev) et l’exploitation des infrastructures (Ops)** afin d’améliorer la **vitesse, la fiabilité et la qualité de livraison des applications**.

Historiquement, les équipes **développement** écrivaient le code puis le transmettaient aux équipes **opérations** qui devaient le déployer et le maintenir en production.  
Ce modèle créait souvent :

- des conflits entre équipes
- des déploiements lents
- des erreurs en production
- un manque de responsabilité partagée

DevOps introduit une **culture de collaboration**, combinée avec **l’automatisation et des outils modernes**, pour transformer la livraison logicielle en **processus continu et reproductible**.

---

## Pourquoi c'est important

DevOps permet de résoudre plusieurs problèmes majeurs dans le développement logiciel moderne.

### 1. Accélérer la livraison des logiciels

Grâce à l'automatisation (tests, build, déploiement), les équipes peuvent livrer des nouvelles fonctionnalités **beaucoup plus rapidement**.

Exemple :

- avant : 1 déploiement tous les 3 mois  
- avec DevOps : plusieurs déploiements **par jour**

---

### 2. Réduire les erreurs en production

Avec :

- des **tests automatisés**
- des **[[Pipeline]] CI/CD**
- des **environnements reproductibles**

les erreurs humaines sont fortement réduites.

---

### 3. Améliorer la collaboration

DevOps casse les silos entre :

- développeurs
- administrateurs systèmes
- ingénieurs [[Cloud]]
- sécurité

Tout le monde partage la responsabilité du produit.

---

### 4. Rendre l'infrastructure programmable

Avec **[[Infrastructure as Code]]**, l’infrastructure devient :

- versionnée
- reproductible
- automatisable

Exemple : créer un serveur avec **[[Terraform]]** plutôt que manuellement.

---

### 5. Améliorer la fiabilité des systèmes

Avec les outils d’**observabilité** :

- logs
- métriques
- [[Monitoring]]
- alertes

les équipes détectent et corrigent les problèmes plus rapidement.

---

## Exemple concret

Sans DevOps :

1. Un développeur écrit une fonctionnalité
2. Il envoie le code à l’équipe ops
3. Les ops déploient manuellement
4. Une erreur survient
5. Débogage long

Avec DevOps :

1. Le développeur pousse le code sur **[[Git]]**
2. Un **pipeline CI/CD** démarre automatiquement
3. Les tests sont exécutés
4. L’image **[[Docker]]** est construite
5. L’application est déployée automatiquement sur **[[Kubernetes]]**

Tout cela peut se produire **en quelques minutes**.

---

## Les piliers du DevOps

Le DevOps repose généralement sur plusieurs piliers techniques.

### Culture

- collaboration
- responsabilité partagée
- communication entre équipes

---

### Automatisation

Automatiser :

- les tests
- le build
- les déploiements
- la création d’infrastructure

---

### Mesure

Mesurer :

- performance
- erreurs
- disponibilité
- utilisation

---

### Partage

Documenter et partager :

- connaissances
- bonnes pratiques
- incidents

---

## Outils typiques du DevOps

| Domaine        | Outils                             |
| -------------- | ---------------------------------- |
| [[Versioning]]     | Git                                |
| CI/CD          | [[GitHub actions]], GitLab CI, [[Jenkins]] |
| Conteneurs     | Docker                             |
| Orchestration  | Kubernetes                         |
| Infrastructure | Terraform                          |
| Cloud          | [[AWS]], GCP, [[Azure]]                    |
| Monitoring     | [[Prometheus]], [[Grafana]]                |

---

## Résumé

DevOps est une **culture + un ensemble de pratiques + des outils** permettant de :

- livrer plus vite
- réduire les erreurs
- automatiser l’infrastructure
- améliorer la fiabilité des systèmes
- rapprocher développeurs et opérations.

C’est aujourd’hui **le modèle dominant pour construire et opérer des applications modernes**.