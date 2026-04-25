---
title: Boot logs
tags:
  - intermediate
---
# Boot logs

---

## Définition

Les boot logs sont les messages enregistrés par journald depuis le démarrage du système. Ils couvrent l'initialisation du [[Kernel]], le démarrage de [[systemd]], et le lancement de chaque service — indispensables pour diagnostiquer les problèmes au boot.

---

## Pourquoi c'est important

> [!tip] Premier diagnostic d'un système qui ne démarre pas
> Quand un service ne démarre pas ou que le boot est lent, les boot logs permettent d'identifier exactement où et pourquoi ça a bloqué, avec les timestamps précis pour mesurer les délais.

---

## Commandes

```bash
# Logs du boot actuel
journalctl -b
journalctl -b 0              # boot actuel (explicite)

# Boot précédent
journalctl -b -1             # avant-dernier boot
journalctl -b -2             # deux boots en arrière

# Lister les boots disponibles
journalctl --list-boots

# Logs d'un boot spécifique avec filtrage
journalctl -b -1 -p err      # erreurs du boot précédent
journalctl -b -u nginx       # logs nginx au dernier boot

# Analyse du temps de démarrage
systemd-analyze              # temps total
systemd-analyze blame        # services les plus lents
systemd-analyze critical-chain   # chemin critique

# Chercher des erreurs au boot
journalctl -b -p 0..3        # emergency + alert + critical + error
```

---

## Exemple de sortie

```
Jan 15 08:00:01 server kernel: Linux version 6.5.0-25-generic
Jan 15 08:00:01 server kernel: Command line: BOOT_IMAGE=/vmlinuz-6.5.0
Jan 15 08:00:03 server systemd[1]: Started Journal Service
Jan 15 08:00:05 server systemd[1]: Started Network Manager
```

---

> [!note]
> Les boots sont numérotés 0 (actuel), -1 (précédent), etc. Utiliser `--list-boots` pour voir tous les boots avec leur timestamp et ID.
