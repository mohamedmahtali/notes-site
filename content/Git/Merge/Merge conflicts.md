---
title: Merge conflicts
tags:
  - intermediate
---

# Merge conflicts

## Parent
- [[Merge]]

## Concepts liés
- [[Merge]]
- [[Rebase]]
- [[Code review]]

---

## Définition

Un conflit de merge survient quand Git ne peut pas fusionner automatiquement deux branches parce que **les deux ont modifié le même endroit dans un même fichier**. Git marque les zones conflictuelles et demande à l'utilisateur de décider quelle version conserver.

---

## Pourquoi ça arrive

```
main :     A → B → C
                     \
feature :  A → B → D  ← même ligne modifiée dans C et D
```

Quand on merge `feature` dans `main`, Git voit deux versions différentes de la même ligne et ne sait pas laquelle choisir.

---

## Reconnaître un conflit

Après un `git merge` ou `git pull` conflictuel :

```bash
$ git merge feature/auth
Auto-merging src/config.js
CONFLICT (content): Merge conflict in src/config.js
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   src/config.js
```

---

## Lire les marqueurs de conflit

```js
<<<<<<< HEAD
const timeout = 3000;   // ← version de main (ta branche actuelle)
=======
const timeout = 5000;   // ← version de feature/auth
>>>>>>> feature/auth
```

| Marqueur | Signification |
|---|---|
| `<<<<<<< HEAD` | Début de ta version (branche actuelle) |
| `=======` | Séparateur entre les deux versions |
| `>>>>>>> branche` | Fin de la version entrante |

---

## Résoudre un conflit

**Étape 1** — Ouvrir le fichier en conflit et choisir :

```js
// Option A : garder ta version
const timeout = 3000;

// Option B : garder la version entrante
const timeout = 5000;

// Option C : fusionner manuellement
const timeout = process.env.TIMEOUT ?? 5000;
```

**Étape 2** — Supprimer tous les marqueurs (`<<<<<<<`, `=======`, `>>>>>>>`)

**Étape 3** — Marquer le conflit comme résolu et committer :

```bash
git add src/config.js
git commit -m "fix: resolve merge conflict on timeout config"
```

---

## Outils visuels

```bash
# Outil de merge intégré à Git
git mergetool

# VS Code (recommandé pour débutants)
# Les conflits sont mis en surbrillance avec des boutons :
# "Accept Current" | "Accept Incoming" | "Accept Both"
```

---

## Prévenir les conflits

> [!tip] Bonnes pratiques
> - **Puller souvent** : `git pull origin main` régulièrement pour rester à jour
> - **Branches courtes** : moins une branche vit longtemps, moins elle diverge
> - **Petits commits** : des changements ciblés conflictent moins souvent
> - **Communiquer** : si deux personnes touchent au même fichier, se coordonner

> [!warning] Ne jamais forcer un merge sans comprendre
> Un `git merge --abort` annule le merge en cours et remet le dépôt dans son état précédent. Utilise-le si tu es bloqué.

```bash
# Annuler le merge et repartir de l'état précédent
git merge --abort
```
