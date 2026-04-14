---
title: Volume drivers
tags:
  - advanced
---

# Volume drivers

## Parent
- [[Docker volumes]]

---

## Définition

Les volume drivers (ou volume plugins) permettent à Docker de stocker des volumes sur des backends autres que le filesystem local : NFS, AWS EBS, Azure Disk, Ceph, etc. Ils sont utilisés pour le stockage partagé entre plusieurs hôtes Docker.

---

## Drivers disponibles

| Driver | Backend | Usage |
|---|---|---|
| `local` (défaut) | Filesystem local | Développement, single-node |
| `nfs` | NFS | Stockage partagé multi-hosts |
| `rexray/ebs` | AWS EBS | Stockage persistant AWS |
| `rexray/s3fs` | AWS S3 | Stockage objet |
| `vieux/sshfs` | SSH | Stockage via SSH |

---

## Utiliser le driver NFS

```bash
# Créer un volume NFS
docker volume create   --driver local   --opt type=nfs   --opt o=addr=192.168.1.100,rw   --opt device=:/srv/nfs/data   nfs-data

docker run -v nfs-data:/data mon-app
```

---

## En Docker Compose

```yaml
volumes:
  shared-data:
    driver: local
    driver_opts:
      type: nfs
      o: "addr=192.168.1.100,rw"
      device: ":/srv/nfs/data"
```

---

> [!note]
> Pour le stockage partagé en production, Kubernetes avec des PersistentVolumes est généralement préféré à Docker standalone. Les volume drivers Docker sont plus courants en Swarm ou dans des setups Docker simples multi-hosts.
