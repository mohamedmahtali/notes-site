---
title: Automated tests
tags:
  - intermediate
---
# Automated tests

---

## Définition

Les automated tests s'exécutent à chaque [[Commit]] dans le [[Pipeline]] CI pour valider le comportement du code. Ils couvrent plusieurs niveaux : unit, intégration, et end-to-end — chacun avec un ratio coût/valeur différent.

---

## Pyramide de tests

```
        /       /e2e\        Lents, coûteux, peu nombreux
      /______     /integr. \     Moyens — valident les interfaces
    /___________   /  unit tests  \ Rapides, abondants, isolés
  /_________________```

---

## Configuration recommandée

```yaml
test:
  runs-on: ubuntu-latest
  strategy:
    matrix:
      [[Node]]-version: ['18', '20', '22']   # tester sur plusieurs versions

  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}

    - run: npm ci
    - run: npm run test:unit -- --coverage
    - run: npm run test:integration

    - name: Coverage report
      uses: codecov/codecov-action@v4
```

---

> [!warning]
> Ne pas mettre les tests e2e dans le CI de chaque PR — trop lents. Les lancer sur merge vers main ou en nightly build.
