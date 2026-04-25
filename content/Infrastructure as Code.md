---
title: Infrastructure as Code
tags:
  - iac
  - intermediate
---

# Infrastructure as Code (IaC)

## Définition

L'Infrastructure as Code (IaC) consiste à gérer et provisionner l'infrastructure (serveurs, réseaux, bases de données) via des fichiers de configuration déclaratifs versionnés dans [[Git]], plutôt que via des interfaces manuelles ou des scripts impératifs ad-hoc.

> [!tip] Pourquoi c'est important
> L'IaC rend l'infrastructure reproductible, versionnable et auditable. Recréer un environnement entier prend quelques minutes au lieu de jours. Les erreurs humaines de configuration sont drastiquement réduites, et chaque changement d'infrastructure est tracé dans git.

## Approches

| Approche | Principe | Exemple |
|----------|---------|---------|
| **Déclarative** | Tu décris l'état final souhaité | Terraform, [[Kubernetes]] manifests |
| **Impérative** | Tu décris les étapes pour y arriver | Scripts [[Bash]], Ansible [[Tasks]] |

La plupart des outils modernes favorisent l'approche **déclarative**.

## Bénéfices clés

- **[[Idempotence]]** — Appliquer 10 fois donne le même résultat qu'une seule fois
- **Versionning** — Chaque changement d'infra est un [[Commit]] git avec message et auteur
- **Reproductibilité** — Dev, [[Staging]], production sont identiques
- **Collaboration** — Les PR pour l'infra comme pour le code
- **Documentation vivante** — Le code IS la documentation

## Outils principaux

### [[Terraform]] (provisionnement)
Outil déclaratif de HashiCorp pour créer et gérer des ressources cloud ([[AWS]], GCP, [[Azure]], K8s...) via des fichiers `.tf`. Gère le cycle de vie complet : `plan → apply → destroy`.

### [[Ansible]] (configuration)
Outil de gestion de configuration et d'automatisation. Ansible se connecte via [[SSH]] aux machines et applique des **[[Playbooks]]** (recettes) pour configurer les systèmes, déployer des applications, gérer les utilisateurs...

## Prérequis

Avant IaC, avoir des bases en : [[Cloud]] (ressources, providers), [[Linux]] (SSH, ligne de commande), [[Git]] (versioning, PR).

## Explorer IaC

### Terraform
- **[[Terraform]]** — présentation, workflow plan/apply/destroy
- **[[Terraform providers]]** — AWS, Azure, GCP, Kubernetes
- **[[Terraform state]]** — état de l'infra, backend distant, locking
- **[[Terraform variables]]** — variables, outputs, locals
- **[[Terraform modules]]** — réutilisabilité, modules publics
- **[[Terraform workspaces]]** — environnements multiples

### Ansible
- **[[Ansible]]** — présentation, inventaire, architecture agentless
- **[[Playbooks]]** — structure, play, tasks, handlers
- **[[Roles]]** — organiser les playbooks en rôles réutilisables
- **[[Inventory]]** — fichiers statiques et dynamiques
- **[[Variables]]** (Ansible) — group vars, host vars, facts
- **[[Templates]]** — Jinja2, fichiers de configuration dynamiques

> [!tip] Lab pratique
> → [[Lab IaC — Provisionner un serveur]]
