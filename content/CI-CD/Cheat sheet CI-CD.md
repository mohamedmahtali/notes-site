---
title: Cheat sheet CI/CD
tags:
  - ci-cd
  - beginner
---

# Cheat sheet CI/CD

## GitHub Actions — Structure

```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  IMAGE: ghcr.io/org/myapp

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm test
      - run: npm run build
```

## GitHub Actions — Patterns courants

```yaml
# Cache des dépendances
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}

# Build + push image Docker
- uses: docker/build-push-action@v5
  with:
    push: true
    tags: ${{ env.IMAGE }}:${{ github.sha }}

# Utiliser un secret
- run: ./deploy.sh
  env:
    API_KEY: ${{ secrets.API_KEY }}

# Condition d'exécution
- run: ./deploy.sh
  if: github.ref == 'refs/heads/main'

# Artifacts
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
```

## GitLab CI — Structure

```yaml
stages:
  - build
  - test
  - deploy

variables:
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  script:
    - docker build -t $IMAGE .
    - docker push $IMAGE

test:
  stage: test
  script:
    - npm ci && npm test

deploy:
  stage: deploy
  script:
    - ./deploy.sh
  environment:
    name: production
  only:
    - main
```

## GitLab CI — Patterns courants

```yaml
# Cache
cache:
  key: $CI_COMMIT_REF_SLUG
  paths:
    - node_modules/

# Artifacts
artifacts:
  paths:
    - dist/
  expire_in: 1 week
  reports:
    junit: test-results.xml

# Règles conditionnelles
rules:
  - if: $CI_COMMIT_BRANCH == "main"
    when: on_success
  - when: never

# Déclencheur manuel
deploy_prod:
  when: manual
```

## Jenkins — Pipeline Declarative

```groovy
pipeline {
  agent any
  stages {
    stage('Build') {
      steps { sh 'npm ci && npm run build' }
    }
    stage('Test') {
      steps { sh 'npm test' }
    }
    stage('Deploy') {
      when { branch 'main' }
      steps { sh './deploy.sh' }
    }
  }
  post {
    failure {
      slackSend message: "Build failed: ${env.JOB_NAME}"
    }
  }
}
```

## Liens

- [[CI-CD]]
- [[GitHub actions]]
- [[GitLab CI]]
- [[Jenkins]]
- [[Pipeline]]
