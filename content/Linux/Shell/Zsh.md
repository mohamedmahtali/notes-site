---
title: Zsh
tags:
  - intermediate
---

# Zsh

## Parent
- [[Shell]]

---

## Définition

Zsh (Z Shell) est un shell puissant et configurable, compatible POSIX, avec des fonctionnalités avancées d'autocomplétion, de correction d'erreurs, et de personnalisation. C'est le shell par défaut sur macOS depuis Catalina.

---

## Installation et configuration

```bash
# Installer Zsh
apt-get install zsh   # Debian/Ubuntu
brew install zsh      # macOS

# Définir comme shell par défaut
chsh -s $(which zsh)

# Fichier de configuration
~/.zshrc
```

---

## oh-my-zsh (framework populaire)

```bash
# Installer
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Changer le thème dans ~/.zshrc
ZSH_THEME="agnoster"   # ou "robbyrussell", "powerlevel10k"

# Activer des plugins
plugins=(git docker kubectl terraform aws)
```

---

## Fonctionnalités utiles

```bash
# Autocomplétion avancée (Tab)
git <Tab>    # liste les sous-commandes
kubectl <Tab> # complète les ressources

# Navigation dans l'historique
Ctrl+R        # recherche dans l'historique
history | grep "docker"

# Glob patterns avancés
ls **/*.log    # récursif
ls ^*.log      # tous sauf .log

# Aliases utiles à ajouter dans ~/.zshrc
alias ll='ls -la'
alias k='kubectl'
alias dc='docker compose'
```
