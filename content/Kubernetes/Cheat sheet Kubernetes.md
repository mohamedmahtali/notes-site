---
title: Cheat sheet Kubernetes
tags:
  - kubernetes
  - beginner
---

# Cheat sheet Kubernetes

## kubectl — Basics

```bash
kubectl version                          # Version client/serveur
kubectl cluster-info                     # Info cluster
kubectl config get-contexts              # Contextes disponibles
kubectl config use-context prod          # Changer de contexte
kubectl config set-context --current --namespace=dev  # Namespace par défaut
kubectl api-resources                    # Toutes les ressources
```

## Get & describe

```bash
kubectl get pods                         # Pods du namespace courant
kubectl get pods -A                      # Tous namespaces
kubectl get pods -o wide                 # + node, IP
kubectl get pods -l app=nginx            # Filtrer par label
kubectl get all -n production            # Tout dans un namespace
kubectl describe pod mypod               # Détails complets
kubectl describe node mynode             # Infos node
kubectl get events --sort-by=.lastTimestamp  # Événements récents
```

## Pods & conteneurs

```bash
kubectl logs mypod                       # Logs
kubectl logs mypod -c mycontainer        # Logs d'un conteneur spécifique
kubectl logs -f mypod                    # Suivre en temps réel
kubectl logs --previous mypod            # Logs du conteneur précédent
kubectl exec -it mypod -- bash           # Shell interactif
kubectl exec mypod -- ls /etc            # Commande ponctuelle
kubectl cp mypod:/tmp/file ./file        # Copier depuis pod
kubectl cp ./file mypod:/tmp/file        # Copier vers pod
kubectl port-forward pod/mypod 8080:80   # Tunnel local
```

## Apply & delete

```bash
kubectl apply -f manifest.yaml           # Appliquer (create ou update)
kubectl apply -f ./k8s/                  # Répertoire entier
kubectl delete -f manifest.yaml          # Supprimer via fichier
kubectl delete pod mypod                 # Supprimer un pod
kubectl delete pod mypod --force         # Forcer (ignore graceful)
kubectl delete all -l app=nginx          # Supprimer par label
```

## Deployments

```bash
kubectl rollout status deployment/myapp  # Statut du déploiement
kubectl rollout history deployment/myapp # Historique
kubectl rollout undo deployment/myapp    # Rollback
kubectl scale deployment myapp --replicas=5  # Scaler
kubectl set image deployment/myapp app=myapp:2.0  # Changer image
kubectl restart deployment myapp         # Redémarrer les pods
```

## Namespaces

```bash
kubectl get namespaces
kubectl create namespace dev
kubectl delete namespace dev
kubectl get pods -n dev
```

## Secrets & ConfigMaps

```bash
kubectl create secret generic mysecret --from-literal=key=value
kubectl create secret generic mysecret --from-file=./secret.txt
kubectl create configmap myconfig --from-literal=key=value
kubectl get secret mysecret -o jsonpath='{.data.key}' | base64 -d
```

## Debugging

```bash
kubectl get pod mypod -o yaml            # Manifest complet
kubectl run debug --image=busybox -it --rm -- sh  # Pod debug temporaire
kubectl auth can-i create pods           # Vérifier permissions
kubectl top pods                         # Utilisation CPU/RAM (metrics-server requis)
kubectl top nodes
```

## Liens

- [[Kubernetes]]
- [[kubectl]]
- [[Pods]]
- [[Deployments]]
- [[Services]]
