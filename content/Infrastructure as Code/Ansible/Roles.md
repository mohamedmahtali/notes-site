---
title: Roles
tags:
  - intermediate
---
# Roles

---

## Définition

Les rôles [[Ansible]] sont des unités réutilisables qui encapsulent [[Tasks]], [[Handlers]], [[Templates]], fichiers, et [[Variables]] pour une fonctionnalité spécifique ([[Nginx]], postgresql, [[Docker]]). Ils structurent les [[Playbooks]] complexes.

---

## Structure d'un rôle

```
roles/nginx/
├── tasks/
│   └── main.yml       # tâches principales
├── handlers/
│   └── main.yml       # handlers (restart, reload)
├── templates/
│   └── nginx.conf.j2  # templates Jinja2
├── files/
│   └── htpasswd       # fichiers statiques
├── vars/
│   └── main.yml       # variables internes au rôle
├── defaults/
│   └── main.yml       # valeurs par défaut (overridables)
└── meta/
    └── main.yml       # dépendances du rôle
```

---

## Utiliser un rôle

```yaml
# playbook.yml
- hosts: webservers
  roles:
    - nginx                        # rôle simple
    - role: app                    # avec variables
      vars:
        app_port: 9090
    - { role: monitoring, when: enable_monitoring }
```

---

## Ansible Galaxy (rôles communautaires)

```bash
# Installer un rôle depuis Galaxy
ansible-galaxy install geerlingguy.nginx
ansible-galaxy install -r requirements.yml

# requirements.yml
roles:
  - name: geerlingguy.nginx
    version: 3.2.0
  - src: https://github.com/mycompany/ansible-role-app.git
    scm: git
    version: v1.0.0
```
