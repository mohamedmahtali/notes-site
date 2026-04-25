---
title: "Lab IaC — Provisionner un serveur avec Ansible"
tags:
  - iac
  - intermediate
---

# Lab IaC — Provisionner un serveur avec Ansible

## Objectif

Utiliser Ansible pour configurer automatiquement un serveur : installer [[Nginx]], déployer une page web, configurer un utilisateur et un service [[systemd]].

> [!note] Prérequis
> - Ansible installé (`pip install ansible`)
> - Un serveur cible accessible via [[SSH]] (VM locale, VM [[Cloud]], ou localhost)
> - Clé SSH configurée

---

## Étape 1 — Structure du projet

```bash
mkdir ansible-lab && cd ansible-lab

mkdir -p roles/webserver/{tasks,templates,handlers,vars}
touch inventory.ini site.yml
```

---

## Étape 2 — Inventaire

```ini
# inventory.ini
[webservers]
web01 ansible_host=192.168.1.100 ansible_user=ubuntu

[webservers:vars]
ansible_ssh_private_key_file=~/.ssh/id_rsa

# Pour un test local (localhost)
# [webservers]
# localhost ansible_connection=local
```

```bash
# Tester la connectivité
ansible all -i inventory.ini -m ping
```

---

## Étape 3 — Rôle Webserver

```yaml
# roles/webserver/vars/main.yml
webserver_port: 80
webserver_user: webadmin
app_name: "Mon App DevOps"
```

```yaml
# roles/webserver/tasks/main.yml
---
- name: Mettre à jour le cache apt
  apt:
    update_cache: yes
    cache_valid_time: 3600
  become: true

- name: Installer nginx
  apt:
    name: nginx
    state: present
  become: true
  notify: Restart nginx

- name: Créer l'utilisateur web
  user:
    name: "{{ webserver_user }}"
    shell: /bin/bash
    create_home: yes
  become: true

- name: Déployer la page d'accueil
  template:
    src: index.html.j2
    dest: /var/www/html/index.html
    owner: www-data
    group: www-data
    mode: "0644"
  become: true
  notify: Reload nginx

- name: Déployer la configuration nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/sites-available/default
    owner: root
    mode: "0644"
  become: true
  notify: Reload nginx

- name: Activer nginx au démarrage
  service:
    name: nginx
    enabled: yes
    state: started
  become: true
```

```yaml
# roles/webserver/handlers/main.yml
---
- name: Restart nginx
  service:
    name: nginx
    state: restarted
  become: true

- name: Reload nginx
  service:
    name: nginx
    state: reloaded
  become: true
```

```html
<!-- roles/webserver/templates/index.html.j2 -->
<!DOCTYPE html>
<html>
<head><title>{{ app_name }}</title></head>
<body>
  <h1>{{ app_name }}</h1>
  <p>Serveur : {{ inventory_hostname }}</p>
  <p>Déployé par Ansible le : {{ ansible_date_time.date }}</p>
  <p>OS : {{ ansible_distribution }} {{ ansible_distribution_version }}</p>
</body>
</html>
```

```nginx
# roles/webserver/templates/nginx.conf.j2
server {
    listen {{ webserver_port }};
    server_name _;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /health {
        return 200 "OK";
        add_header Content-Type text/plain;
    }
}
```

---

## Étape 4 — Playbook principal

```yaml
# site.yml
---
- name: Configurer les serveurs web
  hosts: webservers
  gather_facts: yes

  roles:
    - webserver

  post_tasks:
    - name: Vérifier que nginx répond
      uri:
        url: "http://{{ inventory_hostname }}/health"
        status_code: 200
      register: health_check

    - name: Afficher le résultat
      debug:
        msg: "✅ Nginx répond correctement sur {{ inventory_hostname }}"
```

---

## Étape 5 — Exécution

```bash
# Dry-run (vérifier sans appliquer)
ansible-playbook -i inventory.ini site.yml --check --diff

# Appliquer
ansible-playbook -i inventory.ini site.yml

# Vérifier l'idempotence (re-exécuter : tout doit être "ok", rien "changed")
ansible-playbook -i inventory.ini site.yml
```

---

## Vérification finale

- [ ] `ansible all -m ping` → `pong`
- [ ] Playbook s'exécute sans erreur
- [ ] Page web accessible : `curl http://IP_SERVEUR`
- [ ] Page affiche le hostname et la date de déploiement
- [ ] 2e exécution = 0 `changed` (idempotence)

## Liens

- [[Infrastructure as Code]]
- [[Ansible]]
- [[Playbooks]]
- [[Templates]]
- [[Idempotence]]
