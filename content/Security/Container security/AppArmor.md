---
title: AppArmor
tags:
  - security
  - advanced
---

# AppArmor

## Définition

AppArmor (Application Armor) est un module de sécurité [[Linux]] (LSM) qui confine les programmes en leur assignant des profils définissant leurs accès autorisés au système de fichiers, réseau et capabilities.

> [!tip] Pourquoi c'est important
> AppArmor ajoute une couche de défense en profondeur. Même si un attaquant compromet un conteneur, le profil AppArmor limite ce qu'il peut faire sur le système hôte.

## Gestion des profils

```bash
# Vérifier si AppArmor est actif
aa-status

# Charger un profil
apparmor_parser -r /etc/apparmor.d/docker-nginx

# Mettre un profil en mode complain (log sans bloquer)
aa-complain /etc/apparmor.d/docker-nginx

# Mettre en mode enforce
aa-enforce /etc/apparmor.d/docker-nginx
```

## Profil AppArmor pour conteneur

```
#include <tunables/global>

profile docker-nginx flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>

  network inet tcp,
  network inet udp,

  /usr/sbin/nginx mr,
  /etc/nginx/** r,
  /var/log/nginx/** w,
  /var/run/nginx.pid w,

  deny /proc/** w,
  deny @{HOME}/** w,
}
```

## Avec Docker

```bash
docker run --security-opt apparmor=docker-nginx nginx
```

## Liens

- [[Container security]]
- [[Seccomp]]
- [[Namespace isolation]]
