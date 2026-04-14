---
title: DNS Glossaire
tags:
  - beginner
---

# DNS Glossaire

## Parent
- [[DNS]]

---

## Termes essentiels

| Terme | Définition |
|---|---|
| **Zone** | Portion de l'espace de noms DNS sous la responsabilité d'un serveur |
| **Authoritative server** | Serveur faisant autorité sur une zone (source de vérité) |
| **Recursive resolver** | Serveur qui interroge en cascade pour trouver la réponse |
| **Root servers** | 13 serveurs racines (. ) gérant les TLDs |
| **TLD** | Top Level Domain (.com, .org, .fr) |
| **FQDN** | Fully Qualified Domain Name : `www.example.com.` (avec le point final) |
| **Forward lookup** | Nom → IP |
| **Reverse lookup** | IP → Nom (via PTR records) |
| **Delegation** | Confier une sous-zone à d'autres serveurs NS |
| **Zone transfer** | Synchronisation entre serveurs DNS primaire/secondaire |
| **Negative caching** | Mise en cache des réponses "non trouvé" (NXDOMAIN) |
| **Split DNS** | Réponses différentes selon la source de la requête (interne/externe) |
| **DNSSEC** | Extension qui signe cryptographiquement les réponses DNS |
