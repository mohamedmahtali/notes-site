---
title: Unit tests
tags:
  - beginner
---
# Unit tests

---

## Définition

Les unit tests testent des fonctions ou méthodes isolées, sans dépendances externes (DB, réseau, système de fichiers). Rapides (millisecondes), déterministes, et abondants — ils constituent la base de la pyramide de tests.

---

## En pipeline CI

```yaml
- name: Run unit tests
  run: |
    # Python
    pytest tests/unit/ -v --cov=src --cov-report=xml

    # Node.js
    npm run test:unit -- --coverage --ci

    # Go
    go test ./... -short -race -coverprofile=coverage.out

    # Java
    mvn test -Dtest="*Unit*"
```

---

## Règles des bons unit tests

```python
# Test unitaire correct — isolé, déterministe, rapide
def test_calculate_discount():
    assert calculate_discount(100, 0.1) == 90
    assert calculate_discount(0, 0.5) == 0
    assert calculate_discount(100, 0) == 100

# Anti-pattern — dépend d'une DB (c'est un test d'intégration)
def test_get_user_from_db():
    user = User.query.get(1)  # NE PAS faire ça en unit test
```

---

> [!tip]
> Viser 70-80% de couverture sur le code métier. La couverture à 100% est illusoire et coûteuse — prioriser les chemins critiques.
