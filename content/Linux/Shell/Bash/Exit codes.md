---
title: Exit codes
tags:
  - beginner
---

# Exit codes

## Parent
- [[Bash]]

---

## Définition

Chaque commande Linux retourne un code de sortie (exit code) entre 0 et 255. **0 = succès**, toute autre valeur = erreur. Les scripts CI/CD et les outils de monitoring se basent sur ces codes pour détecter les échecs.

---

## Codes courants

| Code | Signification |
|---|---|
| `0` | Succès |
| `1` | Erreur générique |
| `2` | Mauvaise utilisation de la commande |
| `126` | Commande trouvée mais non exécutable |
| `127` | Commande introuvable |
| `128+N` | Terminé par le signal N (ex: 130 = Ctrl+C) |
| `130` | SIGINT (Ctrl+C) |
| `137` | SIGKILL (kill -9) |

---

## Utilisation

```bash
# Vérifier le code de la dernière commande
ls /existe
echo "$?"   # 0

ls /noexiste
echo "$?"   # 2

# Tester dans un script
if ! commande; then
    echo "Échec !" >&2
    exit 1
fi

# Chaîner avec && et ||
deploy.sh && notify_success || notify_failure

# set -e : arrêt automatique sur erreur
set -e
commande_qui_echoue  # le script s'arrête ici
commande_suivante    # jamais exécutée
```

---

## Codes personnalisés

```bash
# Convention : 0=OK, 1=erreur, 2=mauvais usage, 3+=erreur spécifique
ERROR_CONFIG_MISSING=2
ERROR_DB_DOWN=3

if [[ ! -f config.yaml ]]; then
    echo "Config manquante" >&2
    exit $ERROR_CONFIG_MISSING
fi
```
