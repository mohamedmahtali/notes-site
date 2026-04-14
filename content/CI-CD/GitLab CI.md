---
title: GitLab CI
tags:
  - intermediate
---
# GitLab CI

## Parent
- [[CI-CD]]

## Enfants
- [[.gitlab-ci.yml]]
- [[Stages]]
- [[Jobs]]
- [[Runners]]

---

## Définition

GitLab CI/CD est la plateforme intégrée dans GitLab pour l'intégration et le déploiement continus. Les pipelines sont définis dans `.gitlab-ci.yml` à la racine du repo. GitLab CI est particulièrement puissant pour les environnements self-hosted avec GitLab Community Edition.

---

## Pourquoi c'est important

> [!tip] Tout dans une seule plateforme
> GitLab intègre le code, les issues, les pipelines, le registry Docker, les environnements, et le monitoring dans une seule interface. Pas besoin de GitHub + Jenkins + registry séparés.

---

## Exemple `.gitlab-ci.yml`

```yaml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE

test:
  stage: test
  script:
    - docker run $DOCKER_IMAGE npm test
  coverage: '/Lines\s*:\s*(\d+\.?\d*)%/'

deploy:staging:
  stage: deploy
  script:
    - kubectl set image deployment/app app=$DOCKER_IMAGE
  environment:
    name: staging
    url: https://staging.myapp.com
  only:
    - main
```

---

## Variables prédéfinies utiles

```bash
$CI_COMMIT_SHA          # SHA du commit
$CI_COMMIT_REF_NAME     # nom de la branche/tag
$CI_REGISTRY_IMAGE      # URL du registry GitLab
$CI_PROJECT_PATH        # namespace/projet
$CI_ENVIRONMENT_NAME    # nom de l'environnement
```

---

> [!note]
> Voir [[.gitlab-ci.yml]], [[Stages]], [[Jobs]] pour les détails de configuration.
