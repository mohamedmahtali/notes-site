---
title: Health checks
tags:
  - beginner
---
# Health checks

## Parent
- [[Load balancers]]

---

## Définition

Les health checks sont des vérifications périodiques effectuées par le load balancer vers chaque instance backend. Si une instance échoue le health check, elle est retirée de la rotation jusqu'à ce qu'elle redevienne saine.

---

## Pourquoi c'est important

> [!tip] Tolérance aux pannes automatique
> Sans health checks, le LB continue d'envoyer du trafic vers des instances tombées ou qui démarrent encore. Les health checks garantissent que le trafic n'est envoyé qu'aux instances vraiment disponibles.

---

## Configuration AWS ALB

```bash
aws elbv2 modify-target-group   --target-group-arn arn:aws:...   --health-check-protocol HTTP   --health-check-port 8080   --health-check-path /health   --health-check-interval-seconds 30   --health-check-timeout-seconds 5   --healthy-threshold-count 2 \    # 2 succès → healthy
  --unhealthy-threshold-count 3    # 3 échecs → unhealthy
```

---

## Endpoint de health check

```python
# FastAPI
@app.get("/health")
async def health():
    # Vérifier DB, dependencies
    try:
        await db.ping()
        return {"status": "ok", "timestamp": datetime.utcnow()}
    except Exception:
        raise HTTPException(status_code=503, detail="DB unavailable")
```

---

> [!tip]
> Le health check endpoint doit vérifier les dépendances critiques (DB, cache). Un 200 qui ne vérifie rien donne une fausse sensation de sécurité — l'app peut être "healthy" mais incapable de traiter les requêtes.
