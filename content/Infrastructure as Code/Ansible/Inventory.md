---
title: Inventory
tags:
  - beginner
---
# Inventory

---

## Définition

L'inventory [[Ansible]] liste les hôtes (serveurs) à gérer et les organise en groupes. Il peut être statique (fichier INI ou YAML) ou dynamique (script qui interroge [[AWS]]/GCP pour lister les instances).

---

## Format INI

```ini
# inventory.ini
[webservers]
web-01 ansible_host=10.0.1.10
web-02 ansible_host=10.0.1.11

[databases]
db-01 ansible_host=10.0.2.10 ansible_user=postgres

[production:children]
webservers
databases

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/prod-key.pem
ansible_python_interpreter=/usr/bin/python3
```

---

## Format YAML

```yaml
# inventory.yml
all:
  children:
    webservers:
      hosts:
        web-01:
          ansible_host: 10.0.1.10
        web-02:
          ansible_host: 10.0.1.11
    databases:
      hosts:
        db-01:
          ansible_host: 10.0.2.10
  vars:
    ansible_user: ubuntu
    ansible_ssh_private_key_file: ~/.ssh/prod-key.pem
```

---

## Inventory dynamique AWS

```bash
# Plugin AWS EC2 — liste les instances automatiquement
ansible-inventory -i aws_ec2.yml --list

# aws_ec2.yml
plugin: amazon.aws.aws_ec2
regions:
  - eu-west-1
filters:
  tag:Environment: production
keyed_groups:
  - key: tags.Role
    prefix: role
```
