---
title: Runners
tags:
  - intermediate
---
# Runners

## Parent
- [[CI-CD]]

---

## Définition

Les runners (ou agents) sont les machines qui exécutent physiquement les jobs du pipeline CI/CD. Chaque plateforme CI a son concept : GitHub Actions runners, GitLab Runners, Jenkins agents, CircleCI executors.

---

## Comparaison entre plateformes

| Plateforme | Runners hébergés | Self-hosted | Config |
|---|---|---|---|
| GitHub Actions | ✅ ubuntu/windows/macos | ✅ | `runs-on:` |
| GitLab CI | ✅ sur gitlab.com | ✅ | `tags:` |
| Jenkins | ❌ (self-hosted) | ✅ | `agent` |

---

## GitHub Actions — runner specs

```yaml
jobs:
  build:
    runs-on: ubuntu-latest      # Linux 2 vCPU, 7GB RAM, 14GB SSD
    # runs-on: ubuntu-22.04     # version explicite
    # runs-on: windows-latest   # Windows Server 2022
    # runs-on: macos-14         # macOS Sonoma (Apple Silicon)
    # runs-on: [self-hosted, linux, x64]  # self-hosted
```

---

## Jenkins agents

```groovy
// Jenkinsfile
pipeline {
    agent {
        docker {
            image 'node:20-alpine'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
    }
}
```

---

> [!tip]
> Pour les builds Docker dans les runners, configurer le Docker socket mount ou utiliser Kaniko/Buildah pour des builds rootless sans Docker daemon.
