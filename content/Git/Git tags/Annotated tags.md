---
title: Annotated tags
tags:
  - intermediate
---

# Annotated tags

---

## Définition

Un tag annoté (`git tag -a`) est un objet [[Git]] complet qui stocke : le nom du tag, la date, le tagger, un message, et peut être signé GPG. C'est le type recommandé pour les [[Releases]] officielles.

---

## Commandes

```bash
# Créer un tag annoté
git tag -a v1.2.0 -m "Release v1.2.0 – ajout authentification JWT"

# Tagger un commit spécifique
git tag -a v1.1.3 abc1234 -m "Hotfix: correction timeout API"

# Voir les détails d'un tag annoté
git show v1.2.0

# Lister tous les tags
git tag -l

# Pousser un tag vers le remote
git push origin v1.2.0

# Pousser tous les tags
git push origin --tags
```

---

## Anatomie d'un tag annoté

```
tag v1.2.0
Tagger: Mohamed Mahtali <m@example.com>
Date:   Mon Jan 15 14:32:00 2024

Release v1.2.0 – ajout authentification JWT

commit a3f2c1e...
```

---

## Annotated vs Lightweight

| Critère | Annotated | Lightweight |
|---|---|---|
| Objet Git | Oui (hash propre) | Non (alias de [[Commit]]) |
| Message | Oui | Non |
| Date du tag | Oui | Date du commit |
| Signature GPG | Possible | Non |
| Recommandé pour | Releases | Marquages temporaires |

> [!tip]
> Utilise les tags annotés pour toutes les releases publiées. La commande `git describe` s'appuie sur eux pour générer des versions automatiques.
