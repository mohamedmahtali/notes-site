---
title: VPN
tags:
  - networking
  - intermediate
---

# VPN (Virtual Private Network)

## Définition

Un VPN crée un tunnel chiffré entre deux points sur un réseau public (Internet). Il est utilisé pour sécuriser l'accès aux ressources internes, relier des sites distants, ou protéger des communications.

> [!tip] VPN en [[DevOps]]
> Les VPNs sont utilisés pour accéder aux environnements de production (bastion + VPN), connecter des [[Cloud]] privés à l'on-premise (site-to-site VPN), et sécuriser les communications inter-datacenter.

## Types de VPN

| Type | Usage | Exemple |
|------|-------|---------|
| Remote access | Accès utilisateurs individuels | WireGuard, OpenVPN client |
| Site-to-site | Relier deux réseaux | [[AWS]] VPN, IPSec |
| Mesh | Tous les noeuds connectés entre eux | WireGuard mesh, Tailscale |

## Protocoles

| Protocole | Avantages | Inconvénients |
|-----------|-----------|---------------|
| WireGuard | Très rapide, simple, moderne | Récent (moins de support legacy) |
| OpenVPN | Mature, très compatible | Complexe à configurer |
| IPSec | Standard enterprise, natif OS | Configuration complexe |
| L2TP/PPTP | Ancien standard | Obsolète, non sécurisé |

## WireGuard — démarrage rapide

```bash
# Installation (Ubuntu)
apt install wireguard

# Générer une paire de clés
wg genkey | tee privatekey | wg pubkey > publickey

# /etc/wireguard/wg0.conf — côté serveur
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = <PRIVATE_KEY_SERVEUR>

[Peer]
PublicKey = <PUBLIC_KEY_CLIENT>
AllowedIPs = 10.0.0.2/32

# Démarrer le tunnel
systemctl enable --now wg-quick@wg0
```

```bash
# /etc/wireguard/wg0.conf — côté client
[Interface]
Address = 10.0.0.2/24
PrivateKey = <PRIVATE_KEY_CLIENT>

[Peer]
PublicKey = <PUBLIC_KEY_SERVEUR>
Endpoint = <IP_SERVEUR>:51820
AllowedIPs = 10.0.0.0/24   # Seulement le réseau VPN
# AllowedIPs = 0.0.0.0/0   # Tout le trafic passe par le VPN
PersistentKeepalive = 25
```

## VPN Site-to-site (Cloud)

Connecte un réseau on-premise à un [[VPC]] cloud.

```
On-premise                    Cloud (AWS/Azure/GCP)
  ┌──────────┐    IPSec     ┌──────────┐
  │ Routeur  │◄────────────►│ VPN GW   │
  │ 192.168  │   tunnel     │  VPC     │
  └──────────┘              └──────────┘
```

| Provider | Service | Protocole |
|----------|---------|-----------|
| AWS | Site-to-Site VPN | IPSec IKEv2 |
| [[Azure]] | VPN [[Gateway]] | IPSec / OpenVPN |
| GCP | Cloud VPN | IPSec IKEv2 |

> [!tip] Alternatives modernes
> **Tailscale** et **Cloudflare Tunnel** simplifient drastiquement la mise en place d'un mesh VPN sans exposer de port public. Idéal pour les équipes DevOps qui accèdent aux environnements de dev/[[Staging]].

## Bonnes pratiques DevOps

- Toujours passer par un VPN pour accéder aux environnements de production (pas de [[SSH]] direct)
- Préférer des accès par rôle (VPN + [[RBAC]]) plutôt qu'un tunnel "tout-en-un"
- Activer le [[Logging]] des connexions VPN pour l'audit
- Utiliser un `AllowedIPs` restrictif (split tunneling) pour ne pas router tout le trafic

## Liens

- [[WireGuard]]
- [[OpenVPN]]
- [[Networking]]
