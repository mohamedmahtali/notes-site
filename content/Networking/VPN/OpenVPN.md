---
title: OpenVPN
tags:
  - networking
  - intermediate
---

# OpenVPN

## Définition

OpenVPN est un VPN open-source mature utilisant TLS pour chiffrer les communications. Il est très compatible (fonctionne sur tous les OS, traverse les [[Firewall]] via UDP/TCP sur n'importe quel port).

> [!note] OpenVPN vs WireGuard
> OpenVPN est plus établi et compatible, mais WireGuard est plus rapide et simple. Pour les nouveaux déploiements, WireGuard est souvent préféré. OpenVPN reste pertinent pour les environnements legacy et certaines entreprises.

## Installation rapide (serveur)

```bash
# Script auto-install (pour les tests)
wget https://git.io/vpn -O openvpn-install.sh
bash openvpn-install.sh

# Installation manuelle
sudo apt install openvpn easy-rsa
```

## Structure de configuration

```
# Serveur (/etc/openvpn/server.conf)
port 1194
proto udp
dev tun
ca /etc/openvpn/ca.crt
cert /etc/openvpn/server.crt
key /etc/openvpn/server.key
dh /etc/openvpn/dh.pem
server 10.8.0.0 255.255.255.0
push "redirect-gateway def1"
push "dhcp-option DNS 8.8.8.8"
keepalive 10 120
cipher AES-256-GCM
```

## Commandes

```bash
systemctl start openvpn@server
systemctl status openvpn@server
openvpn --config client.ovpn    # Connexion client
```

## Liens

- [[VPN]]
- [[WireGuard]]
- [[TLS]]
- [[Networking]]
