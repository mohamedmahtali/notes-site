---
title: chown
tags:
  - beginner
---

# chown

## Parent
- [[File permissions]]

---

## Définition

`chown` (change owner) modifie le propriétaire et/ou le groupe d'un fichier. Seul root peut changer le propriétaire. Le propriétaire peut changer le groupe vers un groupe dont il est membre.

---

## Syntaxe

```bash
# Changer le propriétaire
chown user fichier

# Changer propriétaire et groupe
chown user:group fichier

# Changer seulement le groupe (identique à chgrp)
chown :group fichier

# Récursif
chown -R www-data:www-data /var/www/html/
chown -R deploy:deploy /opt/app/

# Copier les permissions d'un fichier référence
chown --reference=fichier-ref autre-fichier
```

---

## Exemples pratiques

```bash
# Application web
chown -R www-data:www-data /var/www/html/

# Application avec service account
chown -R appuser:appgroup /opt/mon-app/

# Logs accessibles par le service
chown root:appgroup /var/log/mon-app/
chmod 775 /var/log/mon-app/

# Après copie de fichiers (root → utilisateur)
cp /tmp/config.yaml /etc/app/
chown appuser:appgroup /etc/app/config.yaml
chmod 640 /etc/app/config.yaml
```
