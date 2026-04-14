---
title: Jobs
tags:
  - intermediate
---
# Jobs

## Parent
- [[GitLab CI]]

---

## Définition

Un job GitLab CI est l'unité d'exécution atomique : un script qui tourne sur un runner dans un stage donné. Chaque job a son environnement isolé (conteneur Docker ou VM).

---

## Anatomie d'un job

```yaml
mon-job:
  stage: test
  image: python:3.12-slim      # image Docker du conteneur
  services:                     # conteneurs annexes (DB, Redis)
    - postgres:15
  variables:                    # variables spécifiques au job
    DATABASE_URL: postgresql://postgres:test@postgres/testdb
  before_script:                # exécuté avant script
    - pip install -r requirements.txt
  script:                       # commandes principales
    - pytest tests/ --cov=src
  after_script:                 # toujours exécuté (même si échec)
    - echo "Job finished"
  artifacts:                    # fichiers à conserver après le job
    reports:
      junit: test-results.xml
    paths:
      - coverage/
    expire_in: 1 week
  rules:                        # conditions d'exécution
    - if: $CI_PIPELINE_SOURCE == "push"
  retry:                        # retry en cas d'échec
    max: 2
    when:
      - runner_system_failure
```

---

## Jobs parallèles

```yaml
test:matrix:
  stage: test
  parallel:
    matrix:
      - PYTHON_VERSION: ['3.10', '3.11', '3.12']
  image: python:${PYTHON_VERSION}
  script: pytest
```
