---
title: WireGuard
tags: [networking, intermediate]
---

# WireGuard

## Définition

WireGuard est un protocole VPN moderne, minimaliste (4000 lignes de code vs 600 000 pour OpenVPN), extrêmement rapide et sécurisé. Il est intégré au kernel Linux depuis la version 5.6.

> [!tip] Pourquoi WireGuard ?
> WireGuard est 3-4x plus rapide qu'OpenVPN, beaucoup plus simple à configurer, et sa petite base de code réduit la surface d'attaque. Il est devenu le standard moderne pour les VPNs.

## Installation et configuration

```bash
# Installer WireGuard
sudo apt install wireguard

# Générer les clés
wg genkey | tee /etc/wireguard/private.key | wg pubkey > /etc/wireguard/public.key
chmod 600 /etc/wireguard/private.key

PRIVATE=$(cat /etc/wireguard/private.key)
PUBLIC=$(cat /etc/wireguard/public.key)
```

## Configuration serveur

```ini
# /etc/wireguard/wg0.conf (serveur)
[Interface]
PrivateKey = <SERVER_PRIVATE_KEY>
Address = 10.8.0.1/24
ListenPort = 51820
PostUp   = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
PublicKey = <CLIENT_PUBLIC_KEY>
AllowedIPs = 10.8.0.2/32
```

## Configuration client

```ini
# /etc/wireguard/wg0.conf (client)
[Interface]
PrivateKey = <CLIENT_PRIVATE_KEY>
Address = 10.8.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = <SERVER_PUBLIC_KEY>
Endpoint = vpn.example.com:51820
AllowedIPs = 0.0.0.0/0  # Tout le trafic via VPN
PersistentKeepalive = 25
```

## Commandes

```bash
wg-quick up wg0             # Démarrer l'interface
wg-quick down wg0           # Arrêter
wg show                     # Statut et peers connectés
systemctl enable wg-quick@wg0  # Démarrer au boot
```

## Liens

- [[VPN]]
- [[OpenVPN]]
- [[Networking]]
