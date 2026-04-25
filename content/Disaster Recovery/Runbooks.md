---
title: Runbooks
tags:
  - reliability
  - intermediate
---

# Runbooks

## Définition

Un runbook est un document opérationnel qui décrit étape par étape comment effectuer une opération spécifique ou répondre à un incident. Il transforme l'expertise tacite en procédure documentée et reproductible.

> [!tip] Runbooks = capital organisationnel
> Un bon runbook permet à n'importe quel membre de l'équipe de résoudre un incident, même à 3h du matin, même si c'est la première fois qu'il voit ce problème. Il réduit le bus factor et le MTTR.

## Structure d'un runbook

```markdown
# Runbook : [Nom de l'incident]

## Sévérité : [P1/P2/P3]
## Équipe responsable : [SRE/Backend/Infra]
## Dernière mise à jour : [date]

## Symptômes
- Liste des symptômes observables
- Alertes Prometheus/Grafana déclenchées

## Diagnostic
1. Vérifier [X] → commande à exécuter
2. Si [condition] → aller à l'étape Y
3. Vérifier les logs : `kubectl logs -n prod ...`

## Remédiation
1. [Étape 1 avec commande exacte]
2. [Étape 2]
3. Vérifier la résolution : [commande]

## Escalade
- Si non résolu en 30min → appeler [contact]
- Si impact > 100 utilisateurs → prévenir [manager]

## Post-incident
- Créer un ticket pour l'analyse post-mortem
- Mettre à jour ce runbook si nécessaire
```

## Automatisation des runbooks

```bash
# Runbook as Code avec des scripts
#!/bin/bash
# runbook-high-memory.sh

echo "=== Diagnostic mémoire ==="
kubectl top pods -n production --sort-by=memory | head -10

echo "=== Pods OOMKilled récents ==="
kubectl get events -n production   --field-selector reason=OOMKilling   --sort-by=lastTimestamp | tail -5

echo "=== Action : restart du service si > 90% RAM ==="
# ... logique de remédiation automatique
```

## Liens

- [[Disaster Recovery]]
- [[Incident response]]
- [[Game days]]
