---
title: PAM
tags:
  - advanced
---

# PAM

---

## Définition

PAM (Pluggable Authentication [[Modules]]) est un framework qui abstrait l'authentification sur [[Linux]]. Les applications ([[SSH]], [[sudo]], login) délèguent l'authentification à PAM, qui applique des règles configurables : mots de passe, clés, LDAP, 2FA, etc.

---

## Fichiers de configuration

```bash
/etc/pam.d/          # configuration PAM par service
/etc/pam.d/sshd      # PAM pour SSH
/etc/pam.d/sudo      # PAM pour sudo
/etc/pam.d/login     # PAM pour le login console
/etc/pam.d/common-auth  # règles d'auth communes (Debian)
```

---

## Structure d'une règle PAM

```
type  control  module  [options]

auth    required   pam_unix.so         # vérification mot de passe Unix
auth    optional   pam_google_auth.so  # 2FA Google Authenticator
account required   pam_permit.so
session required   pam_limits.so
```

---

## Cas d'usage courants

```bash
# Limites de ressources (/etc/security/limits.conf)
# Via pam_limits.so dans /etc/pam.d/common-session

# /etc/security/limits.conf
*       soft    nofile   65536
*       hard    nofile   65536
appuser soft    nproc    1000

# Politique de mots de passe
apt-get install libpam-pwquality

# /etc/security/pwquality.conf
minlen = 12
dcredit = -1    # au moins 1 chiffre
ucredit = -1    # au moins 1 majuscule
```

---

> [!note]
> PAM est rarement modifié directement sauf pour des besoins avancés (2FA, LDAP, politiques de mots de passe). La plupart des distributions ont des configurations PAM fonctionnelles par défaut.
