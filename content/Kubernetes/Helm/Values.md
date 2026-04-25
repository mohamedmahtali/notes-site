---
title: Values
tags:
  - intermediate
---
# Values

---

## Définition

Les values sont les paramètres configurables d'un chart [[Helm]]. Définies dans `values.yaml` avec des valeurs par défaut, elles peuvent être surchargées à l'installation pour adapter le déploiement à chaque environnement.

---

## values.yaml (défauts)

```yaml
# values.yaml
replicaCount: 1

image:
  repository: myapp
  tag: "1.0.0"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false
  hostname: myapp.example.com

resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi

postgresql:
  enabled: true
  auth:
    database: myapp
    username: myapp
```

---

## Surcharge des valeurs

```bash
# En ligne (simple)
helm install myapp ./chart   --set replicaCount=3   --set image.tag=2.0.0

# Fichier de values spécifique env
helm install myapp ./chart -f values.prod.yaml

# Combiner (prod-values.yaml surcharge values.yaml)
helm install myapp ./chart   -f values.yaml   -f values.prod.yaml
```

---

## Validation des values

```yaml
# values.schema.json — valide les valeurs fournies
{
  "type": "object",
  "properties": {
    "replicaCount": {
      "type": "integer",
      "minimum": 1
    }
  }
}
```

---

> [!tip]
> Garder un fichier `values.yaml` avec les défauts sensibles, et des fichiers `values.staging.yaml`, `values.production.yaml` pour les overrides spécifiques. Ne jamais hardcoder les [[Secrets]] — utiliser des references à des Secrets K8s ou un [[Vault]].
