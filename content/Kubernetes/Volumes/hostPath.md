---
title: hostPath
tags:
  - intermediate
---
# hostPath

## Parent
- [[Volumes]]

---

## Définition

`hostPath` monte un fichier ou répertoire du système de fichiers du node hôte dans le pod. Donne accès direct au node — utile pour les agents système mais dangereux pour les applications ordinaires.

---

## Cas d'usage légitimes

- DaemonSets d'agents (logs, métriques) qui lisent `/var/log` ou `/proc`
- Accès au socket Docker `/var/run/docker.sock`
- Stockage local haute performance (avec node affinity)

---

## Manifeste

```yaml
spec:
  containers:
  - name: log-agent
    volumeMounts:
    - name: varlog
      mountPath: /host/var/log
      readOnly: true
    - name: docker-socket
      mountPath: /var/run/docker.sock

  volumes:
  - name: varlog
    hostPath:
      path: /var/log
      type: Directory

  - name: docker-socket
    hostPath:
      path: /var/run/docker.sock
      type: Socket
```

---

## Types hostPath

| Type | Description |
|---|---|
| `Directory` | Le répertoire doit exister |
| `DirectoryOrCreate` | Crée le répertoire si absent |
| `File` | Le fichier doit exister |
| `Socket` | Le socket Unix doit exister |

---

> [!warning]
> `hostPath` avec accès en écriture est un risque de sécurité majeur. Un pod malveillant peut modifier des fichiers système du node. Éviter en production sauf pour des cas justifiés (DaemonSets d'observabilité).
