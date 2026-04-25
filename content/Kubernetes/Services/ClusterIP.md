---
title: ClusterIP
tags:
  - beginner
---
# ClusterIP

---

## Définition

ClusterIP est le type de Service par défaut. Il [[EXPOSE]] le service sur une IP interne au [[Cluster]] uniquement — inaccessible depuis l'extérieur. C'est le type à utiliser pour la communication entre microservices à l'intérieur du cluster.

---

## Manifeste

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  type: ClusterIP      # défaut — peut être omis
  selector:
    app: api
  ports:
  - name: http
    port: 80
    targetPort: 8080
  - name: grpc
    port: 9090
    targetPort: 9090
```

---

## DNS automatique

```bash
# Dans le cluster, le service est accessible via DNS :
http://api-service                              # même namespace
http://api-service.production                   # namespace différent
http://api-service.production.svc.cluster.local # FQDN complet
```

---

## Service headless (ClusterIP: None)

```yaml
spec:
  clusterIP: None     # headless — pas d'IP virtuelle
  selector:
    app: postgres
```

```bash
# Le DNS renvoie directement les IPs des pods
nslookup postgres.default.svc.cluster.local
# → 10.244.1.5 (pod-0)
# → 10.244.2.3 (pod-1)
# Utilisé avec StatefulSets pour le DNS stable par pod
```
