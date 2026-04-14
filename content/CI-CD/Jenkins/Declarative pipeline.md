---
title: Declarative pipeline
tags:
  - intermediate
---
# Declarative pipeline

## Parent
- [[Jenkins]]

---

## Définition

La syntaxe Declarative Pipeline est la façon moderne et recommandée d'écrire des Jenkinsfiles. Elle impose une structure prédéfinie (pipeline → stages → stage → steps) qui est plus lisible et moins sujette aux erreurs que le Scripted Pipeline.

---

## Syntaxe complète

```groovy
pipeline {
    agent any                  // où tourner le build

    environment {              // variables d'environnement
        REGISTRY = 'myregistry.io'
    }

    options {
        skipDefaultCheckout()  // ne pas checkout automatiquement
        timestamps()           // ajouter des timestamps aux logs
        retry(2)               // réessayer 2 fois si échec
    }

    triggers {
        cron('H 2 * * 1-5')   // nightly build du lundi au vendredi
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build & Test') {
            parallel {         // stages en parallèle
                stage('Build') {
                    steps { sh 'make build' }
                }
                stage('Test') {
                    steps { sh 'make test' }
                    post {
                        always { junit 'reports/*.xml' }
                    }
                }
            }
        }
    }

    post {
        always { cleanWs() }   // nettoyer le workspace
        success { echo 'Success!' }
        failure { emailext subject: 'FAILED', body: '...', to: 'team@' }
    }
}
```
