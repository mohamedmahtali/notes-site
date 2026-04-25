---
title: Ansible
tags:
  - intermediate
---
# Ansible

---

## Définition

Ansible est un outil d'automatisation de configuration et de déploiement. Il fonctionne en [[SSH]] sans agent, utilise YAML pour les [[Playbooks]], et est idempotent — re-exécuter un playbook n'a pas d'effet si la cible est déjà dans l'état désiré.

---

## Pourquoi c'est important

> [!tip] Configuration as Code sans agent
> Ansible configure des serveurs via SSH sans installer d'agent. Idéal pour gérer des dizaines à des milliers de serveurs de façon cohérente. Alternative à Puppet/Chef mais plus simple à prendre en main.

---

## Commandes essentielles

```bash
# Tester la connectivité
ansible all -i inventory.ini -m ping

# Exécuter une commande
ansible webservers -i inventory.ini -m command -a "uptime"

# Exécuter un playbook
ansible-playbook -i inventory.ini playbook.yml

# Mode dry-run
ansible-playbook -i inventory.ini playbook.yml --check

# Verbose
ansible-playbook -i inventory.ini playbook.yml -v

# Limiter à un host
ansible-playbook -i inventory.ini playbook.yml --limit web-01
```

---

## Structure d'un projet Ansible

```
project/
├── inventory.ini         # ou hosts.yml
├── playbook.yml          # playbook principal
├── group_vars/
│   ├── all.yml          # variables pour tous les hosts
│   └── webservers.yml   # variables pour le groupe webservers
├── host_vars/
│   └── web-01.yml       # variables pour un host spécifique
└── roles/
    └── nginx/            # rôle nginx réutilisable
        ├── tasks/main.yml
        ├── templates/
        └── handlers/main.yml
```
