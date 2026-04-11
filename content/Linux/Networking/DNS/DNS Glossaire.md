---
tags:
  - advanced
---
### DNS Glossaire

## Parent
- [[DNS]]

## 1️⃣ Architecture & hiérarchie

- **DNS (Domain Name System)** : système de résolution qui associe un nom de domaine à une adresse IP.
- **Nom de domaine** : nom lisible par l’humain (ex : `www.example.com`).
- **FQDN (Fully Qualified Domain Name)** : nom complet d’un hôte (ex : `www.example.com.`).
- **Racine (root)** : sommet de la hiérarchie DNS, représentée par `.`.
- **Serveur root** : serveur qui connaît les serveurs des TLD.
- **TLD (Top Level Domain)** : domaine de premier niveau (`.com`, `.org`, `.fr`…).
- **ccTLD** : TLD de pays (`.fr`, `.dz`, `.uk`…).
- **gTLD** : TLD générique (`.com`, `.net`, `.org`…).
- **Domaine** : ensemble de sous-domaines gérés sous un même nom.
- **Sous-domaine** : subdivision d’un domaine (`mail.example.com`).
- **Zone DNS** : portion de l’espace DNS gérée par un serveur autoritatif.
- **Délégation** : fait de confier la gestion d’une zone à un autre serveur DNS.
- **Hiérarchie DNS** : organisation en arbre (root → TLD → domaine → sous-domaine).

---

## 2️⃣ Types de serveurs DNS

- **Client DNS** : machine qui fait une requête DNS.
- **Résolveur DNS (resolver)** : serveur qui effectue la résolution complète.
- **Serveur DNS récursif** : accepte les requêtes récursives des clients.
- **Serveur DNS itératif** : répond par délégation si nécessaire.
- **Serveur autoritatif** : serveur qui détient la zone DNS officielle.
- **Serveur primaire (master)** : serveur principal d’une zone.
- **Serveur secondaire (slave)** : copie d’une zone DNS.
- **Forwarder DNS** : serveur qui relaie les requêtes à un autre serveur.
- **Cache DNS** : mémoire temporaire des réponses DNS.
- **Serveur de noms (nameserver)** : serveur DNS responsable d’un domaine.

---

## 3️⃣ Types de requêtes & réponses

- **Requête DNS** : demande d’information DNS.
- **Requête récursive** : le serveur doit fournir la réponse finale.
- **Requête itérative** : le serveur donne une piste (délégation).
- **Réponse DNS** : message retourné par un serveur DNS.
- **Réponse autoritative** : réponse venant du serveur officiel du domaine.
- **Réponse non autoritative** : réponse venant du cache.
- **Délégation (referral)** : réponse indiquant un autre serveur à contacter.
- **NXDOMAIN** : domaine inexistant.
- **Timeout** : absence de réponse.
- **TTL (Time To Live)** : durée de validité d’un enregistrement en cache.

---

## 4️⃣ Enregistrements DNS (Resource Records)

- **RR (Resource Record)** : entrée DNS individuelle.
- **A** : associe un nom à une IPv4.
- **AAAA** : associe un nom à une IPv6.
- **CNAME** : alias vers un autre nom.
- **MX** : serveur de mail.
- **NS** : serveur de noms d’un domaine.
- **SOA (Start of Authority)** : enregistrement principal d’une zone.
- **TXT** : texte libre (SPF, DKIM, etc.).
- **PTR** : résolution inverse (IP → nom).
- **SRV** : service spécifique (port + serveur).
- **CAA** : autorités de certification autorisées.
- **DS** : lien DNSSEC entre zones.
- **DNSKEY** : clé DNSSEC.
- **RRSIG** : signature DNSSEC.
- **NSEC / NSEC3** : preuve d’inexistence DNSSEC.

---

## 5️⃣ Fichiers & configuration

- **Fichier de zone** : fichier contenant les enregistrements DNS.
- **Serial (SOA)** : numéro de version de la zone.
- **Refresh / Retry / Expire** : paramètres de synchronisation.
- **AXFR** : transfert complet de zone.
- **IXFR** : transfert incrémental.
- **Bind** : serveur DNS très utilisé sous Linux.
- **named** : processus Bind.
- **Zone directe** : nom → IP.
- **Zone inverse** : IP → nom.
- **in-addr.arpa** : domaine pour IPv4 inverse.
- **ip6.arpa** : domaine pour IPv6 inverse.

---

## 6️⃣ Sécurité DNS

- **DNSSEC** : système de signature cryptographique DNS.
- **Empoisonnement de cache (cache poisoning)** : falsification de réponses DNS.
- **Spoofing DNS** : usurpation de réponse DNS.
- **Attaque par amplification DNS** : attaque DDoS utilisant DNS.
- **Blackhole DNS** : blocage de domaines.
- **Split DNS** : réponses différentes interne/externe.
- **View DNS** : vues différentes selon le client.
- **Zone signing** : signature DNSSEC d’une zone.

---

## 7️⃣ Protocoles & ports

- **UDP 53** : port DNS par défaut.
- **TCP 53** : utilisé pour gros messages et transferts de zone.
- **DoT (DNS over TLS)** : DNS chiffré via TLS.
- **DoH (DNS over HTTPS)** : DNS via HTTPS.
- **EDNS(0)** : extension du protocole DNS.

---

## 8️⃣ Outils & commandes

- **dig** : outil de requête DNS.
- **nslookup** : ancien outil DNS.
- **host** : outil simple DNS.
- **whois** : info registre domaine.
- **resolv.conf** : configuration client DNS.
- **systemd-resolved** : résolveur Linux.
- **flush DNS** : vider le cache DNS.