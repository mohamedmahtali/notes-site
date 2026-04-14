---
title: Self hosted runners
tags:
  - advanced
---
# Self hosted runners

## Parent
- [[GitHub actions]]

---

## Définition

Les self-hosted runners sont des machines (VM, bare-metal, conteneur) que tu héberges toi-même pour exécuter les workflows GitHub Actions. Ils donnent accès à du matériel spécifique, des réseaux privés, et évitent les limitations des runners GitHub-hosted.

---

## Pourquoi les utiliser

> [!note] Quand les runners GitHub ne suffisent pas
> - Accès à des ressources réseau internes (base de données privée, registry interne)
> - Builds nécessitant du matériel puissant (GPU, mémoire élevée)
> - Workloads qui dépassent les quotas de minutes GitHub
> - Environnements avec des exigences de conformité (données qui ne doivent pas quitter l'infra)

---

## Installation

```bash
# Sur la machine hôte
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L   https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

# Configurer (token récupéré dans Settings → Actions → Runners)
./config.sh --url https://github.com/org/repo --token TOKEN

# Installer comme service systemd
sudo ./svc.sh install
sudo ./svc.sh start
```

---

## Utiliser dans un workflow

```yaml
jobs:
  build-gpu:
    runs-on: self-hosted          # runner auto-sélectionné
    # ou avec labels spécifiques
    runs-on: [self-hosted, linux, gpu]
    steps:
      - uses: actions/checkout@v4
      - run: python train.py
```

---

> [!warning]
> Ne jamais utiliser des self-hosted runners pour des repos publics — n'importe qui peut créer une PR et exécuter du code sur ta machine.
