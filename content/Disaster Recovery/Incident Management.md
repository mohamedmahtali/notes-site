---
title: Incident Management
tags:
  - reliability
  - intermediate
---

# Incident Management

## Définition

L'incident management est le processus structuré de détection, réponse, résolution et apprentissage lors d'une interruption ou dégradation du service. L'objectif n'est pas juste de corriger — c'est de réduire le temps de résolution et d'éviter la récidive.

> [!tip] Incident ≠ Problème
> Un **incident** est un événement qui perturbe le service maintenant. Un **problème** est la cause racine qui génère des incidents répétés. L'incident management gère l'urgence ; le problem management traite la cause.

## Sévérités

| Sévérité | Définition | Exemple | Délai de réponse |
|----------|-----------|---------|-----------------|
| SEV-1 | Service down pour tous les utilisateurs | Base de données principale inaccessible | Immédiat |
| SEV-2 | Dégradation majeure ou impact partiel | Latence x10, 30% des requêtes en erreur | < 15 min |
| SEV-3 | Dégradation mineure, workaround disponible | Feature non critique cassée | < 2h |
| SEV-4 | Problème cosmétique ou futur risque | Alerte non critique qui s'accumule | Prochain sprint |

## Cycle de vie d'un incident

```
Détection          → Alerte Prometheus / Datadog / user report
     ↓
Triage             → Qualifier la sévérité, nommer un Incident Commander
     ↓
Mobilisation       → Alerter les bonnes équipes, ouvrir le war room
     ↓
Investigation      → Identifier la cause probable (logs, métriques, traces)
     ↓
Mitigation         → Corriger ou contourner pour rétablir le service
     ↓
Résolution         → Service stable, incident clos
     ↓
Post-mortem        → Analyser les causes, documenter les actions
```

## Rôles pendant un incident

| Rôle | Responsabilité |
|------|---------------|
| **Incident Commander (IC)** | Coordonne la réponse, prend les décisions, évite les silos |
| **Tech Lead** | Dirige l'investigation technique |
| **Communications** | Met à jour la [[Status]] page, informe les stakeholders |
| **Scribe** | Note la timeline, les actions prises, les décisions |

> [!note] Incident Commander
> L'IC ne résout pas l'incident lui-même — il coordonne. Il s'assure que tout le monde avance dans la même direction et que personne ne bloque.

## Checklist de réponse (SEV-1/SEV-2)

```markdown
## Déclenché à : HH:MM UTC

### Mobilisation
- [ ] Incident Commander nommé : @username
- [ ] Canal Slack/Teams dédié créé : #incident-YYYY-MM-DD
- [ ] Équipes concernées alertées
- [ ] Status page mise en "investigating"

### Investigation
- [ ] Impact utilisateur quantifié (% erreurs, latence, nb users)
- [ ] Graphe Grafana/Datadog partagé dans le canal
- [ ] Logs pertinents identifiés
- [ ] Hypothèse principale : ________________

### Mitigation
- [ ] Rollback possible ? Si oui, décision prise par IC
- [ ] Fix ou workaround appliqué à : HH:MM
- [ ] Service monitoré pendant 15 min post-fix

### Clôture
- [ ] Status page mise en "resolved"
- [ ] Post-mortem planifié dans les 48h
- [ ] Timeline complète documentée
```

## Communication pendant l'incident

```
Toutes les 30 min (SEV-1) ou 1h (SEV-2) :

"[Update - HH:MM UTC]
Statut : En cours d'investigation
Impact : [décrire l'impact utilisateur]
Avancement : [ce qu'on a trouvé, ce qu'on teste]
Prochaine update : HH:MM UTC"
```

## Outils courants

| Catégorie | Outils |
|-----------|--------|
| Alerting | PagerDuty, OpsGenie, VictorOps |
| Communication | Slack, Teams, Zoom war room |
| Status page | Statuspage.io, Cachet |
| Gestion incidents | Incident.io, FireHydrant, Jira |
| Post-mortems | Notion, Confluence, GitHub Issues |

## Liens

- [[Runbooks]]
- [[Incident response]]
- [[RTO RPO]]
- [[Disaster Recovery]]
