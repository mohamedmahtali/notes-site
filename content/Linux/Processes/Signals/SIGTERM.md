---
title: SIGTERM
tags:
  - intermediate
---
# SIGTERM

## Parent
- [[Signals]]

---

## Définition

SIGTERM (signal 15) est le signal d'arrêt poli de Unix. Il demande au processus de se terminer **proprement** : fermer les connexions, écrire les données en attente, libérer les ressources. Le processus peut intercepter SIGTERM et décider comment réagir.

---

## Pourquoi c'est important

> [!tip] Le signal d'arrêt par défaut
> `kill PID` envoie SIGTERM par défaut. C'est la façon correcte d'arrêter un service — il laisse le processus faire son cleanup. Kubernetes envoie SIGTERM avant SIGKILL lors d'un pod termination (grace period 30s par défaut).

---

## Utilisation

```bash
# Envoyer SIGTERM
kill 1234
kill -15 1234
kill -SIGTERM 1234

# Arrêt propre de tous les processus nginx
pkill nginx

# Depuis systemd
systemctl stop myservice    # envoie SIGTERM, puis SIGKILL après timeout
```

---

## Gérer SIGTERM dans un script

```bash
#!/bin/bash
cleanup() {
    echo "Reçu SIGTERM, nettoyage..."
    rm -f /tmp/lockfile
    exit 0
}

trap cleanup SIGTERM

while true; do
    sleep 1
done
```

---

> [!note]
> Si le processus ignore SIGTERM, utiliser [[SIGKILL]] (signal 9) qui ne peut pas être intercepté.
