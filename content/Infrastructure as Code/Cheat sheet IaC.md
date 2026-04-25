---
title: Cheat sheet IaC
tags:
  - iac
  - intermediate
---

# Cheat sheet IaC

## Terraform — Commandes

```bash
# Cycle de vie
terraform init                  # Initialiser (providers, modules)
terraform plan                  # Prévisualiser les changements
terraform plan -out=tfplan      # Sauvegarder le plan
terraform apply                 # Appliquer
terraform apply tfplan          # Appliquer un plan sauvegardé
terraform apply -auto-approve   # Sans confirmation (CI/CD)
terraform destroy               # Détruire toutes les ressources
terraform destroy -target=aws_instance.web  # Détruire une ressource

# State
terraform show                  # Voir le state actuel
terraform state list            # Lister les ressources
terraform state show aws_instance.web  # Détails d'une ressource
terraform state rm aws_instance.web    # Retirer du state (sans détruire)
terraform import aws_instance.web i-1234567890abcdef0  # Importer

# Validation
terraform validate              # Valider la syntaxe HCL
terraform fmt                   # Formatter le code
terraform fmt -recursive        # Récursivement

# Workspaces
terraform workspace list
terraform workspace new staging
terraform workspace select prod

# Modules
terraform get                   # Télécharger les modules
terraform providers             # Lister les providers utilisés
```

## Terraform — Snippets HCL

```hcl
# Variables
variable "env" {
  type    = string
  default = "dev"
}

# Outputs
output "instance_ip" {
  value = aws_instance.web.public_ip
}

# Locals
locals {
  name_prefix = "${var.project}-${var.env}"
}

# Data source
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-22.04-amd64-server-*"]
  }
}

# Conditionnel
resource "aws_instance" "web" {
  count         = var.env == "prod" ? 3 : 1
  instance_type = var.env == "prod" ? "t3.large" : "t3.micro"
}
```

## Ansible — Commandes

```bash
# Ping tous les hosts
ansible all -m ping
ansible web -m ping -i inventory.ini

# Commande ad-hoc
ansible all -m shell -a "uptime"
ansible web -m apt -a "name=nginx state=present" --become

# Playbooks
ansible-playbook site.yml
ansible-playbook site.yml -i production.ini
ansible-playbook site.yml --tags nginx
ansible-playbook site.yml --skip-tags debug
ansible-playbook site.yml --limit web01
ansible-playbook site.yml -e "env=prod"   # Extra vars
ansible-playbook site.yml --check          # Dry-run
ansible-playbook site.yml --diff           # Voir les diff

# Vault
ansible-vault encrypt secrets.yml
ansible-vault decrypt secrets.yml
ansible-vault edit secrets.yml
ansible-playbook site.yml --ask-vault-pass
```

## Ansible — Snippets YAML

```yaml
# Tâche avec condition et boucle
- name: Install packages
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - nginx
    - git
    - curl
  when: ansible_os_family == "Debian"
  become: true
  notify: Restart nginx

# Handler
handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted

# Template Jinja2
- name: Deploy config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    mode: '0644'
```

## Liens

- [[Infrastructure as Code]]
- [[Terraform]]
- [[Ansible]]
