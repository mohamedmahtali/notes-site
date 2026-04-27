---
title: Certificates
tags:
  - security
  - intermediate
---

# Certificates

## Définition

Un certificat numérique est un fichier électronique qui lie une clé publique à une identité (domaine, organisation, personne). Il est signé par une autorité de certification (CA) pour garantir son authenticité. Ils sont la base du chiffrement [[TLS]]/HTTPS.

## Chaîne de confiance

```
Root CA (intégré dans le navigateur/OS)
  └── Intermediate CA (signé par Root)
        └── Leaf certificate (signé par Intermediate)
              └── example.com

Navigateur → vérifie leaf → remonte la chaîne → Root CA → confiance établie
```

Le Root CA ne signe jamais directement les certificats de domaine (compromission trop critique). L'Intermediate CA est révocable sans impacter le Root.

## Structure d'un certificat X.509

```
Subject:         CN=example.com, O=My Org, C=FR
Issuer:          CN=Let's Encrypt R3
Validity:        2024-01-01 → 2024-04-01 (90 jours)
Public Key:      RSA 2048 bits
SANs:            DNS:example.com, DNS:www.example.com
Signature:       SHA256withRSA
```

Le champ **SAN (Subject Alternative Names)** permet à un seul certificat de couvrir plusieurs domaines ou sous-domaines (wildcard `*.example.com`).

## Types de certificats

| Type | Validation | Délai | Usage |
|------|------------|-------|-------|
| DV (Domain Validation) | Contrôle du domaine uniquement | Minutes | Sites web standards |
| OV (Organization Validation) | + vérification de l'organisation | Jours | Sites corporate |
| EV (Extended Validation) | + vérification légale approfondie | Semaines | Banques, e-commerce |
| Wildcard | *.domain.com | Minutes | Sous-domaines multiples |
| Self-signed | Signé par soi-même | Immédiat | Dev/test, Kubernetes interne |

## Commandes openssl essentielles

```bash
# Afficher un certificat
openssl x509 -in cert.pem -text -noout

# Vérifier la date d'expiration
openssl x509 -in cert.pem -noout -dates

# Tester un certificat en live (vérifier la chaîne)
openssl s_client -connect example.com:443 -showcerts

# Vérifier la chaîne de certification
openssl verify -CAfile ca-bundle.pem cert.pem

# Générer une clé privée + CSR
openssl req -newkey rsa:2048 -keyout server.key -out server.csr \
  -subj "/CN=example.com/O=My Org/C=FR"

# Créer un certificat self-signed (dev uniquement)
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 365 -nodes -subj "/CN=localhost"
```

## Let's Encrypt — certificats gratuits automatisés

```bash
# Installer certbot
apt install certbot python3-certbot-nginx

# Obtenir et installer un certificat (nginx)
certbot --nginx -d example.com -d www.example.com

# Renouvellement automatique (cron / systemd timer)
certbot renew --dry-run

# Vérifier les certificats gérés
certbot certificates
```

Let's Encrypt émet des certificats DV valables 90 jours. Le renouvellement automatique est prévu dès 30 jours avant expiration.

## cert-manager — certificats dans Kubernetes

```yaml
# Installer cert-manager
helm repo add jetstack https://charts.jetstack.io
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager --create-namespace \
  --set installCRDs=true

# ClusterIssuer Let's Encrypt
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01:
          ingress:
            class: nginx
---
# Certificate automatique pour un Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
    - hosts: [example.com]
      secretName: example-com-tls   # cert-manager crée ce Secret
```

## Explorer

- **[[TLS]]** — protocole de chiffrement, handshake, versions TLS 1.2/1.3
- **[[CA]]** — autorités de certification, Root CA vs Intermediate
- **[[CSR]]** — Certificate Signing Request, processus de demande
- **[[Certificate renewal]]** — renouvellement automatique, alertes d'expiration
- **[[Self signed certificate]]** — usage en dev et en interne Kubernetes
