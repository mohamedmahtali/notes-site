### Parent
- [[DNS]]

Le **DNS (Domain Name System)** est un système distribué qui traduit des **noms de domaine** (ex: `example.com`) en **adresses IP**. Les implémentations DNS sont des **logiciels serveur** qui réalisent différentes fonctions : **serveur autoritatif**, **résolveur récursif**, **cache DNS**, **forwarder**, etc.  
Les logiciels que tu cites représentent différentes approches selon les besoins (infrastructure Internet, réseau local, cloud, conteneurs…).

## 1. BIND (Berkeley Internet Name Domain)

![[Pasted image 20260307232856.png|697]]

![[Pasted image 20260308002705.png]]

![[Pasted image 20260308002801.png]]

**BIND** est l’implémentation DNS **historique et la plus répandue** sur Internet.

**Caractéristiques techniques :**
- Développé initialement à **UC Berkeley**
- Maintenu aujourd’hui par **ISC (Internet Systems Consortium)**
- Peut fonctionner comme :
	- **serveur autoritatif**
    - **résolveur récursif**
    - **cache DNS**

**Architecture :**
- processus principal : `named`
- fichiers de configuration :
    - `named.conf`
    - fichiers de **zones DNS**

Exemple de zone :

```bash
zone "example.com" {  
    type master;  
    file "/etc/bind/db.example.com";  
};
```


Exemple d’enregistrement :
```bash
www     IN  A   192.168.1.10  
mail    IN  MX  10 mail.example.com.
```

**Points forts**
- extrêmement complet
- support DNSSEC
- très configurable

**Inconvénients**
- configuration lourde
- surface d’attaque plus grande
- complexité opérationnelle

**Usage typique**
- infrastructures DNS publiques
- registres de domaine
- serveurs autoritatifs Internet

---

## 2. Unbound

![[Pasted image 20260308003052.png|555]]![[Pasted image 20260308003100.png|556]]
![[Pasted image 20260308003109.png|561]]
![[Pasted image 20260308003118.png|564]]


**Unbound** est un **résolveur récursif DNS moderne**.

Développé par **NLnet Labs** (organisation derrière **NSD**).

**Rôle principal :**
- **résolution récursive**
- **validation DNSSEC**
- **cache DNS performant**

**Fonctionnement**
Quand un client demande `example.com` :
1. le résolveur interroge un **root server**
2. puis un **TLD server (.com)**
3. puis le **serveur autoritatif**
4. stocke la réponse en **cache**

**Configuration simple**
server:  
  interface: 0.0.0.0  
  access-control: 192.168.1.0/24 allow

**Points forts**
- très **sécurisé**
- **DNSSEC par défaut**
- **performances élevées**
- code plus simple que BIND

**Usage typique**
- résolveur local
- serveurs DNS d’opérateurs
- solutions de confidentialité DNS

---
## 3. dnsmasq

![[Pasted image 20260308003303.png|549]]![[Pasted image 20260308003312.png|546]]
![Personal DHCP & DNS over TLS Server](https://www.naut.ca/blog/content/images/2018/06/dns_diagram-1.svg)
![[Pasted image 20260308003338.png|469]]
**dnsmasq** est un **DNS cache léger** souvent utilisé dans :

- **routeurs**
- **box Internet**
- **petits réseaux**

Il combine plusieurs services :
- **DNS cache**
- **DHCP server**
- **TFTP server**

**Fonctionnement typique dans une box :**

Client → dnsmasq (box)  
        → DNS FAI (forward)

ou

Client → dnsmasq  
        → résolveur public (1.1.1.1 / 8.8.8.8)

**Exemple configuration**

server=8.8.8.8  
server=1.1.1.1  
cache-size=1000

**Points forts**
- extrêmement **léger**
- très simple
- idéal pour **LAN domestique**

**Limites**

- pas conçu pour grandes infrastructures
- fonctionnalités DNS limitées

---

## 4. CoreDNS (cloud / Kubernetes)

![[Pasted image 20260308004916.png]]![[Pasted image 20260308004921.png|697]]
![[Pasted image 20260308004934.png]]![[Pasted image 20260308004939.png]]

**CoreDNS** est un serveur DNS **modulaire** écrit en **Go**.

Il est aujourd’hui le **DNS par défaut de Kubernetes**.

**Architecture plugin**

CoreDNS fonctionne via des **plugins** :

- `kubernetes`
- `forward`    
- `cache`
- `prometheus`
- `rewrite`

Exemple de configuration :
```bash
.:53 {  
    kubernetes cluster.local  
    forward . 8.8.8.8  
    cache 30  
}
```
**Rôle dans Kubernetes**

Résolution de services internes :
```bash
myservice.default.svc.cluster.local
```
**Points forts**
- architecture **plugin**
- très **cloud-native**
- facile à intégrer dans **microservices**

---
## 5. PowerDNS

![[Pasted image 20260308005437.png]]

![[Pasted image 20260308005448.png]]

![[Pasted image 20260308005457.png]]

![[Pasted image 20260308005503.png]]

**PowerDNS** est une implémentation DNS moderne séparée en **deux composants** :

1. **PowerDNS Authoritative Server**
2. **PowerDNS Recursor**

**Particularité importante :**
Les zones DNS peuvent être stockées dans une **base de données** :
- MySQL
- PostgreSQL
- SQLite
- LDAP

Exemple :
domain → database  
DNS server → query database → answer

**Avantages**
- très utilisé chez les **hébergeurs**
- API REST
- backend base de données
- scalable

**Usage typique**
- DNS de fournisseurs cloud
- registrars
- plateformes SaaS

---
# Comparaison rapide

| Logiciel     | Type principal         | Usage                             |
| ------------ | ---------------------- | --------------------------------- |
| **BIND**     | autoritatif + récursif | Internet classique                |
| **Unbound**  | résolveur récursif     | sécurité / performance            |
| **dnsmasq**  | cache + DHCP           | routeurs / LAN                    |
| **CoreDNS**  | DNS modulaire          | Kubernetes / cloud                |
| **PowerDNS** | autoritatif + recursor | hébergeurs / DNS à grande échelle |

---

💡 **Résumé simple**

- **BIND** → historique et complet
- **Unbound** → résolveur récursif moderne
- **dnsmasq** → DNS léger pour réseaux locaux    
- **CoreDNS** → DNS cloud-native (Kubernetes)
- **PowerDNS** → DNS scalable avec backend base de données

---


