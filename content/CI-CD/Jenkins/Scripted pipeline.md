---
title: Scripted pipeline
tags:
  - advanced
---
# Scripted pipeline

## Parent
- [[Jenkins]]

---

## Définition

Le Scripted Pipeline est la syntaxe Groovy pure pour Jenkins. Plus flexible que le Declarative Pipeline, il permet des constructions arbitraires (boucles, conditions complexes, fonctions), mais est plus difficile à lire et maintenir.

---

## Quand l'utiliser

> [!note] Flexibilité vs lisibilité
> Préférer le Declarative Pipeline dans 90% des cas. Utiliser le Scripted Pipeline seulement quand les capacités du Declarative sont insuffisantes : logique conditionnelle complexe, génération dynamique de stages, intégration avancée avec des APIs Jenkins.

---

## Exemple

```groovy
node('linux') {
    def image
    def version = ""

    try {
        stage('Checkout') {
            checkout scm
            version = sh(returnStdout: true, script: 'cat version.txt').trim()
        }

        stage('Build') {
            image = docker.build("myapp:${version}")
        }

        stage('Test') {
            image.inside {
                sh 'npm test'
            }
        }

        // Stage dynamique basé sur la branche
        if (env.BRANCH_NAME == 'main') {
            stage('Deploy Production') {
                input message: 'Deploy to production?'
                sh "./deploy.sh production ${version}"
            }
        } else {
            stage('Deploy Staging') {
                sh "./deploy.sh staging ${version}"
            }
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    } finally {
        cleanWs()
    }
}
```
