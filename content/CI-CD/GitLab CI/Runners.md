---
title: Runners
tags:
  - intermediate
---
# Runners

---

## Définition

Les GitLab Runners sont des agents qui exécutent les jobs CI/CD. GitLab.com fournit des runners partagés. Pour des projets self-hosted ou avec des besoins spécifiques, on enregistre ses propres runners.

---

## Types de runners

| Type | Scope | Utilisation |
|---|---|---|
| Shared | Tous les projets GitLab | Jobs standards, gratuits sur GitLab.com |
| Group | Tous les projets d'un groupe | Partage d'infra entre projets liés |
| Specific | Un seul projet | Besoins spécifiques, accès réseau privé |

---

## Installation et enregistrement

```bash
# Installer le runner
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
sudo apt install gitlab-runner

# Enregistrer avec GitLab
sudo gitlab-runner register   --url https://gitlab.com   --registration-token TOKEN   --executor docker   --docker-image alpine:latest   --description "My runner"   --tag-list "docker,linux"
```

---

## Utilisation dans `.gitlab-ci.yml`

```yaml
# Job qui tourne sur n'importe quel runner disponible
test:
  script: npm test

# Job qui requiert des tags spécifiques
deploy:gpu:
  tags:
    - gpu
    - linux
  script: python train.py
```

---

## Runner Docker executor

```toml
# /etc/gitlab-runner/config.toml
[[runners]]
  executor = "docker"
  [runners.docker]
    image = "alpine:latest"
    privileged = false
    volumes = ["/cache"]
    pull_policy = ["if-not-present"]
```
