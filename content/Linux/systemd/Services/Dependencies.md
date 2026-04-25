---
title: Dependencies
tags:
  - intermediate
---

# Dependencies

---

## Définition

[[systemd]] gère les dépendances entre [[Services]] pour garantir l'ordre de démarrage correct. Un service peut déclarer qu'il a besoin d'autres services avant de démarrer.

---

## Directives

```ini
[Unit]
# After= : ordre seulement (démarrer après X si X est actif)
After=network.target postgresql.service

# Requires= : dépendance stricte (si X s'arrête, ce service aussi)
Requires=postgresql.service

# Wants= : dépendance souple (essaie de démarrer X, continue si X échoue)
Wants=redis.service

# BindsTo= : comme Requires mais réciproque
BindsTo=postgresql.service

# Conflicts= : ne peut pas tourner en même temps que X
Conflicts=apache2.service
```

---

## Targets (groupes de services)

```bash
# multi-user.target ≈ runlevel 3 (sans GUI)
# graphical.target ≈ runlevel 5 (avec GUI)

# Voir la target par défaut
systemctl get-default

# Changer la target par défaut
systemctl set-default multi-user.target
```

---

## Inspecter les dépendances

```bash
# Arbre des dépendances
systemctl list-dependencies nginx

# Ce qui dépend de ce service
systemctl list-dependencies --reverse nginx
```
