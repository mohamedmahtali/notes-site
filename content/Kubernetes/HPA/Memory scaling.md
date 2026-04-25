---
title: Memory scaling
tags:
  - intermediate
---
# Memory scaling

---

## Définition

Le memory scaling avec [[HPA]] ajuste le nombre de [[Pods]] en fonction de l'utilisation mémoire. Moins courant que le [[CPU scaling]] car la mémoire est moins élastique — les pods ne libèrent pas facilement la mémoire.

---

## Configuration

```yaml
metrics:
- type: Resource
  resource:
    name: memory
    target:
      type: Utilization
      averageUtilization: 80    # 80% du memory request en moyenne
      # ou en valeur absolue :
      # type: AverageValue
      # averageValue: 200Mi
```

---

## Limites du memory scaling

> [!warning] La mémoire ne se libère pas spontanément
> Contrairement au CPU (qui diminue quand le pic passe), la mémoire peut rester haute même après le pic — le GC Java/Go ne libère pas immédiatement. Scaler sur la mémoire peut créer des oscillations.
> Préférer scaler sur le CPU ou des métriques applicatives custom.

---

## Utilisation combinée

```yaml
spec:
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  # HPA scale si l'une OU l'autre des métriques dépasse le seuil
```
