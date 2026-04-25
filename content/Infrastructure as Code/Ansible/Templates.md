---
title: Templates
tags:
  - intermediate
---
# Templates

---

## Définition

Les templates [[Ansible]] utilisent le moteur Jinja2 pour générer des fichiers de configuration dynamiques. Ils permettent de créer des configs personnalisées par [[Host]] ou environnement à partir d'un seul template.

---

## Utilisation

```yaml
# Task
- name: Deploy nginx config
  template:
    src: nginx.conf.j2      # template source (dans templates/)
    dest: /etc/nginx/nginx.conf
    owner: root
    mode: '0644'
    validate: nginx -t -c %s   # valider avant de déployer
  notify: Reload nginx
```

---

## Template nginx.conf.j2

```nginx
user {{ nginx_user | default('www-data') }};
worker_processes {{ ansible_processor_vcpus }};
error_log /var/log/nginx/error.log {{ nginx_log_level | default('warn') }};

events {
    worker_connections {{ nginx_worker_connections | default(1024) }};
}

http {
    server_name_hash_bucket_size 128;

    {% for vhost in nginx_vhosts %}
    server {
        listen {{ vhost.port | default(80) }};
        server_name {{ vhost.name }};

        location / {
            proxy_pass http://{{ vhost.backend }};
        }
    }
    {% endfor %}
}
```

---

> [!note]
> Voir [[Jinja2]] pour la syntaxe complète des templates Jinja2 dans Ansible.
