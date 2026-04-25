---
title: Variables
tags:
  - intermediate
---
# Variables

---

## Définition

Les variables [[Ansible]] permettent de paramétrer les [[Playbooks]] et rôles. Elles peuvent être définies à plusieurs niveaux avec des priorités différentes (host_vars > group_vars > [[Defaults]]).

---

## Priorité des variables (du plus fort au plus faible)

```
1. Extra vars CLI (-e var=value)       ← plus haute priorité
2. Task vars (dans la task)
3. Block vars
4. Role vars (vars/main.yml)
5. Play vars
6. Host facts (ansible_*)
7. host_vars/ (variables par host)
8. group_vars/groupname/
9. group_vars/all/
10. Role defaults (defaults/main.yml)  ← plus faible priorité
```

---

## Définir et utiliser des variables

```yaml
# group_vars/webservers.yml
nginx_port: 80
nginx_worker_processes: auto
app_name: myapp

# Dans un playbook/task
- name: Configure nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  vars:
    max_connections: 1024

# Dans un template
server {
    listen {{ nginx_port }};
    worker_processes {{ nginx_worker_processes }};
}
```

---

## Facts et register

```yaml
# Collecter les facts du système
- setup:   # collecte : ansible_os_family, ansible_distribution, etc.

# Utiliser les facts
- name: Install package (cross-distro)
  package:
    name: nginx
    state: present

# Register — capturer le résultat d'une task
- name: Check service
  command: systemctl is-active nginx
  register: nginx_status
  changed_when: false

- debug:
    msg: "Nginx status: {{ nginx_status.stdout }}"
```
