---
title: Cheat sheet Linux
tags:
  - linux
  - beginner
---

# Cheat sheet Linux

## Navigation & fichiers

```bash
pwd                        # Répertoire courant
ls -lah                    # Liste détaillée + cachés + human-readable
cd -                       # Retour au répertoire précédent
find / -name "*.conf" 2>/dev/null   # Chercher un fichier
find . -type f -mtime -7   # Fichiers modifiés dans les 7 derniers jours
locate nginx.conf          # Chercher (base indexée)
tree -L 2                  # Arborescence sur 2 niveaux
```

## Manipulation de fichiers

```bash
cp -r src/ dest/           # Copier récursivement
mv old new                 # Déplacer/renommer
rm -rf dir/                # Supprimer récursivement (attention !)
ln -s /target /link        # Lien symbolique
chmod 755 script.sh        # Permissions (rwxr-xr-x)
chmod +x script.sh         # Rendre exécutable
chown user:group file      # Changer propriétaire
```

## Contenu de fichiers

```bash
cat file.txt               # Afficher tout
less file.txt              # Afficher avec pagination
head -n 20 file.txt        # 20 premières lignes
tail -f /var/log/syslog    # Suivre en temps réel
grep -rn "pattern" dir/    # Chercher dans les fichiers (récursif + n° ligne)
grep -v "pattern" file     # Lignes NE contenant PAS le pattern
sed -i 's/old/new/g' file  # Remplacer dans le fichier
awk '{print $1}' file      # Afficher la 1re colonne
wc -l file                 # Compter les lignes
```

## Processus

```bash
ps aux                     # Tous les processus
ps aux | grep nginx        # Chercher un processus
top / htop                 # Moniteur temps réel
kill -9 PID                # Tuer un processus (force)
killall nginx              # Tuer par nom
nohup ./script.sh &        # Exécuter en arrière-plan persistant
jobs                       # Lister les jobs en arrière-plan
fg %1                      # Ramener job 1 au premier plan
```

## Réseau

```bash
ip addr                    # Interfaces réseau
ip route                   # Table de routage
ss -tlnp                   # Ports en écoute
curl -I https://example.com  # En-têtes HTTP
wget -O file.zip https://...  # Télécharger
ping -c 4 8.8.8.8          # Test connectivité
traceroute google.com      # Tracer la route
dig example.com            # Résolution DNS
nmap -p 22,80,443 host     # Scanner des ports
```

## Permissions

```bash
# Format : user | group | other
chmod 644 file    # rw-r--r--  (fichier standard)
chmod 755 dir/    # rwxr-xr-x  (dossier/script)
chmod 600 key.pem # rw-------  (clé privée SSH)
chmod 777 file    # rwxrwxrwx  (jamais en prod)

# Permissions spéciales
chmod u+s binary  # SetUID — s'exécute en tant que owner
chmod g+s dir/    # SetGID — hérite du groupe parent
chmod +t /tmp     # Sticky bit — seul le owner peut supprimer
```

## Disque & stockage

```bash
df -h                      # Espace disque par partition
du -sh dir/                # Taille d'un répertoire
du -sh * | sort -hr        # Trier par taille
lsblk                      # Périphériques bloc
mount /dev/sdb1 /mnt       # Monter une partition
umount /mnt                # Démonter
```

## Systemd

```bash
systemctl status nginx
systemctl start/stop/restart nginx
systemctl enable/disable nginx      # Au démarrage
systemctl list-units --type=service
journalctl -u nginx -f              # Logs en temps réel
journalctl --since "1 hour ago"
```

## SSH

```bash
ssh user@host
ssh -i ~/.ssh/id_rsa user@host
ssh -p 2222 user@host
ssh -L 8080:localhost:80 user@host  # Tunnel local
scp file.txt user@host:/tmp/        # Copier vers remote
scp -r user@host:/data/ ./local/    # Copier depuis remote
rsync -avz src/ user@host:/dest/    # Sync avec compression
```

## Liens

- [[Linux]]
- [[Shell]]
- [[SSH]]
- [[Networking]]
- [[Processes]]
