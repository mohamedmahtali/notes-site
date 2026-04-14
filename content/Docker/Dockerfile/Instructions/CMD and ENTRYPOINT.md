---
title: CMD and ENTRYPOINT
tags:
  - intermediate
---

# CMD and ENTRYPOINT

## Parent
- [[Instructions]]

---

## Définition

`CMD` et `ENTRYPOINT` définissent la commande exécutée au démarrage d'un conteneur. Ils se complètent : `ENTRYPOINT` est le binaire principal (fixe), `CMD` sont les arguments par défaut (overridables).

---

## CMD

```dockerfile
# Shell form
CMD npm start

# Exec form (recommandée)
CMD ["node", "server.js"]
CMD ["python", "-m", "uvicorn", "main:app"]
```

`CMD` peut être complètement remplacé au `docker run` :
```bash
docker run mon-app bash   # remplace CMD par "bash"
```

---

## ENTRYPOINT

```dockerfile
ENTRYPOINT ["docker-entrypoint.sh"]
ENTRYPOINT ["nginx", "-g", "daemon off;"]
```

`ENTRYPOINT` n'est pas remplacé par les arguments de `docker run` — il les reçoit comme paramètres.

---

## Combinaison ENTRYPOINT + CMD

```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--port", "8000"]   # arguments par défaut
```

```bash
docker run mon-app                      # → python app.py --port 8000
docker run mon-app --port 9000          # → python app.py --port 9000
docker run --entrypoint bash mon-app    # override ENTRYPOINT
```

---

## Résumé

| | Remplacé par `docker run args` | Remplacé par `--entrypoint` |
|---|---|---|
| `CMD` | ✅ Oui | ✅ Oui |
| `ENTRYPOINT` | ❌ Non (reçoit en args) | ✅ Oui |

> [!tip]
> Utilise `ENTRYPOINT` pour les binaires principaux d'un outil CLI, `CMD` pour les serveurs ou commandes avec arguments par défaut.
