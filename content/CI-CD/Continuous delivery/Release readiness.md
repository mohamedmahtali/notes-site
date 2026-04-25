---
title: Release readiness
tags:
  - intermediate
---
# Release readiness

---

## Définition

La release readiness est l'ensemble des critères qu'un build doit satisfaire pour être considéré "prêt pour la production". Ces critères sont codifiés dans le [[Pipeline]] pour garantir qu'aucune étape n'est oubliée.

---

## Checklist automatisée

```yaml
readiness-check:
  runs-on: ubuntu-latest
  steps:
    - name: Check test coverage
      run: |
        COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
        [ "$COVERAGE" -ge 80 ] || (echo "Coverage below 80%" && exit 1)

    - name: Check no critical vulnerabilities
      run: trivy image --exit-code 1 --severity CRITICAL myapp:${{ github.sha }}

    - name: Staging smoke test
      run: |
        curl -sf https://staging.myapp.com/health | jq '.status == "ok"' | grep true

    - name: Check performance baseline
      run: |
        k6 run --out json=results.json performance/smoke.js
        jq '.metrics.http_req_duration.values.p95 < 500' results.json | grep true
```

---

## Métriques de readiness

| Métrique | Seuil recommandé |
|---|---|
| Couverture de tests | ≥ 80% |
| Vulnérabilités critiques | 0 |
| Temps de réponse p95 | < 500ms |
| Error rate [[Staging]] | < 0.1% |
| Build time | < 15 min |
