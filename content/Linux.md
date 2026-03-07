# Linux

## Parent
- [[DevOps]]

## Enfants
- [[Shell]]
- [[Filesystem]]
- [[Process]]
- [[Permissions]]
- [[Package Manager]]
- [[Systemd]]
- [[Networking]]

---

## Concepts liés
- [[DevOps]]
- [[Docker]]
- [[Kubernetes]]
- [[Cloud]]

---

## Définition

**Linux** est un **système d’exploitation open source basé sur Unix** utilisé pour faire fonctionner des serveurs, des infrastructures cloud et la majorité des plateformes DevOps modernes.

Il est composé de deux éléments principaux :

- **le kernel (noyau)** : qui gère le matériel (CPU, mémoire, disque, réseau)
- **les outils système** : commandes et programmes permettant d’utiliser le système

Linux est aujourd’hui **le système dominant dans l’infrastructure moderne** :

- la majorité des serveurs internet
- les plateformes cloud
- les conteneurs Docker
- les clusters Kubernetes

fonctionnent sur Linux.

---

## Pourquoi c'est important

### 1. Base de toute l’infrastructure DevOps

La plupart des outils DevOps tournent sur Linux :

- Docker
- Kubernetes
- Terraform
- Git
- les serveurs web

Comprendre Linux est donc **indispensable pour travailler avec ces technologies**.

---

### 2. Automatisation et scripting

Linux permet d’automatiser des tâches grâce :

- au **shell**
- aux **scripts bash**
- aux **cron jobs**

Exemple :

```bash
#!/bin/bash
docker build -t myapp .
docker push registry/myapp
```

### 3. Contrôle complet du système

Linux permet de contrôler précisément :

- les processus    
- la mémoire
- le réseau
- les fichiers
- les permissions

Ce contrôle est essentiel pour :

- le debugging
- l'optimisation
- la sécurité.

### 3. Contrôle complet du système

Linux permet de contrôler précisément :

- les processus
- la mémoire
- le réseau
- les fichiers
- les permissions

Ce contrôle est essentiel pour :

- le debugging
- l'optimisation
- la sécurité.

---

### 4. Environnement standard de production

Dans le monde DevOps, les environnements de production sont presque toujours :

- Ubuntu Server
- Debian
- Red Hat
- Rocky Linux
- Amazon Linux

Apprendre Linux signifie comprendre **comment fonctionne réellement un serveur**.

---

## Exemple concret

Un développeur pousse son code sur Git.

Le pipeline CI/CD :

1. lance une **machine Linux**
2. installe les dépendances
3. construit une image **Docker**
4. déploie l'application sur **Kubernetes**

Tout cela se passe **sur des systèmes Linux**.

---

## Commandes Linux fondamentales

| Commande | Utilité                        |
| -------- | ------------------------------ |
| `ls`     | lister les fichiers            |
| `cd`     | changer de dossier             |
| `pwd`    | afficher le dossier courant    |
| `cp`     | copier un fichier              |
| `mv`     | déplacer ou renommer           |
| `rm`     | supprimer                      |
| `cat`    | afficher un fichier            |
| `grep`   | rechercher dans un texte       |
| `ps`     | afficher les processus         |
| `top`    | voir l'utilisation CPU/mémoire |

---

## Distribution Linux

Linux existe sous plusieurs **distributions**.

Exemples populaires :

| Distribution | Utilisation         |
| ------------ | ------------------- |
| Ubuntu       | serveurs et cloud   |
| Debian       | stable et minimal   |
| Red Hat      | entreprise          |
| Rocky Linux  | alternative Red Hat |
| Alpine       | conteneurs Docker   |

---

## Résumé

Linux est :

- le **système d’exploitation principal des serveurs**
- la **base technique de la majorité des outils DevOps**
- l’environnement dans lequel tournent **Docker, Kubernetes et le Cloud**

Maîtriser Linux permet de **comprendre et contrôler l’infrastructure moderne**.
