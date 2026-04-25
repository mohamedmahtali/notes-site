---
title: Mounted configuration
tags:
  - intermediate
---
# Mounted configuration

---

## Définition

Monter un ConfigMap comme volume crée des fichiers dans le container pour chaque clé du ConfigMap. Contrairement à l'injection d'environnement, les fichiers sont mis à jour automatiquement quand le ConfigMap change (avec un délai).

---

## Montage complet

```yaml
spec:
  containers:
  - name: nginx
    volumeMounts:
    - name: nginx-config
      mountPath: /etc/nginx/conf.d
      readOnly: true
  volumes:
  - name: nginx-config
    configMap:
      name: nginx-config
      # Chaque clé du ConfigMap crée un fichier dans /etc/nginx/conf.d/
```

---

## Clés spécifiques avec noms de fichiers personnalisés

```yaml
volumes:
- name: app-config
  configMap:
    name: app-config
    items:
    - key: config.yaml        # clé du ConfigMap
      path: app.yaml          # nom du fichier créé
    - key: logging.yaml
      path: logging.yaml
```

---

## Mise à jour automatique

```bash
# Modifier le ConfigMap
kubectl edit configmap nginx-config
# ou
kubectl apply -f updated-configmap.yaml

# Les fichiers dans le pod sont mis à jour après ~1 minute (kubelet sync)
# L'application doit détecter et recharger les fichiers (SIGHUP, fsnotify...)

# Vérifier dans le pod
kubectl exec -it nginx-pod -- cat /etc/nginx/conf.d/default.conf
```

---

> [!tip]
> [[Nginx]] se recharge sur [[SIGHUP]]. Configurer un sidecar qui surveille les changements de fichiers et envoie SIGHUP au container principal — c'est le pattern "configmap reload".
