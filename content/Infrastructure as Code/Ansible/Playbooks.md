---
title: Playbooks
tags:
  - beginner
---
# Playbooks

## Parent
- [[Ansible]]

---

## Définition

Un playbook Ansible est un fichier YAML qui décrit une série de tâches à exécuter sur un groupe de serveurs. C'est le fichier principal d'orchestration d'Ansible.

---

## Structure

```yaml
---
# playbook.yml
- name: Configure web servers
  hosts: webservers          # groupe dans l'inventory
  become: true               # sudo
  vars:
    app_port: 8080

  pre_tasks:
    - name: Update apt cache
      apt:
        update_cache: true
        cache_valid_time: 3600

  roles:
    - nginx                  # rôle réutilisable
    - app

  tasks:
    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: true

    - name: Deploy application config
      template:
        src: app.conf.j2
        dest: /etc/app/app.conf
      notify: Restart app     # déclenche le handler

  post_tasks:
    - name: Verify service is responding
      uri:
        url: "http://localhost:{{ app_port }}/health"
        status_code: 200
```

---

## Modules courants

```yaml
# Fichiers
- copy: src=files/config dest=/etc/app/config mode=0644
- template: src=config.j2 dest=/etc/app/config
- file: path=/var/log/app state=directory mode=0755

# Packages
- apt: name=nginx state=present update_cache=yes   # Debian/Ubuntu
- yum: name=nginx state=present                    # RHEL/CentOS
- pip: name=flask version=2.3.0

# Services
- service: name=nginx state=started enabled=yes

# Commandes
- command: /opt/app/migrate.sh
- shell: "echo $(date) >> /var/log/deploy.log"
```
