---
title: Jenkins
tags:
  - intermediate
---
# Jenkins

---

## Définition

Jenkins est le serveur d'automatisation open-source le plus répandu. Auto-hébergé, extensible par plus de 1800 plugins, il orchestre les [[Pipeline]] CI/CD pour des centaines de milliers d'organisations.

---

## Pourquoi c'est important

> [!note] Le vétéran du CI/CD
> Jenkins est partout dans les entreprises. Créé en 2011, il est mature, stable, et hautement configurable. Sa flexibilité totale a un coût : configuration et maintenance plus complexes que [[GitHub actions]] ou GitLab CI.

---

## Jenkinsfile basique

```groovy
// Jenkinsfile
pipeline {
    agent any

    environment {
        REGISTRY = 'myregistry.io'
        IMAGE = "${REGISTRY}/myapp:${BUILD_NUMBER}"
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE} .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run ${IMAGE} npm test'
            }
            post {
                always {
                    junit 'test-results/*.xml'
                }
            }
        }
        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'registry-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'docker login -u $USER -p $PASS $REGISTRY'
                    sh 'docker push ${IMAGE}'
                }
            }
        }
    }
    post {
        failure {
            slackSend message: "Build ${BUILD_NUMBER} failed!"
        }
    }
}
```

---

> [!note]
> Voir [[Declarative pipeline]] (syntaxe moderne recommandée) et [[Scripted pipeline]] (Groovy pur, plus flexible).
