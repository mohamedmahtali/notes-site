---
title: Manual approval
tags:
  - intermediate
---
# Manual approval

## Parent
- [[Continuous delivery]]

---

## Définition

L'approbation manuelle est une étape humaine dans le pipeline CD qui bloque le déploiement en production jusqu'à validation explicite d'un reviewer désigné. Elle permet de contrôler le moment du déploiement sans compromettre l'automatisation.

---

## Pourquoi c'est important

> [!note] Contrôle humain sur les risques
> Même avec un pipeline entièrement automatisé, certains déploiements nécessitent un regard humain : releases majeures, changements de schéma DB, déploiements en période de fort trafic. L'approbation manuelle est ce contrôle.

---

## GitHub Actions — Environment protection

```yaml
# Settings → Environments → production → Required reviewers
# (configurer dans l'UI GitHub)

deploy-production:
  needs: deploy-staging
  runs-on: ubuntu-latest
  environment:
    name: production     # bloque ici si des reviewers sont requis
  steps:
    - name: Deploy
      run: ./deploy.sh production
```

---

## GitLab CI — Manual job

```yaml
deploy:production:
  stage: deploy
  script:
    - ./deploy.sh production
  when: manual          # requiert un clic dans l'UI GitLab
  environment:
    name: production
  only:
    - main
```

---

> [!tip]
> Limiter les approbateurs à une liste restreinte (lead devs, SRE). Trop d'approbateurs = goulot d'étranglement. Trop peu = indisponibilité si la personne est absente. 2-3 personnes est optimal.
