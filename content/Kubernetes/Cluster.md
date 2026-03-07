# Cluster

## Parent  
- [[Kubernetes]]  
  
## Enfants  
- [[Node]]  
- [[Control plane]]  
  
## Concepts liés  
- [[Node]]  
- [[Control plane]]  
- [[Pod]]  
- [[Overlay]]  
- [[VPC]]  
  
---  
  
## Définition  
  
Un **Cluster Kubernetes** est un ensemble de machines (physiques ou virtuelles) qui exécutent et gèrent des applications conteneurisées.  
  
Le cluster est composé de deux parties principales :  
  
- **Control Plane** → le cerveau qui gère l’état du cluster  
- **Nodes** → les machines qui exécutent les applications  
  
Le cluster permet de :  

- déployer des applications  
- gérer les conteneurs  
- répartir la charge  
- assurer la haute disponibilité  
  
---    
## Architecture  
  
Un cluster Kubernetes ressemble généralement à ceci :

```bash
Kubernetes Cluster  
│  
├── Control Plane  
│ ├── API Server  
│ ├── Scheduler  
│ ├── Controller Manager  
│ └── etcd  
│  
└── Nodes  
├── kubelet  
├── kube-proxy  
└── Pods
```

### Control Plane

Le **Control Plane** prend les décisions globales du cluster :

- planification des pods
- gestion de l’état du cluster
- orchestration des ressources

### Nodes

Les **Nodes** exécutent les workloads (pods).

Chaque node contient :

- kubelet
- container runtime
- kube-proxy

---
## Pourquoi c'est important

Le cluster est la **base de tout Kubernetes**.

Sans cluster :

- pas de déploiement
- pas de pods
- pas de réseau
- pas d’orchestration

Le cluster permet :

- scalabilité
- résilience
- automatisation
- gestion centralisée des applications

---
## Exemple

Exemple simple :  
  
Une application web déployée dans un cluster Kubernetes.

```bash
Cluster  
│  
├── Node 1  
│ ├── Pod : frontend  
│ └── Pod : backend  
│  
└── Node 2  
└── Pod : database
```

Si un node tombe en panne, Kubernetes peut recréer les pods sur un autre node.

---
## Exemple réel (Cloud)

Un cluster Kubernetes dans le cloud peut ressembler à :
```bash
AWS / GCP / Azure  
│  
└── Kubernetes Cluster  
├── Control Plane (géré par le cloud)  
└── Nodes  
├── VM 1  
├── VM 2  
└── VM 3
```

Services managés :

- EKS (AWS)
- GKE (Google)
- AKS (Azure)

---
## Commandes utiles

Lister les nodes du cluster :
```bash
kubectl get nodes
```

Voir les informations du cluster :
```bash
kubectl cluster-info
```

Voir les pods dans tous les namespaces :
```bash
kubectl get pods -A
```

---

