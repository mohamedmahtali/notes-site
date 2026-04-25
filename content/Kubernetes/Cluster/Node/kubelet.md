---
title: kubelet
tags:
  - advanced
---
# kubelet

---

## Définition

Le kubelet est l'agent [[Kubernetes]] qui tourne sur chaque [[Node]] worker. Il reçoit les PodSpecs de l'[[API server]] et s'assure que les [[Containers]] décrits tournent et sont en bonne santé. C'est lui qui parle au [[Container runtime]] ([[containerd]]/CRI-O).

---

## Responsabilités

```
API server → PodSpec assigné au node
    ↓
kubelet
    ├── Demande au container runtime de démarrer les containers
    ├── Monte les volumes (PVC, ConfigMaps, Secrets)
    ├── Exécute les liveness/readiness/startup probes
    ├── Rapporte l'état du pod à l'API server
    └── Gère les logs des containers
```

---

## Configuration

```bash
# Statut du kubelet
systemctl status kubelet
journalctl -u kubelet -f

# Configuration (kubeadm)
cat /var/lib/kubelet/config.yaml
cat /etc/kubernetes/kubelet.conf

# Voir les pods que le kubelet gère
# (les static pods sont dans /etc/kubernetes/manifests/)
ls /etc/kubernetes/manifests/
```

---

## Probes

```yaml
spec:
  containers:
  - livenessProbe:       # kubelet redémarre si échec
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 30
      periodSeconds: 10
    readinessProbe:      # retire du load balancer si échec
      httpGet:
        path: /ready
        port: 8080
```

---

> [!tip]
> Les static [[Pods]] (dans `/etc/kubernetes/manifests/`) sont gérés directement par le kubelet sans passer par l'API server — c'est comme ça que les composants du [[Control plane]] (apiserver, [[etcd]]) sont démarrés.
