---
title: Capability dropping
tags:
  - advanced
---

# Capability dropping

## Parent
- [[Docker security]]

---

## Définition

Les Linux capabilities divisent les privilèges root en unités distinctes. Docker permet de supprimer des capabilities spécifiques (ou toutes) pour réduire la surface d'attaque d'un conteneur, même s'il tourne en root.

---

## Capabilities courantes

| Capability | Permet |
|---|---|
| `NET_ADMIN` | Modifier les interfaces réseau |
| `SYS_PTRACE` | Déboguer des processus |
| `SYS_ADMIN` | Appels système avancés |
| `CHOWN` | Changer les propriétaires de fichiers |
| `NET_BIND_SERVICE` | Écouter sur les ports < 1024 |

---

## Commandes

```bash
# Supprimer toutes les capabilities
docker run --cap-drop=ALL mon-app

# Supprimer toutes + ajouter seulement ce qui est nécessaire
docker run   --cap-drop=ALL   --cap-add=NET_BIND_SERVICE   mon-app

# Mode privilégié (⚠️ tout est autorisé)
docker run --privileged mon-app
```

---

## En Docker Compose

```yaml
services:
  api:
    image: mon-app
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
```

---

> [!warning]
> `--privileged` donne au conteneur un accès quasi-complet à l'hôte. Ne jamais l'utiliser en production sauf cas très spécifiques (Docker-in-Docker contrôlé).
