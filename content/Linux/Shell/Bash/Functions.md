---
title: Functions
tags:
  - intermediate
---

# Functions

---

## Définition

Les fonctions [[Bash]] permettent de regrouper du code réutilisable. Elles acceptent des arguments positionnels ($1, $2…) et peuvent retourner un code de sortie (0-255).

---

## Syntaxe

```bash
# Déclarer une fonction
ma_fonction() {
    echo "Bonjour depuis la fonction"
}

# Syntaxe alternative
function ma_fonction {
    echo "Bonjour"
}

# Appeler
ma_fonction

# Avec arguments
saluer() {
    local nom="$1"          # local : variable locale à la fonction
    local message="${2:-Bonjour}"
    echo "$message, $nom !"
}

saluer "Mohamed"            # Bonjour, Mohamed !
saluer "Mohamed" "Salut"    # Salut, Mohamed !
```

---

## Retourner des valeurs

```bash
# return = code de sortie (0-255), pas une valeur
verifier_port() {
    nc -z "$1" "$2" 2>/dev/null
    return $?   # 0 = ouvert, 1 = fermé
}

if verifier_port localhost 5432; then
    echo "PostgreSQL accessible"
fi

# Retourner une chaîne via echo + substitution
get_version() {
    echo "1.2.3"
}
VERSION=$(get_version)
```

---

## Exemple pratique

```bash
log() {
    local level="$1"
    local message="$2"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $message"
}

check_service() {
    local service="$1"
    if systemctl is-active --quiet "$service"; then
        log "INFO" "$service is running"
    else
        log "ERROR" "$service is NOT running"
        return 1
    fi
}

check_service nginx || exit 1
```
