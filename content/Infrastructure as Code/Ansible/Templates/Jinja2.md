---
title: Jinja2
tags:
  - intermediate
---
# Jinja2

## Parent
- [[Templates]]

---

## Définition

Jinja2 est le moteur de templating utilisé par Ansible. Il permet d'insérer des variables, d'évaluer des conditions, et de boucler dans des fichiers texte pour générer des configurations dynamiques.

---

## Syntaxe de base

```jinja2
{# Commentaire — non inclus dans l'output #}

{# Variables #}
{{ variable }}
{{ variable | default('valeur_defaut') }}
{{ ansible_hostname | upper }}
{{ liste | join(', ') }}

{# Conditions #}
{% if environment == 'production' %}
log_level = warning
{% elif environment == 'staging' %}
log_level = info
{% else %}
log_level = debug
{% endif %}

{# Boucles #}
{% for server in backend_servers %}
server {{ server.name }} {{ server.ip }}:{{ server.port }};
{% endfor %}

{# Filtres utiles #}
{{ chemin | basename }}          {# /etc/nginx.conf → nginx.conf #}
{{ texte | lower }}
{{ nombre | int }}
{{ liste | length }}
{{ dict | to_json }}
{{ "secret" | password_hash('sha512') }}
```

---

## Template de configuration complète

```jinja2
# Généré par Ansible le {{ ansible_date_time.date }}
# NE PAS MODIFIER MANUELLEMENT

[database]
host = {{ db_host }}
port = {{ db_port | default(5432) }}
name = {{ db_name }}
pool_size = {{ db_pool_size | default(10) }}

{% if enable_ssl %}
ssl_mode = require
ssl_cert = /etc/ssl/certs/{{ inventory_hostname }}.crt
{% endif %}
```
