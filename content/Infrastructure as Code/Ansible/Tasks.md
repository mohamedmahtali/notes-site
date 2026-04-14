---
title: Tasks
tags:
  - beginner
---
# Tasks

## Parent
- [[Ansible]]

---

## Définition

Les tasks sont les unités d'exécution dans Ansible. Chaque task appelle un module Ansible avec des paramètres pour effectuer une action spécifique (installer un package, copier un fichier, redémarrer un service).

---

## Exemples de tasks

```yaml
tasks:
  # Installer nginx
  - name: Install nginx
    apt:
      name: nginx
      state: present
      update_cache: yes
    tags: [packages]

  # Copier un fichier avec conditions
  - name: Deploy config
    copy:
      src: files/nginx.conf
      dest: /etc/nginx/nginx.conf
      owner: root
      group: root
      mode: '0644'
    notify: Reload nginx

  # Exécuter seulement si une condition est vraie
  - name: Run migration
    command: /opt/app/migrate.sh
    when: app_version is version('2.0', '>=')
    changed_when: false   # ne pas marquer comme "changed"

  # Loop
  - name: Create directories
    file:
      path: "{{ item }}"
      state: directory
      mode: '0755'
    loop:
      - /var/log/app
      - /var/run/app
      - /etc/app

  # Gérer les erreurs
  - name: Try optional step
    command: /opt/optional.sh
    ignore_errors: true
    register: result

  - name: Show result
    debug:
      var: result.stdout
```
