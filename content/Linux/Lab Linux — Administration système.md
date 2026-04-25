---
title: "Lab Linux — Administration système"
tags:
  - linux
  - beginner
---

# Lab Linux — Administration système

## Objectif

Pratiquer les opérations d'administration Linux essentielles : gestion des utilisateurs, des [[Services]], des processus, des logs et du réseau.

> [!note] Prérequis
> - Une VM Linux (Ubuntu 22.04 recommandé) ou WSL2
> - Accès [[sudo]]

---

## Étape 1 — Exploration du système

```bash
# Infos système
uname -a
cat /etc/os-release
uptime
free -h
df -h

# CPU
nproc
lscpu | grep -E "Model name|CPU\(s\)|Thread"
```

**Vérification :** Tu dois voir le nombre de CPUs, la RAM disponible et l'espace disque.

---

## Étape 2 — Gestion des utilisateurs

```bash
# Créer un utilisateur
sudo useradd -m -s /bin/bash devuser
sudo passwd devuser

# Ajouter au groupe sudo
sudo usermod -aG sudo devuser

# Vérifier
id devuser
groups devuser
cat /etc/passwd | grep devuser
```

**Vérification :**

```bash
su - devuser
sudo whoami  # → root
exit
```

---

## Étape 3 — Gestion des services (systemd)

```bash
# Installer et gérer nginx
sudo apt update && sudo apt install -y nginx

sudo systemctl start nginx
sudo systemctl status nginx
sudo systemctl enable nginx

# Tester
curl -s http://localhost | grep "<title>"

# Stopper
sudo systemctl stop nginx
```

**Vérification :** `systemctl is-active nginx` doit retourner `active`.

---

## Étape 4 — Surveillance des processus

```bash
# Lancer un processus en arrière-plan
sleep 300 &
SLEEP_PID=$!
echo "PID: $SLEEP_PID"

# Trouver le processus
ps aux | grep sleep
pgrep sleep

# Voir sa consommation
top -p $SLEEP_PID -n 1 -b

# Tuer le processus
kill $SLEEP_PID
ps aux | grep sleep  # → ne doit plus apparaître
```

---

## Étape 5 — Analyse des logs

```bash
# Logs système
sudo journalctl -n 50
sudo journalctl -u nginx -f

# Logs kernel
sudo dmesg | tail -20
sudo dmesg | grep -i error

# Logs d'auth
sudo tail -f /var/log/auth.log

# Chercher les erreurs SSH
sudo grep "Failed password" /var/log/auth.log | tail -5
```

---

## Étape 6 — Réseau

```bash
# Interfaces réseau
ip addr show
ip route show

# Connexions actives
ss -tlnp

# Tester la connectivité
ping -c 3 8.8.8.8
curl -o /dev/null -s -w "%{http_code}\n" https://example.com

# DNS
dig google.com +short
nslookup google.com
```

---

## Étape 7 — Script de monitoring simple

```bash
cat > /tmp/monitor.sh << 'EOF'
#!/bin/bash
echo "=== Rapport système $(date) ==="
echo ""
echo "CPU : $(top -bn1 | grep 'Cpu(s)' | awk '{print $2}')% utilisé"
echo "RAM : $(free -h | awk '/^Mem:/ {print $3"/"$2}')"
echo "Disk: $(df -h / | awk 'NR==2 {print $3"/"$2" ("$5" used)"}')"
echo ""
echo "Top 3 processus CPU :"
ps aux --sort=-%cpu | awk 'NR<=4 {printf "%-15s %s%%\n", $11, $3}'
EOF

chmod +x /tmp/monitor.sh
/tmp/monitor.sh
```

---

## Vérification finale

- [ ] Utilisateur `devuser` créé avec droits sudo
- [ ] [[Nginx]] installé, démarré et activé au boot
- [ ] Logs [[journalctl]] lisibles
- [ ] Réseau opérationnel ([[ping]] + [[DNS]])
- [ ] Script de [[Monitoring]] fonctionne

## Liens

- [[Linux]]
- [[Shell]]
- [[Processes]]
- [[Logs]]
- [[SSH]]
