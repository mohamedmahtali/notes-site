---
title: Jenkinsfile
tags:
  - intermediate
---
# Jenkinsfile

---

## Définition

Un Jenkinsfile est un fichier texte (Groovy DSL) à la racine du repo qui définit le [[Pipeline]] [[Jenkins]]. Il versionne la configuration CI avec le code — "Pipeline as Code".

---

## Avantages

> [!tip] Pipeline as Code
> Le Jenkinsfile est versionné avec le code : historique des changements de pipeline, review via PR, [[Rollback]] possible. Remplace les configurations Jenkins manuelles dans l'interface web.

---

## Structure Declarative (recommandée)

```groovy
pipeline {
    agent { docker { image 'node:20' } }

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    parameters {
        choice(name: 'ENV', choices: ['staging', 'production'])
    }

    stages {
        stage('Install') {
            steps { sh 'npm ci' }
        }
        stage('Test') {
            parallel {
                stage('Unit') { steps { sh 'npm run test:unit' } }
                stage('Lint') { steps { sh 'npm run lint' } }
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t myapp:${BUILD_NUMBER} ."
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                sh "./deploy.sh ${params.ENV}"
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded!' }
        failure { mail to: 'team@example.com', subject: 'Build failed' }
    }
}
```
