---
title: Handlers
tags:
  - intermediate
---
# Handlers

---

## Définition

Les handlers sont des [[Tasks]] spéciales déclenchées par `notify`. Ils s'exécutent une seule fois à la fin du playbook, même si plusieurs tasks les ont notifiés. Utilisés pour les redémarrages de [[Services]] après une modification de configuration.

---

## Exemple

```yaml
# tasks/main.yml
tasks:
  - name: Deploy nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Reload nginx     # notifie le handler si changement

  - name: Update SSL cert
    copy:
      src: cert.pem
      dest: /etc/ssl/cert.pem
    notify:
      - Reload nginx          # le handler ne tourne qu'une fois
      - Notify monitoring

# handlers/main.yml
handlers:
  - name: Reload nginx
    service:
      name: nginx
      state: reloaded         # reload (pas restart — 0 downtime)

  - name: Restart nginx
    service:
      name: nginx
      state: restarted

  - name: Notify monitoring
    uri:
      url: "https://monitoring.mycompany.com/deployments"
      method: POST
      body_format: json
      body: '{"service":"nginx","action":"reload"}'
```

---

## Forcer l'exécution des handlers

```bash
# Les handlers tournent en fin de play normalement
# Pour les forcer immédiatement dans le play :
- meta: flush_handlers
```

---

> [!tip]
> Utiliser `state: reloaded` plutôt que `restarted` pour [[Nginx]] — il recharge la configuration sans couper les connexions existantes (zero-downtime config update).
