---
title: Seccomp
tags:
  - security
  - advanced
---

# Seccomp (Secure Computing Mode)

## Définition

Seccomp filtre les appels système (syscalls) qu'un processus peut effectuer. Il permet de restreindre un conteneur aux seuls syscalls nécessaires à son fonctionnement.

> [!tip] Pourquoi c'est important
> Limiter les syscalls réduit drastiquement la surface d'attaque. Si un attaquant exploite une vulnérabilité, les syscalls bloqués l'empêchent d'escalader ses privilèges.

## Profil seccomp Docker par défaut

[[Docker]] applique automatiquement un profil seccomp qui bloque ~44 syscalls dangereux (ex: `ptrace`, `reboot`, `kexec_load`).

```bash
# Vérifier le profil actif
docker inspect container_name | grep -i seccomp

# Désactiver seccomp (déconseillé)
docker run --security-opt seccomp=unconfined nginx

# Profil personnalisé
docker run --security-opt seccomp=/path/to/profile.json nginx
```

## Structure d'un profil seccomp

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64"],
  "syscalls": [
    {
      "names": ["read", "write", "open", "close", "stat"],
      "action": "SCMP_ACT_ALLOW"
    },
    {
      "names": ["ptrace", "reboot"],
      "action": "SCMP_ACT_ERRNO"
    }
  ]
}
```

## Kubernetes

```yaml
securityContext:
  seccompProfile:
    type: RuntimeDefault  # Profil par défaut du runtime
```

## Liens

- [[Container security]]
- [[AppArmor]]
