# Node

## Parent
- [[Cluster]]

## Enfants
- [[kubelet]]
- [[kube-proxy]]
- [[Container runtime]]
- [[Node labels]]

## Concepts liés
- [[kubelet]]
- [[kube-proxy]]
- [[Container runtime]]
- [[Node labels]]
- [[DaemonSets]]

---  
  
## Définition  
  
Un **Node** est une machine (physique ou virtuelle) dans un **Cluster Kubernetes** qui exécute les applications conteneurisées.  
  
Les Nodes sont les **machines de travail du cluster**.  
Ils exécutent les **Pods** qui contiennent les containers des applications.  
  
Un cluster Kubernetes peut contenir **plusieurs nodes**, permettant :  
  
- la scalabilité  
- la répartition de charge  
- la tolérance aux pannes  
  
Chaque Node est géré par le **Control Plane** du cluster.  
  
---  
  
## Architecture d'un Node  
  
Un Node contient plusieurs composants essentiels :

```bash
Node  
│  
├── kubelet  
├── kube-proxy  
├── container runtime  
└── Pods
```

### kubelet

Le **kubelet** est un agent qui tourne sur chaque node.

Son rôle :

- communiquer avec le Control Plane
- s'assurer que les pods sont en fonctionnement
- gérer le cycle de vie des containers

---

### container runtime

Le **container runtime** est le logiciel qui exécute les containers.

Exemples :

- containerd
- CRI-O
- Docker (anciennement)

Il est responsable de :

- lancer les containers
- arrêter les containers
- gérer les images

---

### kube-proxy

Le **kube-proxy** gère le **réseau des services Kubernetes**.

Il permet :

- la communication entre pods
- le routage vers les services
- la gestion des règles réseau

---

## Pourquoi c'est important

Les Nodes sont les **machines qui exécutent réellement les applications**.

Sans nodes :

- aucun pod ne peut s'exécuter
- aucune application ne peut fonctionner

Les nodes permettent :

- la **distribution des workloads**
- la **haute disponibilité**
- la **scalabilité horizontale**

Si un node tombe en panne, Kubernetes peut **recréer les pods sur un autre node**.

---

## Exemple

Un cluster avec trois nodes :
```bash
Cluster  
│  
├── Node 1  
│ ├── Pod : frontend  
│ └── Pod : backend  
│  
├── Node 2  
│ └── Pod : API  
│  
└── Node 3  
└── Pod : database
```

Le scheduler Kubernetes décide **sur quel node chaque pod doit être exécuté**.

---

## Commandes utiles

Lister les nodes du cluster :
```bash
kubectl get nodes
```

Voir les détails d'un node :
```bash
kubectl describe node <nom-du-node>
```

Voir l'utilisation des ressources :
```bash
kubectl top nodes
```


