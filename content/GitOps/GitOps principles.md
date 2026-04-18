---
title: GitOps principles
tags: [gitops, intermediate]
---

# GitOps principles

## Définition

Les 4 principes GitOps (formalisés par OpenGitOps/CNCF) définissent les caractéristiques d'un système GitOps valide.

> [!note] Source officielle
> Ces principes sont définis par le groupe de travail OpenGitOps de la CNCF : openGitOps.com

## Les 4 principes

| # | Principe | Description |
|---|---------|-------------|
| 1 | **Déclaratif** | L'état souhaité est décrit déclarativement (pas impérativement) |
| 2 | **Versionné** | L'état est stocké dans Git avec historique immuable |
| 3 | **Appliqué automatiquement** | Les agents appliquent automatiquement les changements |
| 4 | **Réconcilié en continu** | Les agents détectent et corrigent les dérives |

## Liens

- [[Single source of truth]]
- [[Declarative config]]
- [[Reconciliation loop]]
- [[Pull vs Push]]
- [[GitOps]]
