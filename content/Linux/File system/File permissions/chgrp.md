---
title: chgrp
tags:
  - beginner
---

# chgrp

---

## Définition

`chgrp` (change group) modifie le groupe propriétaire d'un fichier. Fonctionnellement identique à `chown :groupe fichier`.

---

## Syntaxe

```bash
# Changer le groupe
chgrp www-data /var/www/html/
chgrp developers /opt/projet/

# Récursif
chgrp -R www-data /var/www/

# Copier le groupe d'un fichier référence
chgrp --reference=fichier-ref autre-fichier
```

---

> [!note]
> En pratique, `chown user:group` est plus utilisé que `chgrp` car il permet de changer propriétaire et groupe en une seule commande.
