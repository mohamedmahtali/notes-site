---
title: Targets
tags:
  - intermediate
---

# Targets

---

## Définition

Les targets [[systemd]] sont des unités spéciales qui représentent des états système — analogues aux runlevels de SysV. Elles regroupent des [[Services]] et permettent d'atteindre un état système cohérent (réseau disponible, multi-utilisateur, GUI…).

---

## Targets principales

| Target | Ancien runlevel | Description |
|---|---|---|
| `poweroff.target` | 0 | Arrêt |
| `rescue.target` | 1 | Mode mono-utilisateur |
| `multi-user.target` | 3 | Multi-utilisateur sans GUI |
| `graphical.target` | 5 | Multi-utilisateur avec GUI |
| `reboot.target` | 6 | Redémarrage |
| `emergency.target` | — | [[Shell]] minimal en urgence |

---

## Commandes

```bash
# Voir la target active
systemctl get-default

# Changer la target par défaut (serveur sans GUI)
systemctl set-default multi-user.target

# Basculer vers une target immédiatement
systemctl isolate rescue.target

# Lister toutes les targets
systemctl list-units --type=target
```

---

## Dans un unit file

```ini
[Install]
WantedBy=multi-user.target
# → le service sera activé quand multi-user.target est atteint
```
