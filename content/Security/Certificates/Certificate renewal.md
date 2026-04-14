---
title: Certificate renewal
tags: [security, intermediate]
---

# Certificate renewal

## Définition

Le renouvellement de certificat est le processus de remplacement d'un certificat expirant par un nouveau certificat valide, sans interruption de service.

> [!warning] Pourquoi c'est critique
> Un certificat expiré rend le service inaccessible (erreur navigateur). La plupart des incidents TLS sont dus à des oublis de renouvellement.

## Avec Certbot (Let's Encrypt)

```bash
# Renouvellement manuel
certbot renew

# Renouvellement automatique (cron)
0 3 * * * certbot renew --quiet --deploy-hook "systemctl reload nginx"

# Tester le renouvellement (dry-run)
certbot renew --dry-run

# Vérifier les certificats gérés
certbot certificates
```

## Avec cert-manager (Kubernetes)

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: example-cert
spec:
  secretName: example-tls
  duration: 2160h   # 90 jours
  renewBefore: 360h # Renouveler 15j avant
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  dnsNames:
    - example.com
```

## Surveiller les expirations

```bash
# Vérifier expiration d'un domaine en live
echo | openssl s_client -connect example.com:443 2>/dev/null   | openssl x509 -noout -dates

# Script d'alerte (jours restants)
openssl x509 -in cert.pem -noout -checkend 2592000   || echo "Expire dans moins de 30 jours!"
```

## Liens

- [[Certificates]]
- [[CA]]
- [[TLS]]
