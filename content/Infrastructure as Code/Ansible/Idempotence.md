---
title: Idempotence
tags:
  - intermediate
---
# Idempotence

---

## Définition

L'idempotence signifie que re-exécuter un playbook [[Ansible]] produit le même résultat qu'une première exécution — si le serveur est déjà dans l'état désiré, aucune modification n'est faite. C'est une propriété fondamentale d'Ansible.

---

## Pourquoi c'est important

> [!tip] Exécuter en toute sécurité à tout moment
> Grâce à l'idempotence, tu peux re-exécuter un playbook sans craindre de casser quelque chose. C'est essentiel pour le déploiement continu et la récupération après incident.

---

## Modules idempotents vs commandes brutes

```yaml
# NON idempotent — crée un user même s'il existe déjà
- command: useradd deploy

# Idempotent — vérifie avant de créer
- user:
    name: deploy
    state: present    # crée si absent, ignore si présent

# NON idempotent
- shell: echo "log" >> /var/log/deploy.log

# Idempotent avec condition
- shell: /opt/migrate.sh
  changed_when: false   # toujours "OK", jamais "changed"
  # ou
  creates: /var/lib/migrated   # skip si ce fichier existe
```

---

## Valider l'idempotence

```bash
# Premier run — changes attendus
ansible-playbook playbook.yml

# Deuxième run — zéro changes attendu
ansible-playbook playbook.yml
# → PLAY RECAP : changed=0, failed=0

# Mode check (dry-run idempotent)
ansible-playbook playbook.yml --check
```

---

> [!warning]
> Les [[Modules]] `command` et `shell` ne sont pas idempotents par défaut. Toujours utiliser `creates:`, `removes:`, ou `changed_when:` pour les rendre idempotents, ou préférer les modules dédiés (apt, [[COPY]], template).
