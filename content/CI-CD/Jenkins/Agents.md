---
title: Agents
tags:
  - intermediate
---
# Agents

---

## Définition

Les agents [[Jenkins]] (anciennement "slaves") sont les machines qui exécutent les builds. Le contrôleur Jenkins (master) distribue les jobs aux agents disponibles selon des labels et critères de capacité.

---

## Déclaration d'agent dans Jenkinsfile

```groovy
// Agent statique par label
pipeline {
    agent { label 'linux-docker' }
}

// Agent Docker (conteneur éphémère)
pipeline {
    agent {
        docker {
            image 'maven:3.9-eclipse-temurin-17'
            args '-v $HOME/.m2:/root/.m2'   // cache Maven
        }
    }
}

// Agent Kubernetes (pod éphémère)
pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: maven
    image: maven:3.9
    command: ['sleep', 'infinity']
'''
            defaultContainer 'maven'
        }
    }
}
```

---

## Agents par stage

```groovy
pipeline {
    agent none    // pas d'agent global

    stages {
        stage('Build') {
            agent { docker { image 'node:20' } }
            steps { sh 'npm build' }
        }
        stage('Deploy') {
            agent { label 'deploy-server' }
            steps { sh './deploy.sh' }
        }
    }
}
```

---

> [!tip]
> Utiliser des agents [[Docker]] ou [[Kubernetes]] pour des builds reproductibles et des environnements propres. Les agents persistants accumulent les artefacts et créent des problèmes de flaky builds.
