---
title: Runtime security
tags:
  - security
  - advanced
---

# Runtime security

## Définition

La sécurité runtime surveille et protège les conteneurs pendant leur exécution. Elle détecte les comportements anormaux (appels système suspects, connexions réseau inattendues) en temps réel.

> [!tip] Pourquoi c'est important
> Les scanners d'images vérifient avant le déploiement, mais la runtime [[Security]] protège contre les attaques qui surviennent après. Elle est essentielle pour la détection d'intrusion.

## Falco

```yaml
# Règle Falco : détecter un shell dans un conteneur
- rule: Terminal shell in container
  desc: A shell was spawned in a container
  condition: >
    container.id != host
    and proc.name in (shell_binaries)
    and evt.type = execve
  output: >
    Shell spawned in container
    (user=%user.name container=%container.name
     image=%container.image.repository
     cmd=%proc.cmdline)
  priority: WARNING
```

```bash
# Installer Falco
helm install falco falcosecurity/falco   --set falco.jsonOutput=true

# Voir les alertes en direct
kubectl logs -n falco -l app=falco -f
```

## Outils de runtime security

| Outil | Approche |
|-------|---------|
| Falco | Règles syscalls/[[Kernel]] |
| Tetragon (Cilium) | eBPF, observabilité kernel |
| Sysdig | Forensics + détection |
| Aqua Security | Plateforme complète |

## Liens

- [[Container security]]
- [[AppArmor]]
- [[Seccomp]]
- [[Image scanning]]
