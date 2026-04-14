---
title: Loops
tags:
  - intermediate
---
# Loops

## Parent
- [[Bash]]

---

## Définition

Les boucles Bash permettent de répéter des commandes sur une séquence de valeurs, tant qu'une condition est vraie, ou indéfiniment avec contrôle manuel. Les trois types principaux : `for`, `while`, et `until`.

---

## for loop

```bash
# Itérer sur une liste
for fruit in apple banana cherry; do
    echo "Fruit: $fruit"
done

# Itérer sur des fichiers
for file in /etc/*.conf; do
    echo "Config: $file"
done

# Boucle C-style
for ((i=0; i<10; i++)); do
    echo "i=$i"
done

# Itérer sur la sortie d'une commande
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "User: $user"
done
```

---

## while loop

```bash
# Tant que la condition est vraie
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Lire un fichier ligne par ligne
while IFS= read -r line; do
    echo "Line: $line"
done < /etc/hosts

# Boucle infinie avec break
while true; do
    read -p "Continuer? [y/n]: " answer
    [ "$answer" = "n" ] && break
done
```

---

## Contrôle de flux

```bash
for i in {1..10}; do
    [ $i -eq 5 ] && continue    # sauter l'itération 5
    [ $i -eq 8 ] && break       # arrêter à 8
    echo $i
done
```

---

> [!tip]
> Pour traiter des fichiers avec des espaces dans les noms, toujours utiliser `while IFS= read -r line` plutôt que `for line in $(cat file)`.
