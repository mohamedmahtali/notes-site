---
title: Test stage
tags:
  - intermediate
---
# Test stage

---

## Définition

Le test stage exécute l'ensemble des suites de tests automatisés pour valider que le code fonctionne correctement avant tout déploiement. C'est le principal filet de sécurité du [[Pipeline]] CI/CD.

---

## Pourquoi c'est important

> [!warning] Sans tests automatisés, pas de CI/CD
> Le test stage est ce qui distingue le CI/CD du simple déploiement automatisé. Sans tests, on automatise le déploiement de bugs. Viser au minimum : [[Unit tests]] + smoke test en [[Staging]].

---

## Stratégie de tests en pipeline

```
Stage 1 (rapide, <2min) :  lint + type check + unit tests
Stage 2 (moyen, <10min) :  integration tests
Stage 3 (lent, <30min) :   e2e tests + security scan
```

---

## Exemple complet

```yaml
test:
  runs-on: ubuntu-latest
  services:
    postgres:
      image: postgres:15
      env:
        POSTGRES_PASSWORD: test
  steps:
    - uses: actions/checkout@v4
    - name: Unit tests
      run: npm run test:unit -- --coverage
    - name: Integration tests
      run: npm run test:integration
      env:
        DATABASE_URL: postgresql://postgres:test@localhost/testdb
    - name: Upload coverage
      uses: codecov/codecov-action@v4
```

---

> [!tip]
> Toujours lancer les tests les plus rapides en premier (fail fast). Paralléliser les suites longues avec `matrix` dans [[GitHub actions]] ou `parallel` dans GitLab CI.
