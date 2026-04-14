---
title: Restart policies
tags:
  - intermediate
---

# Restart policies

## Parent
- [[Services]]

---

## Définition

La restart policy d'un service systemd définit dans quels cas le service est automatiquement redémarré après un arrêt.

---

## Valeurs

```ini
[Service]
# no : ne jamais redémarrer (défaut)
Restart=no

# always : toujours redémarrer
Restart=always

# on-failure : redémarrer si exit code ≠ 0 ou tué par signal
Restart=on-failure

# on-abnormal : sur signal, timeout, watchdog
Restart=on-abnormal

# on-abort : seulement si tué par signal non-clean
Restart=on-abort
```

---

## Paramètres de délai

```ini
[Service]
Restart=on-failure
RestartSec=5s             # attendre 5s avant de redémarrer

# Limiter les redémarrages en boucle
StartLimitIntervalSec=60s  # fenêtre de 60s
StartLimitBurst=3          # max 3 redémarrages dans cette fenêtre
# → après 3 échecs en 60s, le service passe en "failed"
```

---

## Exemple production

```ini
[Service]
Restart=on-failure
RestartSec=10s
StartLimitIntervalSec=120s
StartLimitBurst=5
```

---

> [!tip]
> `Restart=on-failure` est le choix standard pour les services de production. Il redémarre sur crash (exit non-zero) mais pas sur arrêt propre (systemctl stop), évitant les boucles infinies lors des maintenances.
