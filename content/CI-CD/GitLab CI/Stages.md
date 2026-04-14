---
title: Stages
tags:
  - intermediate
---
# Stages

## Parent
- [[GitLab CI]]

---

## Définition

Les stages dans GitLab CI définissent l'ordre d'exécution des jobs. Tous les jobs d'un même stage tournent en parallèle. Le stage suivant ne commence que si tous les jobs du stage précédent ont réussi.

---

## Configuration

```yaml
stages:
  - build      # 1er — tous les jobs "build" en parallèle
  - test       # 2ème — attend que build réussisse
  - scan       # 3ème
  - deploy     # dernier

build:image:
  stage: build
  script: docker build .

test:unit:
  stage: test        # attend build
  script: npm test

test:lint:
  stage: test        # parallèle avec test:unit
  script: npm run lint

scan:trivy:
  stage: scan        # attend que test ET lint réussissent
  script: trivy image myimage:latest

deploy:staging:
  stage: deploy
  script: ./deploy.sh staging
```

---

## Stages conditionnels

```yaml
deploy:production:
  stage: deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"   # seulement sur main
      when: manual                        # déclenchement manuel
    - when: never                         # sinon jamais
```

---

> [!tip]
> Garder les stages courts et focalisés. Plus les stages sont rapides, plus le feedback est rapide. Viser < 5 min pour le stage test.
