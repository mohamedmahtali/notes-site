---
title: Networking
tags:
  - intermediate
---

# Networking (Linux)

## Définition

Le réseau Linux couvre la configuration des interfaces réseau, l'adressage IP, le routage, et les outils de diagnostic. C'est une compétence fondamentale pour l'administration serveur et le DevOps.

## Interfaces réseau

```bash
# Voir toutes les interfaces et leurs IPs
ip addr show
ip addr show eth0         # interface spécifique

# État des interfaces (up/down)
ip link show
ip link set eth0 up       # activer
ip link set eth0 down     # désactiver

# Ajouter / supprimer une IP
ip addr add 192.168.1.10/24 dev eth0
ip addr del 192.168.1.10/24 dev eth0
```

## Routage

```bash
# Table de routage
ip route show

# Ajouter une route
ip route add 10.0.0.0/8 via 192.168.1.1 dev eth0   # route spécifique
ip route add default via 192.168.1.1                 # route par défaut

# Supprimer une route
ip route del default via 192.168.1.1

# Vérifier le chemin vers une destination
ip route get 8.8.8.8
```

## Ports et connexions actives

```bash
# Ports en écoute (remplace netstat)
ss -tlnp            # TCP listening, no resolve, avec PID
ss -ulnp            # UDP listening
ss -tlnp | grep :80 # chercher un port précis

# Connexions établies
ss -tnp             # TCP établies avec processus
ss -s               # statistiques réseau globales

# Rechercher quel processus utilise un port
ss -tlnp | grep :8080
lsof -i :8080       # alternative
```

## DNS — diagnostic

```bash
# Résolution DNS détaillée
dig example.com
dig example.com A           # enregistrement A uniquement
dig example.com MX          # enregistrements mail
dig @8.8.8.8 example.com   # via un resolver spécifique

# Résolution rapide
host example.com
nslookup example.com

# Fichiers de configuration DNS
cat /etc/resolv.conf        # resolver configuré
cat /etc/hosts              # overrides locaux
```

## Diagnostic de connectivité

```bash
# Ping — test de connectivité L3
ping 8.8.8.8
ping -c 4 google.com        # 4 paquets seulement

# Traceroute — chemin réseau hop par hop
traceroute 8.8.8.8
traceroute -T 8.8.8.8      # via TCP (utile si ICMP filtré)

# MTR — traceroute continu (meilleur outil)
mtr 8.8.8.8                 # interactif
mtr --report 8.8.8.8        # rapport en une passe

# Test HTTP complet
curl -v https://api.example.com
curl -I https://example.com                        # headers only
curl -w "%{time_total}" -o /dev/null https://...  # mesurer la latence
```

## Capture de trafic (tcpdump)

```bash
# Capturer sur une interface
tcpdump -i eth0

# Filtrer par port
tcpdump -i eth0 port 443
tcpdump -i eth0 port 80 or port 443

# Filtrer par host
tcpdump -i eth0 host 10.0.0.5

# Sauvegarder pour analyse dans Wireshark
tcpdump -i eth0 -w capture.pcap

# Voir le contenu ASCII (utile pour HTTP)
tcpdump -i eth0 -A port 80
```

## Tester des connexions réseau

```bash
# Tester si un port est ouvert (netcat)
nc -zv 10.0.0.5 5432        # -z = scan, -v = verbose
nc -zv -w 3 10.0.0.5 443    # timeout 3s

# Serveur TCP simple pour tester
nc -l 8080                   # écoute sur 8080
echo "test" | nc 10.0.0.5 8080  # envoyer depuis l'autre côté

# Test de bande passante
iperf3 -s                    # serveur
iperf3 -c 10.0.0.5          # client → mesure le débit
```

## Configuration persistante

```bash
# /etc/hosts — résolution locale (overrides DNS)
echo "10.0.0.5 mydb.internal" >> /etc/hosts

# /etc/resolv.conf — resolver DNS
nameserver 8.8.8.8
nameserver 8.8.4.4
search mycompany.internal    # suffixe DNS auto-ajouté
```

## Explorer

- **[[IP addressing]]** — adressage IPv4, CIDR, subnetting
- **[[Ports]]** — ports bien connus (22, 80, 443, 5432...)
- **[[Firewall]]** — iptables, ufw, filtrage du trafic
- **[[DNS]]** — résolution de noms, records A/CNAME/MX
- **[[SSH]]** — connexion sécurisée à distance
