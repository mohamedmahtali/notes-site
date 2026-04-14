---
title: Port forwarding
tags:
  - intermediate
---

# Port forwarding

## Parent
- [[SSH]]

---

## Définition

Le port forwarding SSH crée un tunnel crypté qui redirige le trafic d'un port local vers un port distant (ou l'inverse). Permet d'accéder à des services non exposés publiquement comme si ils étaient locaux.

---

## Local forwarding (-L)

Redirige un port local vers un service distant via le serveur SSH.

```bash
# Accéder à une DB distante sur le port local 5433
ssh -L 5433:localhost:5432 user@serveur

# Se connecter ensuite
psql -h localhost -p 5433 -U app mydb

# Via un bastion vers un serveur interne
ssh -L 8080:internal-api:80 user@bastion
```

---

## Remote forwarding (-R)

Expose un service local sur un port du serveur distant.

```bash
# Exposer un serveur local (port 3000) sur le port 8080 du serveur
ssh -R 8080:localhost:3000 user@serveur
# → les visiteurs du serveur:8080 voient ton localhost:3000
```

---

## Dynamic forwarding (-D) – proxy SOCKS

```bash
# Créer un proxy SOCKS5 sur le port local 1080
ssh -D 1080 user@serveur
# → configurer le navigateur/application pour utiliser SOCKS5 localhost:1080
```

---

## Tunnel persistant

```bash
# Tunnel en arrière-plan, auto-reconnexion
autossh -M 0 -f -N -L 5433:db:5432 user@bastion
```
