---
title: Security
tags:
  - security
  - intermediate
---

# Security (Sécurité DevOps)

## Définition

La sécurité [[DevOps]] (DevSecOps) intègre les pratiques de sécurité à chaque étape du cycle de vie logiciel — du code à la production. Elle repose sur l'automatisation des contrôles de sécurité pour détecter et corriger les vulnérabilités tôt, avant qu'elles n'atteignent la production.

> [!warning] Pourquoi c'est critique
> 94% des organisations ont eu un incident de sécurité lié à des vulnérabilités connues non patchées. La sécurité intégrée au [[Pipeline]] CI/CD (shift left) réduit le coût de correction d'un facteur 30x par rapport à une détection en production.

## Domaines de sécurité

### Chiffrement & Identité
- **[[TLS]]** — Chiffrement des communications (HTTPS, [[mTLS]])
- **[[Certificates]]** — Certificats X.509, CA, PKI
- **[[RBAC]]** — Contrôle d'accès basé sur les rôles

### Secrets & Accès
- **[[Secrets management]]** — HashiCorp [[Vault]], K8s [[Secrets]], rotation
- **[[Zero trust]]** — Ne jamais faire confiance, toujours vérifier

### Conteneurs & Images
- **[[Container security]]** — [[AppArmor]], [[Seccomp]], [[Namespaces]]
- **[[Image scanning]]** — Trivy, [[CVE detection]], [[Policy enforcement]]

### Tests de sécurité
- **[[Vulnerability scanning]]** — [[SAST]], [[DAST]], [[Dependency scanning]]
- **[[DevSecOps]]** — Shift left, [[Secure SDLC]], [[Security gates]]

## Modèle de menace (STRIDE)

| Menace | Description |
|--------|-------------|
| **S**poofing | Usurpation d'identité |
| **T**ampering | Altération de données |
| **R**epudiation | Déni d'action |
| **I**nformation Disclosure | Fuite de données |
| **D**enial of Service | Interruption de service |
| **E**levation of Privilege | Escalade de privilèges |

## Liens

- [[DevSecOps]]
- [[Secrets management]]
- [[TLS]]
- [[Certificates]]
- [[Container security]]
- [[Image scanning]]
- [[Vulnerability scanning]]
- [[RBAC]]
- [[Zero trust]]
