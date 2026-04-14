---
title: netstat
tags:
  - beginner
---

# netstat

## Parent
- [[Troubleshooting]]

---

## Définition

`netstat` est l'outil historique de diagnostic réseau. Il affiche les connexions, les ports en écoute, les tables de routage, et les statistiques. Remplacé par `ss` et `ip` sur les systèmes modernes, mais encore très présent dans la documentation.

---

## Commandes

```bash
# Ports en écoute (équivalent ss -tlnp)
netstat -tlnp

# Toutes les connexions TCP
netstat -tn

# Table de routage (équivalent ip route)
netstat -r
netstat -rn    # sans résolution de noms

# Statistiques par protocole
netstat -s

# Connexions d'une interface
netstat -i
```

---

## Correspondance netstat → ss

| netstat | ss équivalent |
|---|---|
| `netstat -tlnp` | `ss -tlnp` |
| `netstat -tn` | `ss -tn` |
| `netstat -r` | `ip route show` |
| `netstat -s` | `ss -s` |

---

> [!note]
> Sur Debian/Ubuntu, `netstat` est dans le paquet `net-tools` qui n'est plus installé par défaut. Utiliser `ss` directement sur les systèmes modernes.
