---
title: Integration tests
tags:
  - intermediate
---
# Integration tests

---

## Définition

Les tests d'intégration vérifient que plusieurs composants fonctionnent correctement ensemble : application + base de données, API + service tiers, microservices entre eux. Plus lents que les [[Unit tests]], ils détectent les problèmes d'interface.

---

## Services Docker en CI

```yaml
# GitHub Actions avec services
test-integration:
  runs-on: ubuntu-latest
  services:
    postgres:
      image: postgres:15
      env:
        POSTGRES_DB: testdb
        POSTGRES_PASSWORD: test
      options: >-
        --health-cmd pg_isready
        --health-interval 10s
    redis:
      image: redis:7
      options: --health-cmd "redis-cli ping"

  steps:
    - uses: actions/checkout@v4
    - name: Run integration tests
      run: pytest tests/integration/ -v
      env:
        DATABASE_URL: postgresql://postgres:test@localhost/testdb
        REDIS_URL: redis://localhost:6379
```

---

## Docker Compose en CI

```yaml
- name: Start services
  run: docker compose -f docker-compose.test.yml up -d

- name: Wait for services
  run: docker compose -f docker-compose.test.yml run --rm wait

- name: Run tests
  run: docker compose -f docker-compose.test.yml run --rm app pytest
```

---

> [!note]
> Les tests d'intégration doivent utiliser une base de données de test isolée, jamais de données de production.
