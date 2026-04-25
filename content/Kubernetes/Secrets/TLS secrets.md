---
title: TLS secrets
tags:
  - intermediate
---
# TLS secrets

---

## Définition

Les [[TLS]] [[Secrets]] stockent les certificats et clés privées pour HTTPS. Ils sont utilisés par les [[Ingress]] controllers pour la terminaison SSL et peuvent être référencés dans les objets Ingress.

---

## Créer un TLS secret

```bash
# Depuis des fichiers existants
kubectl create secret tls myapp-tls   --cert=./fullchain.pem   --key=./privkey.pem   --namespace=production

# Ou en YAML
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Secret
metadata:
  name: myapp-tls
  namespace: production
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded-cert>
  tls.key: <base64-encoded-key>
EOF
```

---

## Utiliser dans un Ingress

```yaml
spec:
  tls:
  - hosts:
    - myapp.com
    - www.myapp.com
    secretName: myapp-tls       # le TLS secret
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
```

---

## Let's Encrypt avec cert-manager

```yaml
# cert-manager crée et renouvelle automatiquement les certificats
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: myapp-cert
spec:
  secretName: myapp-tls
  dnsNames: [myapp.com]
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
```
