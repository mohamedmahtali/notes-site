---
tags:
  - intermediate
---

`DevOps [[Linux]] [[Git]] [[CI/CD]] [[Infrastructure as Code]] [[Cloud]] [[Observability]] [[Security]]`
`│`
`├── Linux [[Kernel]] [[Shell]] [[Processes]] [[Networking]] [[Security]]`
`│   ├── Kernel [[System calls]] [[Process scheduler]] [[Memory management]] [[Modules]] [[Device drivers]]`
`│   │   ├── System calls [[Kernel]] [[Processes]] [[Shell]] [[Container runtime]]`
`│   │   ├── Process scheduler [[Processes]] [[Memory management]] [[kubelet]]`
`│   │   ├── Memory management [[Virtual memory]] [[Paging]] [[Swap]] [[Processes]] [[Containers]]`
`│   │   │   ├── Virtual memory [[Paging]] [[Swap]] [[Memory management]] [[Processes]]`
`│   │   │   ├── Paging [[Virtual memory]] [[Swap]] [[Memory management]]`
`│   │   │   └── Swap [[Paging]] [[Virtual memory]] [[Memory management]]`
`│   │   ├── Modules [[Kernel]] [[Device drivers]] [[Firewall]]`
`│   │   └── Device drivers [[Kernel]] [[Network interfaces]] [[Container runtime]]`
`│   │`
`│   ├── Shell [[Bash]] [[Zsh]] [[POSIX shell]] [[SSH]]`
`│   │   ├── Bash [[Variables]] [[Conditions]] [[Loops]] [[Functions]] [[Pipes]] [[Redirections]] [[Exit codes]]`
`│   │   │   ├── Variables [[Bash]] [[Environment variables]] [[Terraform variables]] [[Variables]]`
`│   │   │   ├── Conditions [[Bash]] [[Loops]] [[Exit codes]]`
`│   │   │   ├── Loops [[Bash]] [[Conditions]] [[Functions]]`
`│   │   │   ├── Functions [[Bash]] [[Loops]] [[Tasks]]`
`│   │   │   ├── Pipes [[Redirections]] [[stdout]] [[stdin]] [[Logs]]`
`│   │   │   ├── Redirections [[Pipes]] [[stdout]] [[stderr]] [[stdin]]`
`│   │   │   │   ├── stdout [[stderr]] [[stdin]] [[Redirections]] [[Logs]]`
`│   │   │   │   ├── stderr [[stdout]] [[stdin]] [[Redirections]] [[Logs]]`
`│   │   │   │   └── stdin [[stdout]] [[stderr]] [[Redirections]] [[Pipes]]`
`│   │   │   └── Exit codes [[Conditions]] [[Bash]] [[Pipeline]] [[Jobs]]`
`│   │   ├── Zsh [[Bash]] [[Shell]] [[POSIX shell]]`
`│   │   └── POSIX shell [[Shell]] [[Bash]] [[Zsh]]`
`│   │`
`│   ├── File system [[File permissions]] [[Inodes]] [[Mount points]] [[Partitions]] [[Links]] [[Volumes]]`
`│   │   ├── File permissions [[chmod]] [[chown]] [[chgrp]] [[umask]] [[Users]] [[Groups]]`
`│   │   │   ├── chmod [[File permissions]] [[umask]] [[chown]]`
`│   │   │   ├── chown [[File permissions]] [[Users]] [[Groups]] [[chgrp]]`
`│   │   │   ├── chgrp [[File permissions]] [[Groups]] [[chown]]`
`│   │   │   └── umask [[File permissions]] [[chmod]] [[Users]]`
`│   │   ├── Inodes [[Links]] [[File types]] [[File system]]`
`│   │   ├── Mount points [[Partitions]] [[Volumes]] [[Bind mounts]] [[Persistent volumes]]`
`│   │   ├── Partitions [[Mount points]] [[Boot disks]] [[File system]]`
`│   │   ├── Links [[Hard links]] [[Symbolic links]] [[Inodes]]`
`│   │   │   ├── Hard links [[Symbolic links]] [[Links]] [[Inodes]]`
`│   │   │   └── Symbolic links [[Hard links]] [[Links]] [[Mount points]]`
`│   │   └── File types [[Inodes]] [[File system]] [[Links]]`
`│   │`
`│   ├── Users [[Groups]] [[sudo]] [[PAM]] [[Home directories]] [[IAM]] [[RBAC]]`
`│   │   ├── Groups [[Users]] [[File permissions]] [[RBAC]] [[Service accounts]]`
`│   │   ├── sudo [[Users]] [[Least privilege]] [[PAM]] [[RBAC]]`
`│   │   ├── PAM [[Users]] [[sudo]] [[SSH]] [[Zero trust]]`
`│   │   ├── Home directories [[Users]] [[File system]] [[SSH keys]]`
`│   │   └── Service accounts [[Users]] [[RBAC]] [[Secrets]] [[Tokens]]`
`│   │`
`│   ├── Processes [[Signals]] [[ps]] [[top]] [[htop]] [[Container lifecycle]] [[Pod lifecycle]]`
`│   │   ├── Foreground and background [[Processes]] [[Shell]] [[Cron]]`
`│   │   ├── Signals [[SIGTERM]] [[SIGKILL]] [[SIGHUP]] [[Processes]] [[Container lifecycle]]`
`│   │   │   ├── SIGTERM [[SIGKILL]] [[SIGHUP]] [[Signals]] [[Graceful shutdown]]`
`│   │   │   ├── SIGKILL [[SIGTERM]] [[Signals]] [[Processes]]`
`│   │   │   └── SIGHUP [[Signals]] [[SSH]] [[Services]]`
`│   │   ├── ps [[Processes]] [[top]] [[htop]]`
`│   │   ├── top [[htop]] [[ps]] [[Metrics]]`
`│   │   ├── htop [[top]] [[ps]] [[Processes]]`
`│   │   └── nice and renice [[Processes]] [[Process scheduler]] [[CPU limits]]`
`│   │`
`│   ├── systemd [[Services]] [[journalctl]] [[Timers]] [[Logs]]`
`│   │   ├── Services [[Unit files]] [[Targets]] [[Restart policies]] [[Dependencies]] [[systemd]]`
`│   │   │   ├── Unit files [[Services]] [[Targets]] [[Dependencies]]`
`│   │   │   ├── Targets [[Unit files]] [[Services]] [[Dependencies]]`
`│   │   │   ├── Restart policies [[Services]] [[Pod lifecycle]] [[Container lifecycle]]`
`│   │   │   └── Dependencies [[Unit files]] [[Targets]] [[Services]]`
`│   │   ├── journalctl [[Logs]] [[Boot logs]] [[Service logs]] [[Log filtering]] [[systemd]]`
`│   │   │   ├── Log filtering [[journalctl]] [[Service logs]] [[Structured logs]]`
`│   │   │   ├── Boot logs [[journalctl]] [[Services]] [[systemd]]`
`│   │   │   └── Service logs [[journalctl]] [[Services]] [[Application logs]]`
`│   │   └── Timers [[Cron]] [[systemd]] [[Scheduled jobs]]`
`│   │`
`│   ├── Logs [[Syslog]] [[logrotate]] [[Application logs]] [[Audit logs]] [[Logging]]`
`│   │   ├── Syslog [[Logs]] [[journalctl]] [[Centralized logging]]`
`│   │   ├── logrotate [[Logs]] [[Log retention]] [[Application logs]]`
`│   │   ├── Application logs [[Logs]] [[Service logs]] [[Loki]] [[Structured logs]]`
`│   │   └── Audit logs [[Logs]] [[PAM]] [[Zero trust]] [[Security]]`
`│   │`
`│   ├── SSH [[SSH keys]] [[SSH config]] [[Port forwarding]] [[SCP and SFTP]] [[Security]]`
`│   │   ├── SSH keys [[Public key]] [[Private key]] [[Passphrase]] [[ssh-agent]] [[Vault]]`
`│   │   │   ├── Public key [[Private key]] [[SSH keys]] [[Certificates]]`
`│   │   │   ├── Private key [[Public key]] [[Passphrase]] [[SSH keys]] [[Secrets management]]`
`│   │   │   ├── Passphrase [[Private key]] [[SSH keys]] [[Vault]]`
`│   │   │   └── ssh-agent [[SSH keys]] [[Private key]] [[Passphrase]]`
`│   │   ├── SSH config [[SSH]] [[Port forwarding]] [[SCP and SFTP]]`
`│   │   ├── Port forwarding [[SSH]] [[Ports]] [[NodePort]] [[Ingress]]`
`│   │   └── SCP and SFTP [[SSH]] [[Object storage]] [[File system]]`
`│   │`
`│   ├── Cron [[Crontab syntax]] [[Scheduled jobs]] [[Cron logs]] [[Timers]]`
`│   │   ├── Crontab syntax [[Cron]] [[Scheduled jobs]] [[Timers]]`
`│   │   ├── Scheduled jobs [[Cron]] [[Timers]] [[Schedule trigger]]`
`│   │   └── Cron logs [[Cron]] [[Logs]] [[journalctl]]`
`│   │`
`│   ├── Networking [[IP addressing]] [[Ports]] [[DNS]] [[Routing]] [[TCP and UDP]] [[Network interfaces]] [[Troubleshooting]]`
`│   │   ├── IP addressing [[IPv4]] [[IPv6]] [[CIDR]] [[Subnetting]] [[Subnets]] [[VPC]]`
`│   │   │   ├── IPv4 [[IPv6]] [[CIDR]] [[IP addressing]]`
`│   │   │   ├── IPv6 [[IPv4]] [[CIDR]] [[IP addressing]]`
`│   │   │   ├── CIDR [[Subnetting]] [[Subnets]] [[IP addressing]]`
`│   │   │   └── Subnetting [[CIDR]] [[Subnets]] [[VPC]]`
`│   │   ├── Ports [[Port scanning]] [[Well known ports]] [[Ephemeral ports]] [[Services]] [[Firewall]]`
`│   │   │   ├── Well known ports [[Ports]] [[Services]] [[Ingress]]`
`│   │   │   ├── Ephemeral ports [[Ports]] [[TCP and UDP]] [[Load balancers]]`
`│   │   │   └── Port scanning [[Ports]] [[Firewall]] [[Zero trust]] [[Vulnerability scanning]]`
`│   │   ├── DNS [[A record]] [[CNAME]] [[MX]] [[TTL]] [[Ingress]] [[Load balancers]]`
`│   │   │   ├── A record [[CNAME]] [[DNS]] [[Load balancers]]`
`│   │   │   ├── CNAME [[A record]] [[DNS]] [[Ingress]]`
`│   │   │   ├── MX [[DNS]] [[TTL]] [[SMTP]]`
`│   │   │   └── TTL [[DNS]] [[Caching]] [[A record]]`
`│   │   ├── Routing [[VPC]] [[Routing tables]] [[Ingress]] [[Load balancers]]`
`│   │   ├── TCP and UDP [[Ports]] [[Load balancers]] [[Services]]`
`│   │   ├── Network interfaces [[Device drivers]] [[Routing]] [[Bridge]]`
`│   │   └── Troubleshooting [[ping]] [[traceroute]] [[netstat]] [[ss]] [[Monitoring]]`
`│   │       ├── ping [[traceroute]] [[DNS]] [[Troubleshooting]]`
`│   │       ├── traceroute [[ping]] [[Routing]] [[Troubleshooting]]`
`│   │       ├── netstat [[ss]] [[Ports]] [[Troubleshooting]]`
`│   │       └── ss [[netstat]] [[Ports]] [[Troubleshooting]]`
`│   │`
`│   └── Firewall [[iptables]] [[ufw]] [[nftables]] [[Ports]] [[Security groups]]`
`│       ├── iptables [[Chains]] [[Rules]] [[NAT]] [[Forwarding]] [[Firewall]]`
`│       │   ├── Chains [[Rules]] [[iptables]] [[NAT]]`
`│       │   ├── Rules [[Chains]] [[iptables]] [[Security groups]]`
`│       │   ├── NAT [[Forwarding]] [[iptables]] [[NAT gateway]]`
`│       │   └── Forwarding [[NAT]] [[iptables]] [[Routing]]`
`│       ├── ufw [[Firewall]] [[Allow rules]] [[Deny rules]] [[Status]]`
`│       │   ├── Allow rules [[Deny rules]] [[ufw]] [[Security groups]]`
`│       │   ├── Deny rules [[Allow rules]] [[ufw]] [[Zero trust]]`
`│       │   └── Status [[ufw]] [[Monitoring]] [[Logs]]`
`│       └── nftables [[Firewall]] [[iptables]] [[Rules]]`
`│`
`├── Git [[Repository]] [[Commit]] [[Branch]] [[Merge]] [[Rebase]] [[Pull request]] [[Git workflow]]`
`│   ├── Repository [[Local repository]] [[Remote repository]] [[Bare repository]] [[Git submodules]]`
`│   │   ├── Local repository [[Remote repository]] [[Repository]] [[Commit]]`
`│   │   ├── Remote repository [[Local repository]] [[Pull request]] [[Repository]]`
`│   │   └── Bare repository [[Remote repository]] [[Repository]] [[Git hooks]]`
`│   ├── Commit [[Commit message]] [[Amend]] [[Commit history]] [[Branch]]`
`│   │   ├── Commit message [[Commit]] [[commit-msg]] [[Code review]]`
`│   │   ├── Amend [[Commit]] [[Interactive rebase]] [[Rewrite history]]`
`│   │   └── Commit history [[Commit]] [[reflog]] [[bisect]]`
`│   ├── Branch [[Feature branch]] [[Main branch]] [[Release branch]] [[Hotfix branch]] [[Merge]] [[Rebase]]`
`│   │   ├── Feature branch [[Branch]] [[Pull request]] [[GitHub flow]]`
`│   │   ├── Main branch [[Branch]] [[Trunk based development]] [[Release branch]]`
`│   │   ├── Release branch [[Main branch]] [[Hotfix branch]] [[Git flow]]`
`│   │   └── Hotfix branch [[Release branch]] [[Branch]] [[Continuous deployment]]`
`│   ├── Merge [[Fast forward merge]] [[Three way merge]] [[Merge conflicts]] [[Pull request]]`
`│   │   ├── Fast forward merge [[Merge]] [[Rebase]] [[GitHub flow]]`
`│   │   ├── Three way merge [[Merge]] [[Merge conflicts]] [[Pull request]]`
`│   │   └── Merge conflicts [[Merge]] [[Rebase]] [[Code review]]`
`│   ├── Rebase [[Interactive rebase]] [[Squash]] [[Rewrite history]] [[Merge]]`
`│   │   ├── Interactive rebase [[Rebase]] [[Squash]] [[Amend]]`
`│   │   ├── Squash [[Interactive rebase]] [[Commit]] [[Pull request]]`
`│   │   └── Rewrite history [[Rebase]] [[reflog]] [[Amend]]`
`│   ├── Pull request [[Code review]] [[Approvals]] [[Merge checks]] [[Branch]] [[Merge]]`
`│   │   ├── Code review [[Pull request]] [[Approvals]] [[Merge checks]] [[Commit message]]`
`│   │   ├── Approvals [[Pull request]] [[Code review]] [[Merge checks]]`
`│   │   └── Merge checks [[Pull request]] [[CI/CD]] [[Code quality checks]]`
`│   ├── Git workflow [[Git flow]] [[GitHub flow]] [[Trunk based development]] [[CI/CD]]`
`│   │   ├── Git flow [[Git workflow]] [[Release branch]] [[Hotfix branch]]`
`│   │   ├── GitHub flow [[Git workflow]] [[Feature branch]] [[Pull request]]`
`│   │   └── Trunk based development [[Git workflow]] [[Main branch]] [[Continuous integration]]`
`│   ├── Git hooks [[pre-commit]] [[pre-push]] [[commit-msg]] [[CI/CD]]`
`│   │   ├── pre-commit [[Git hooks]] [[Code quality checks]] [[SAST]]`
`│   │   ├── pre-push [[Git hooks]] [[Automated tests]] [[CI/CD]]`
`│   │   └── commit-msg [[Git hooks]] [[Commit message]] [[Conventional commits]]`
`│   ├── Git tags [[Lightweight tags]] [[Annotated tags]] [[Versioning]]`
`│   │   ├── Lightweight tags [[Annotated tags]] [[Git tags]] [[Versioning]]`
`│   │   └── Annotated tags [[Lightweight tags]] [[Git tags]] [[Artifacts]]`
`│   ├── Git ignore [[Global ignore]] [[Project ignore]] [[Artifacts]]`
`│   │   ├── Global ignore [[Project ignore]] [[Git ignore]] [[Local repository]]`
`│   │   └── Project ignore [[Global ignore]] [[Git ignore]] [[Artifacts]]`
`│   ├── Git stash [[Save stash]] [[Pop stash]] [[Apply stash]] [[Branch]]`
`│   │   ├── Save stash [[Git stash]] [[Apply stash]] [[Pop stash]]`
`│   │   ├── Pop stash [[Save stash]] [[Apply stash]] [[Git stash]]`
`│   │   └── Apply stash [[Save stash]] [[Pop stash]] [[Git stash]]`
`│   ├── Git submodules [[Add submodule]] [[Update submodule]] [[Nested repositories]] [[Repository]]`
`│   │   ├── Add submodule [[Git submodules]] [[Update submodule]] [[Repository]]`
`│   │   ├── Update submodule [[Git submodules]] [[Add submodule]] [[Pipeline]]`
`│   │   └── Nested repositories [[Git submodules]] [[Repository]] [[Terraform modules]]`
`│   └── Advanced Git [[cherry-pick]] [[bisect]] [[reflog]] [[reset]]`
`│       ├── cherry-pick [[Advanced Git]] [[Commit]] [[Hotfix branch]]`
`│       ├── bisect [[Advanced Git]] [[Commit history]] [[Automated tests]]`
`│       ├── reflog [[Advanced Git]] [[Rewrite history]] [[Commit history]]`
`│       └── reset [[soft]] [[mixed]] [[hard]] [[Advanced Git]]`
`│           ├── soft [[reset]] [[mixed]] [[Commit]]`
`│           ├── mixed [[reset]] [[soft]] [[hard]]`
`│           └── hard [[reset]] [[Rewrite history]] [[reflog]]`
`│`
`├── Docker [[Containers]] [[Images]] [[Dockerfile]] [[Docker run]] [[Docker volumes]] [[Docker networks]] [[Docker compose]] [[Docker security]]`
`│   ├── Containers [[Container lifecycle]] [[Container logs]] [[Exec into container]] [[Resource limits]] [[Pods]]`
`│   │   ├── Container lifecycle [[create]] [[start]] [[stop]] [[restart]] [[remove]] [[Pod lifecycle]]`
`│   │   │   ├── create [[Container lifecycle]] [[Docker build]] [[Images]]`
`│   │   │   ├── start [[Container lifecycle]] [[stop]] [[restart]]`
`│   │   │   ├── stop [[Container lifecycle]] [[start]] [[restart]]`
`│   │   │   ├── restart [[Container lifecycle]] [[start]] [[stop]]`
`│   │   │   └── remove [[Container lifecycle]] [[Images]] [[Docker volumes]]`
`│   │   ├── Container logs [[Containers]] [[Application logs]] [[Loki]] [[kubectl logs]]`
`│   │   ├── Exec into container [[Containers]] [[kubectl exec]] [[Shell]]`
`│   │   └── Resource limits [[CPU limits]] [[Memory limits]] [[HPA]] [[Containers]]`
`│   │       ├── CPU limits [[Memory limits]] [[Resource limits]] [[CPU scaling]]`
`│   │       └── Memory limits [[CPU limits]] [[Resource limits]] [[Memory management]]`
`│   ├── Images [[Layers]] [[Base images]] [[Image tagging]] [[Image caching]] [[Docker registry]]`
`│   │   ├── Layers [[Images]] [[Image caching]] [[Docker build]]`
`│   │   ├── Base images [[Images]] [[Image scanning]] [[CVE detection]]`
`│   │   ├── Image tagging [[Images]] [[Versioning]] [[Git tags]]`
`│   │   └── Image caching [[Layers]] [[Docker layer cache]] [[Images]]`
`│   ├── Dockerfile [[Docker build]] [[Multi stage builds]] [[Instructions]] [[Best practices]]`
`│   │   ├── Docker build [[Build context]] [[Build cache]] [[Build arguments]] [[Dockerfile]]`
`│   │   │   ├── Build context [[Docker build]] [[COPY]] [[ADD]]`
`│   │   │   ├── Build cache [[Docker build]] [[Image caching]] [[Docker layer cache]]`
`│   │   │   └── Build arguments [[Docker build]] [[ENV]] [[Terraform variables]]`
`│   │   ├── Multi stage builds [[Dockerfile]] [[Base images]] [[Artifacts]]`
`│   │   ├── Instructions [[FROM]] [[RUN]] [[COPY]] [[ADD]] [[WORKDIR]] [[ENV]] [[EXPOSE]] [[CMD / ENTRYPOINT]]`
`│   │   │   ├── FROM [[Base images]] [[Dockerfile]] [[Multi stage builds]]`
`│   │   │   ├── RUN [[Dockerfile]] [[Build cache]] [[Packages]]`
`│   │   │   ├── COPY [[ADD]] [[Build context]] [[Dockerfile]]`
`│   │   │   ├── ADD [[COPY]] [[Build context]] [[Dockerfile]]`
`│   │   │   ├── WORKDIR [[Dockerfile]] [[CMD / ENTRYPOINT]] [[Exec into container]]`
`│   │   │   ├── ENV [[Environment variables]] [[Docker run]] [[Dockerfile]]`
`│   │   │   ├── EXPOSE [[Ports]] [[Docker run]] [[Services]]`
`│   │   │   └── CMD / ENTRYPOINT [[WORKDIR]] [[Docker run]] [[Exec into container]]`
`│   │   └── Best practices [[Dockerfile]] [[Non root user]] [[Multi stage builds]] [[Image scanning]]`
`│   ├── Docker run [[Detached mode]] [[Port mapping]] [[Environment variables]] [[Restart policy]] [[Containers]]`
`│   │   ├── Detached mode [[Docker run]] [[Container logs]] [[Restart policy]]`
`│   │   ├── Port mapping [[Docker run]] [[Ports]] [[EXPOSE]] [[NodePort]]`
`│   │   ├── Environment variables [[Docker run]] [[ENV]] [[Variables]] [[Secrets]]`
`│   │   └── Restart policy [[Docker run]] [[Restart policies]] [[Container lifecycle]]`
`│   ├── Docker volumes [[Bind mounts]] [[Named volumes]] [[Volume drivers]] [[Persistent volumes]]`
`│   │   ├── Bind mounts [[Docker volumes]] [[Mount points]] [[hostPath]]`
`│   │   ├── Named volumes [[Docker volumes]] [[Persistent volumes]] [[Storage classes]]`
`│   │   └── Volume drivers [[Docker volumes]] [[Persistent volumes]] [[Object storage]]`
`│   ├── Docker networks [[Bridge]] [[Host]] [[Overlay]] [[DNS in Docker]] [[Networking]]`
`│   │   ├── Bridge [[Docker networks]] [[Network interfaces]] [[ClusterIP]]`
`│   │   ├── Host [[Docker networks]] [[Ports]] [[NodePort]]`
`│   │   ├── Overlay [[Docker networks]] [[Cluster]] [[Services]]`
`│   │   └── DNS in Docker [[Docker networks]] [[DNS]] [[Docker compose]]`
`│   ├── Docker compose [[compose.yml]] [[Services]] [[Networks]] [[Volumes]] [[Profiles]] [[CI/CD]]`
`│   │   ├── compose.yml [[Docker compose]] [[Services]] [[Networks]] [[Volumes]]`
`│   │   ├── Services [[Docker compose]] [[ClusterIP]] [[Ports]] [[systemd]]`
`│   │   ├── Networks [[Docker compose]] [[Docker networks]] [[Routing]]`
`│   │   ├── Volumes [[Docker compose]] [[Docker volumes]] [[Persistent volumes]]`
`│   │   └── Profiles [[Docker compose]] [[CI/CD]] [[Environments]]`
`│   ├── Docker registry [[Docker hub]] [[Private registry]] [[Image pull and push]] [[Artifacts]]`
`│   │   ├── Docker hub [[Docker registry]] [[Public registry]] [[Base images]]`
`│   │   ├── Private registry [[Docker registry]] [[Secrets management]] [[IAM]]`
`│   │   └── Image pull and push [[Docker registry]] [[Images]] [[Artifacts]]`
`│   ├── Container runtime [[OCI]] [[containerd]] [[runc]] [[Node]]`
`│   │   ├── OCI [[Container runtime]] [[runc]] [[Images]]`
`│   │   ├── containerd [[Container runtime]] [[runc]] [[kubelet]]`
`│   │   └── runc [[Container runtime]] [[OCI]] [[containerd]]`
`│   ├── Rootless containers [[Non root user]] [[Container security]] [[Least privilege]]`
`│   └── Docker security [[Non root user]] [[Image signing]] [[Secrets handling]] [[Capability dropping]] [[Container security]]`
`│       ├── Non root user [[Docker security]] [[Rootless containers]] [[Least privilege]]`
`│       ├── Image signing [[Docker security]] [[Image scanning]] [[Policy enforcement]]`
`│       ├── Secrets handling [[Docker security]] [[Secrets]] [[Vault]] [[Environment variables]]`
`│       └── Capability dropping [[Docker security]] [[Seccomp]] [[AppArmor]]`
`│`
`├── Kubernetes [[Cluster]] [[Pods]] [[Services]] [[ConfigMaps]] [[Secrets]] [[Volumes]] [[Namespaces]] [[RBAC]] [[Helm]] [[Operators]] [[HPA]] [[kubectl]]`
`│   ├── Cluster [[Node]] [[Control plane]] [[Overlay]] [[VPC]]`
`│   │   ├── Node [[kubelet]] [[kube-proxy]] [[Container runtime]] [[Node labels]] [[DaemonSets]]`
`│   │   │   ├── kubelet [[Node]] [[containerd]] [[Pods]] [[kubectl]]`
`│   │   │   ├── kube-proxy [[Node]] [[Services]] [[ClusterIP]] [[NodePort]]`
`│   │   │   ├── Container runtime [[Node]] [[containerd]] [[runc]] [[Containers]]`
`│   │   │   └── Node labels [[Node]] [[Affinity and anti-affinity]] [[DaemonSets]]`
`│   │   └── Control plane [[API server]] [[Scheduler]] [[etcd]] [[Controller manager]] [[Cloud controller manager]]`
`│   │       ├── API server [[Control plane]] [[kubectl]] [[RBAC]] [[CRD]]`
`│   │       ├── Scheduler [[Control plane]] [[Pods]] [[Affinity and anti-affinity]]`
`│   │       ├── etcd [[Control plane]] [[Cluster]] [[Terraform state]]`
`│   │       ├── Controller manager [[Control plane]] [[Deployments]] [[ReplicaSets]]`
`│   │       └── Cloud controller manager [[Control plane]] [[Load balancers]] [[Cloud]]`
`│   │`
`│   ├── Pods [[Pod lifecycle]] [[Init containers]] [[Sidecar containers]] [[Deployments]] [[StatefulSets]] [[DaemonSets]]`
`│   │   ├── Pod lifecycle [[Containers]] [[Restart policies]] [[Container lifecycle]]`
`│   │   ├── Init containers [[Pods]] [[Sidecar containers]] [[ConfigMaps]]`
`│   │   ├── Sidecar containers [[Pods]] [[Init containers]] [[Logging]] [[Tracing]]`
`│   │   ├── Deployments [[ReplicaSets]] [[Rolling updates]] [[Rollbacks]] [[Continuous deployment]]`
`│   │   │   ├── ReplicaSets [[Deployments]] [[Controller manager]] [[HPA]]`
`│   │   │   ├── Rolling updates [[Deployments]] [[Rollbacks]] [[Progressive rollout]]`
`│   │   │   └── Rollbacks [[Deployments]] [[Rolling updates]] [[Continuous deployment]]`
`│   │   ├── StatefulSets [[Stable identity]] [[Persistent storage]] [[Persistent volumes]]`
`│   │   │   ├── Stable identity [[StatefulSets]] [[DNS]] [[Persistent storage]]`
`│   │   │   └── Persistent storage [[StatefulSets]] [[Persistent volumes]] [[Persistent volume claims]]`
`│   │   └── DaemonSets [[Node agents]] [[Node]] [[Monitoring]]`
`│   │       └── Node agents [[DaemonSets]] [[Exporters]] [[Logging]]`
`│   │`
`│   ├── Services [[ClusterIP]] [[NodePort]] [[LoadBalancer]] [[Ingress]] [[kube-proxy]]`
`│   │   ├── ClusterIP [[Services]] [[Bridge]] [[DNS in Docker]]`
`│   │   ├── NodePort [[Services]] [[Ports]] [[Port mapping]] [[LoadBalancer]]`
`│   │   ├── LoadBalancer [[Services]] [[Load balancers]] [[Cloud controller manager]]`
`│   │   └── Ingress [[Ingress controller]] [[Host based routing]] [[Path based routing]] [[DNS]] [[TLS]]`
`│   │       ├── Ingress controller [[Ingress]] [[LoadBalancer]] [[Controller manager]]`
`│   │       ├── Host based routing [[Ingress]] [[DNS]] [[CNAME]]`
`│   │       └── Path based routing [[Ingress]] [[Routing]] [[API gateway]]`
`│   │`
`│   ├── ConfigMaps [[Environment injection]] [[Mounted configuration]] [[Secrets]] [[Helm]]`
`│   │   ├── Environment injection [[ConfigMaps]] [[Mounted configuration]] [[Environment variables]]`
`│   │   └── Mounted configuration [[ConfigMaps]] [[Volumes]] [[Templates]]`
`│   ├── Secrets [[Opaque secrets]] [[TLS secrets]] [[External secrets]] [[Vault]] [[Secrets management]]`
`│   │   ├── Opaque secrets [[Secrets]] [[Environment injection]] [[Vault]]`
`│   │   ├── TLS secrets [[Secrets]] [[TLS]] [[Certificates]]`
`│   │   └── External secrets [[Secrets]] [[Vault]] [[Dynamic secrets]]`
`│   ├── Volumes [[emptyDir]] [[hostPath]] [[Persistent volumes]] [[Persistent volume claims]] [[Mount points]]`
`│   │   ├── emptyDir [[Volumes]] [[Pods]] [[Temporary storage]]`
`│   │   ├── hostPath [[Volumes]] [[Bind mounts]] [[Node]]`
`│   │   ├── Persistent volumes [[Storage classes]] [[Reclaim policies]] [[Persistent volume claims]] [[Docker volumes]]`
`│   │   │   ├── Storage classes [[Persistent volumes]] [[Named volumes]] [[Cloud]]`
`│   │   │   └── Reclaim policies [[Persistent volumes]] [[Terraform destroy]] [[Lifecycle rules]]`
`│   │   └── Persistent volume claims [[Persistent volumes]] [[StatefulSets]] [[Persistent storage]]`
`│   ├── Namespaces [[Resource isolation]] [[Multi tenancy]] [[RBAC]]`
`│   │   ├── Resource isolation [[Namespaces]] [[Resource limits]] [[RBAC]]`
`│   │   └── Multi tenancy [[Namespaces]] [[RBAC]] [[Zero trust]]`
`│   ├── RBAC [[Roles]] [[ClusterRoles]] [[RoleBindings]] [[Service accounts]] [[IAM]]`
`│   │   ├── Roles [[RBAC]] [[Permissions]] [[Least privilege]]`
`│   │   ├── ClusterRoles [[RBAC]] [[Roles]] [[API server]]`
`│   │   ├── RoleBindings [[RBAC]] [[Roles]] [[Service accounts]]`
`│   │   └── Service accounts [[RBAC]] [[Tokens]] [[Secrets]]`
`│   ├── Helm [[Charts]] [[Values]] [[Templates]] [[Releases]] [[Operators]]`
`│   │   ├── Charts [[Helm]] [[Templates]] [[Values]]`
`│   │   ├── Values [[Helm]] [[Terraform variables]] [[Variables]]`
`│   │   ├── Templates [[Helm]] [[Jinja2]] [[ConfigMaps]]`
`│   │   └── Releases [[Helm]] [[Continuous deployment]] [[Versioning]]`
`│   ├── Operators [[CRD]] [[Custom controllers]] [[Reconciliation loop]] [[Helm]]`
`│   │   ├── CRD [[Operators]] [[API server]] [[Custom controllers]]`
`│   │   ├── Custom controllers [[Operators]] [[Controller manager]] [[Reconciliation loop]]`
`│   │   └── Reconciliation loop [[Operators]] [[Custom controllers]] [[Desired state]]`
`│   ├── HPA [[CPU scaling]] [[Memory scaling]] [[Custom metrics]] [[Deployments]]`
`│   │   ├── CPU scaling [[HPA]] [[CPU limits]] [[Metrics]]`
`│   │   ├── Memory scaling [[HPA]] [[Memory limits]] [[Metrics]]`
`│   │   └── Custom metrics [[HPA]] [[Prometheus]] [[Application metrics]]`
`│   ├── kubectl [[apply]] [[get]] [[describe]] [[logs]] [[exec]] [[API server]]`
`│   │   ├── apply [[kubectl]] [[Terraform apply]] [[Deployments]]`
`│   │   ├── get [[kubectl]] [[describe]] [[API server]]`
`│   │   ├── describe [[kubectl]] [[get]] [[Events]]`
`│   │   ├── logs [[kubectl]] [[Container logs]] [[Application logs]]`
`│   │   └── exec [[kubectl]] [[Exec into container]] [[Shell]]`
`│   └── Advanced Kubernetes [[Taints and tolerations]] [[Affinity and anti-affinity]] [[Network policies]] [[Pod disruption budgets]] [[Admission controllers]]`
`│       ├── Taints and tolerations [[Advanced Kubernetes]] [[Node labels]] [[Scheduler]]`
`│       ├── Affinity and anti-affinity [[Advanced Kubernetes]] [[Node labels]] [[Scheduler]]`
`│       ├── Network policies [[Advanced Kubernetes]] [[Firewall]] [[Zero trust]] [[Security groups]]`
`│       ├── Pod disruption budgets [[Advanced Kubernetes]] [[Deployments]] [[Availability target]]`
`│       └── Admission controllers [[Advanced Kubernetes]] [[API server]] [[Policy enforcement]]`
`│`
`├── CI/CD [[Continuous integration]] [[Continuous delivery]] [[Continuous deployment]] [[Pipeline]] [[Artifacts]] [[GitHub actions]] [[GitLab CI]] [[Jenkins]]`
`│   ├── Continuous integration [[Automated build]] [[Automated tests]] [[Code quality checks]] [[Trunk based development]]`
`│   │   ├── Automated build [[Continuous integration]] [[Build stage]] [[Artifacts]]`
`│   │   ├── Automated tests [[Continuous integration]] [[Unit tests]] [[Integration tests]] [[End to end tests]]`
`│   │   └── Code quality checks [[Continuous integration]] [[SAST]] [[pre-commit]] [[Merge checks]]`
`│   ├── Continuous delivery [[Release readiness]] [[Manual approval]] [[Deploy stage]]`
`│   │   ├── Release readiness [[Continuous delivery]] [[Artifacts]] [[Staging]]`
`│   │   └── Manual approval [[Continuous delivery]] [[Production]] [[Approvals]]`
`│   ├── Continuous deployment [[Automated release]] [[Progressive rollout]] [[Rolling updates]] [[Rollbacks]]`
`│   │   ├── Automated release [[Continuous deployment]] [[Deploy stage]] [[Production]]`
`│   │   └── Progressive rollout [[Continuous deployment]] [[Rolling updates]] [[Load balancers]]`
`│   ├── Pipeline [[Build stage]] [[Test stage]] [[Deploy stage]] [[Pipeline triggers]] [[Pipeline caching]]`
`│   │   ├── Build stage [[Compile]] [[Package]] [[Containerize]] [[Artifacts]]`
`│   │   │   ├── Compile [[Build stage]] [[Package]] [[Automated build]]`
`│   │   │   ├── Package [[Build stage]] [[Compile]] [[Artifacts]]`
`│   │   │   └── Containerize [[Build stage]] [[Docker build]] [[Images]]`
`│   │   ├── Test stage [[Unit tests]] [[Integration tests]] [[End to end tests]] [[Security tests]]`
`│   │   │   ├── Unit tests [[Test stage]] [[Automated tests]] [[Jenkins]]`
`│   │   │   ├── Integration tests [[Test stage]] [[Automated tests]] [[Services]]`
`│   │   │   ├── End to end tests [[Test stage]] [[Automated tests]] [[Staging]]`
`│   │   │   └── Security tests [[Test stage]] [[SAST]] [[DAST]] [[Dependency scanning]]`
`│   │   └── Deploy stage [[Staging]] [[Production]] [[Rollback]] [[Continuous deployment]]`
`│   │       ├── Staging [[Deploy stage]] [[Release readiness]] [[End to end tests]]`
`│   │       ├── Production [[Deploy stage]] [[Manual approval]] [[Automated release]]`
`│   │       └── Rollback [[Deploy stage]] [[Rollbacks]] [[Continuous deployment]]`
`│   ├── Artifacts [[Build outputs]] [[Versioning]] [[Artifact repositories]] [[Docker registry]]`
`│   │   ├── Build outputs [[Artifacts]] [[Package]] [[Image pull and push]]`
`│   │   ├── Versioning [[Artifacts]] [[Git tags]] [[Releases]]`
`│   │   └── Artifact repositories [[Artifacts]] [[Docker registry]] [[Private registry]]`
`│   ├── GitHub actions [[Workflows]] [[Jobs]] [[Steps]] [[Actions marketplace]] [[Self hosted runners]]`
`│   │   ├── Workflows [[GitHub actions]] [[Jobs]] [[Pipeline]]`
`│   │   ├── Jobs [[GitHub actions]] [[Steps]] [[Runners]]`
`│   │   ├── Steps [[GitHub actions]] [[Jobs]] [[Actions marketplace]]`
`│   │   ├── Actions marketplace [[GitHub actions]] [[Steps]] [[Reusable modules]]`
`│   │   └── Self hosted runners [[GitHub actions]] [[Runners]] [[Agents]]`
`│   ├── GitLab CI [[.gitlab-ci.yml]] [[Stages]] [[Jobs]] [[Runners]]`
`│   │   ├── .gitlab-ci.yml [[GitLab CI]] [[Stages]] [[Jobs]]`
`│   │   ├── Stages [[GitLab CI]] [[Pipeline]] [[Jobs]]`
`│   │   ├── Jobs [[GitLab CI]] [[Runners]] [[Pipeline]]`
`│   │   └── Runners [[GitLab CI]] [[GitHub actions]] [[Jenkins]]`
`│   ├── Jenkins [[Jenkinsfile]] [[Declarative pipeline]] [[Scripted pipeline]] [[Agents]]`
`│   │   ├── Jenkinsfile [[Jenkins]] [[Declarative pipeline]] [[Scripted pipeline]]`
`│   │   ├── Declarative pipeline [[Jenkins]] [[Jenkinsfile]] [[Pipeline]]`
`│   │   ├── Scripted pipeline [[Jenkins]] [[Jenkinsfile]] [[Pipeline]]`
`│   │   └── Agents [[Jenkins]] [[Runners]] [[Self hosted runners]]`
`│   ├── Runners [[Self hosted runners]] [[Agents]] [[Jobs]]`
`│   ├── Pipeline triggers [[Push trigger]] [[Merge request trigger]] [[Schedule trigger]] [[Manual trigger]]`
`│   │   ├── Push trigger [[Pipeline triggers]] [[Continuous integration]] [[pre-push]]`
`│   │   ├── Merge request trigger [[Pipeline triggers]] [[Pull request]] [[Code review]]`
`│   │   ├── Schedule trigger [[Pipeline triggers]] [[Cron]] [[Scheduled jobs]]`
`│   │   └── Manual trigger [[Pipeline triggers]] [[Manual approval]] [[Production]]`
`│   └── Pipeline caching [[Dependency cache]] [[Docker layer cache]] [[Build cache]]`
`│       ├── Dependency cache [[Pipeline caching]] [[Package]] [[Build stage]]`
`│       └── Docker layer cache [[Pipeline caching]] [[Build cache]] [[Image caching]]`
`│`
`├── Infrastructure as Code [[Terraform]] [[Ansible]] [[Cloud]] [[CI/CD]]`
`│   ├── Terraform [[Terraform providers]] [[Terraform state]] [[Terraform modules]] [[Terraform variables]] [[Terraform outputs]] [[Terraform plan]] [[Terraform apply]]`
`│   │   ├── Terraform providers [[AWS provider]] [[Azure provider]] [[Google provider]] [[Cloud]]`
`│   │   │   ├── AWS provider [[Terraform providers]] [[AWS]] [[VPC]]`
`│   │   │   ├── Azure provider [[Terraform providers]] [[Azure]] [[Virtual Machines]]`
`│   │   │   └── Google provider [[Terraform providers]] [[Google Cloud]] [[GKE]]`
`│   │   ├── Terraform state [[Local state]] [[Remote state]] [[State locking]] [[Drift]] [[etcd]]`
`│   │   │   ├── Local state [[Terraform state]] [[Remote state]] [[Versioning]]`
`│   │   │   ├── Remote state [[Terraform state]] [[State locking]] [[Object storage]]`
`│   │   │   ├── State locking [[Terraform state]] [[Remote state]] [[Concurrency]]`
`│   │   │   └── Drift [[Terraform state]] [[Terraform plan]] [[Desired state]]`
`│   │   ├── Terraform modules [[Reusable modules]] [[Module inputs]] [[Module outputs]] [[Nested repositories]]`
`│   │   │   ├── Reusable modules [[Terraform modules]] [[Roles]] [[Actions marketplace]]`
`│   │   │   ├── Module inputs [[Terraform modules]] [[Terraform variables]] [[Values]]`
`│   │   │   └── Module outputs [[Terraform modules]] [[Terraform outputs]] [[Module inputs]]`
`│   │   ├── Terraform variables [[Types]] [[Defaults]] [[tfvars]] [[Variables]]`
`│   │   │   ├── Types [[Terraform variables]] [[Defaults]] [[Variables]]`
`│   │   │   ├── Defaults [[Terraform variables]] [[Types]] [[tfvars]]`
`│   │   │   └── tfvars [[Terraform variables]] [[Defaults]] [[Values]]`
`│   │   ├── Terraform outputs [[Terraform]] [[Module outputs]] [[Terraform apply]]`
`│   │   ├── Terraform plan [[Terraform]] [[Drift]] [[Terraform apply]]`
`│   │   ├── Terraform apply [[Terraform]] [[Terraform plan]] [[apply]]`
`│   │   ├── Terraform destroy [[Terraform]] [[Reclaim policies]] [[Lifecycle rules]]`
`│   │   └── Terraform workspaces [[Terraform]] [[Environments]] [[Staging]]`
`│   └── Ansible [[Inventory]] [[Playbooks]] [[Roles]] [[Tasks]] [[Handlers]] [[Variables]] [[Templates]] [[Idempotence]]`
`│       ├── Inventory [[Ansible]] [[Hosts]] [[Groups]]`
`│       ├── Playbooks [[Ansible]] [[Tasks]] [[Handlers]] [[Roles]]`
`│       ├── Roles [[Ansible]] [[RBAC]] [[Reusable modules]]`
`│       ├── Tasks [[Ansible]] [[Playbooks]] [[Functions]]`
`│       ├── Handlers [[Ansible]] [[Tasks]] [[Restart policies]]`
`│       ├── Variables [[Ansible]] [[Terraform variables]] [[Environment variables]]`
`│       ├── Templates [[Jinja2]] [[ConfigMaps]] [[Mounted configuration]]`
`│       │   └── Jinja2 [[Templates]] [[Helm]] [[Variables]]`
`│       └── Idempotence [[Ansible]] [[Desired state]] [[Reconciliation loop]]`
`│`
`├── Cloud [[Cloud computing]] [[IaaS]] [[PaaS]] [[SaaS]] [[Virtual machines]] [[AWS]] [[Azure]] [[Google Cloud]] [[VPC]] [[Subnets]] [[Security groups]] [[Load balancers]] [[Object storage]] [[IAM]] [[Autoscaling]]`
`│   ├── Cloud computing [[Elasticity]] [[On demand resources]] [[Shared responsibility model]] [[Autoscaling]]`
`│   │   ├── Elasticity [[Cloud computing]] [[Autoscaling]] [[Horizontal scaling]]`
`│   │   ├── On demand resources [[Cloud computing]] [[IaaS]] [[PaaS]]`
`│   │   └── Shared responsibility model [[Cloud computing]] [[Security]] [[IAM]]`
`│   ├── IaaS [[Virtual machines]] [[VPC]] [[Subnets]]`
`│   ├── PaaS [[SaaS]] [[Cloud computing]] [[Continuous deployment]]`
`│   ├── SaaS [[PaaS]] [[Cloud computing]] [[IAM]]`
`│   ├── Virtual machines [[Images]] [[Instance types]] [[Boot disks]] [[EC2]] [[Compute Engine]]`
`│   │   ├── Images [[Virtual machines]] [[Base images]] [[Image scanning]]`
`│   │   ├── Instance types [[Virtual machines]] [[Autoscaling]] [[CPU limits]]`
`│   │   └── Boot disks [[Virtual machines]] [[Partitions]] [[Persistent volumes]]`
`│   ├── AWS [[EC2]] [[S3]] [[IAM]] [[VPC]] [[EKS]] [[Terraform providers]]`
`│   │   ├── EC2 [[AWS]] [[Virtual machines]] [[Security groups]]`
`│   │   ├── S3 [[AWS]] [[Object storage]] [[Remote state]]`
`│   │   ├── IAM [[AWS]] [[Roles]] [[Policies]] [[Least privilege]]`
`│   │   ├── VPC [[AWS]] [[Subnets]] [[Routing tables]] [[Internet gateway]]`
`│   │   └── EKS [[AWS]] [[Kubernetes]] [[Cluster]]`
`│   ├── Azure [[Virtual Machines]] [[Blob Storage]] [[Azure AD]] [[AKS]] [[Azure provider]]`
`│   │   ├── Virtual Machines [[Azure]] [[Virtual machines]] [[Boot disks]]`
`│   │   ├── Blob Storage [[Azure]] [[Object storage]] [[Lifecycle rules]]`
`│   │   ├── Azure AD [[Azure]] [[IAM]] [[Users]]`
`│   │   └── AKS [[Azure]] [[Kubernetes]] [[Cluster]]`
`│   ├── Google Cloud [[Compute Engine]] [[Cloud Storage]] [[IAM]] [[GKE]] [[Google provider]]`
`│   │   ├── Compute Engine [[Google Cloud]] [[Virtual machines]] [[Instance types]]`
`│   │   ├── Cloud Storage [[Google Cloud]] [[Object storage]] [[Buckets]]`
`│   │   ├── IAM [[Google Cloud]] [[Roles]] [[Policies]]`
`│   │   └── GKE [[Google Cloud]] [[Kubernetes]] [[Cluster]]`
`│   ├── VPC [[Routing tables]] [[Internet gateway]] [[NAT gateway]] [[Subnets]] [[Security groups]]`
`│   │   ├── Routing tables [[VPC]] [[Routing]] [[Subnets]]`
`│   │   ├── Internet gateway [[VPC]] [[Public subnet]] [[Load balancers]]`
`│   │   └── NAT gateway [[VPC]] [[Private subnet]] [[NAT]]`
`│   ├── Subnets [[Public subnet]] [[Private subnet]] [[CIDR]] [[VPC]]`
`│   │   ├── Public subnet [[Subnets]] [[Internet gateway]] [[Load balancers]]`
`│   │   └── Private subnet [[Subnets]] [[NAT gateway]] [[Security groups]]`
`│   ├── Security groups [[Inbound rules]] [[Outbound rules]] [[Firewall]] [[Network policies]]`
`│   │   ├── Inbound rules [[Security groups]] [[Allow rules]] [[Ports]]`
`│   │   └── Outbound rules [[Security groups]] [[Deny rules]] [[Routing]]`
`│   ├── Load balancers [[Layer 4]] [[Layer 7]] [[Health checks]] [[Ingress]] [[LoadBalancer]]`
`│   │   ├── Layer 4 [[Load balancers]] [[TCP and UDP]] [[NodePort]]`
`│   │   ├── Layer 7 [[Load balancers]] [[Ingress]] [[Host based routing]]`
`│   │   └── Health checks [[Load balancers]] [[Monitoring]] [[Availability target]]`
`│   ├── Object storage [[Buckets]] [[Versioning]] [[Lifecycle rules]] [[Artifacts]]`
`│   │   ├── Buckets [[Object storage]] [[S3]] [[Cloud Storage]]`
`│   │   ├── Versioning [[Object storage]] [[Git tags]] [[Artifacts]]`
`│   │   └── Lifecycle rules [[Object storage]] [[Terraform destroy]] [[Reclaim policies]]`
`│   ├── IAM [[Users]] [[Roles]] [[Policies]] [[Least privilege]] [[RBAC]]`
`│   │   ├── Users [[IAM]] [[Groups]] [[Service accounts]]`
`│   │   ├── Roles [[IAM]] [[Policies]] [[RBAC]]`
`│   │   ├── Policies [[IAM]] [[Roles]] [[Least privilege]]`
`│   │   └── Least privilege [[IAM]] [[Zero trust]] [[sudo]] [[RBAC]]`
`│   └── Autoscaling [[Horizontal scaling]] [[Vertical scaling]] [[Scaling policies]] [[HPA]]`
`│       ├── Horizontal scaling [[Autoscaling]] [[HPA]] [[Elasticity]]`
`│       ├── Vertical scaling [[Autoscaling]] [[Instance types]] [[Memory limits]]`
`│       └── Scaling policies [[Autoscaling]] [[CPU scaling]] [[Health checks]]`
`│`
`├── Observability [[Monitoring]] [[Logging]] [[Metrics]] [[Tracing]] [[Grafana]] [[SLO SLA SLI]]`
`│   ├── Monitoring [[Prometheus]] [[Alertmanager]] [[Health checks]] [[Metrics]]`
`│   │   ├── Prometheus [[Exporters]] [[Scraping]] [[PromQL]] [[Recording rules]] [[Custom metrics]]`
`│   │   │   ├── Exporters [[Prometheus]] [[Node agents]] [[Infrastructure metrics]]`
`│   │   │   ├── Scraping [[Prometheus]] [[PromQL]] [[Metrics]]`
`│   │   │   ├── PromQL [[Prometheus]] [[Recording rules]] [[Grafana]]`
`│   │   │   └── Recording rules [[Prometheus]] [[PromQL]] [[Alertmanager]]`
`│   │   └── Alertmanager [[Alert routing]] [[Silences]] [[Notification channels]] [[Alerts]]`
`│   │       ├── Alert routing [[Alertmanager]] [[Notification channels]] [[SLO SLA SLI]]`
`│   │       ├── Silences [[Alertmanager]] [[Notification channels]] [[Maintenance]]`
`│   │       └── Notification channels [[Alertmanager]] [[Alert routing]] [[Manual approval]]`
`│   ├── Logging [[Loki]] [[Structured logs]] [[Centralized logging]] [[Log retention]] [[Logs]]`
`│   │   ├── Loki [[Logging]] [[Grafana]] [[Application logs]] [[Container logs]]`
`│   │   ├── Structured logs [[Logging]] [[Application logs]] [[Trace context]]`
`│   │   ├── Centralized logging [[Logging]] [[Loki]] [[Syslog]]`
`│   │   └── Log retention [[Logging]] [[logrotate]] [[Lifecycle rules]]`
`│   ├── Metrics [[RED method]] [[USE method]] [[Application metrics]] [[Infrastructure metrics]] [[Prometheus]]`
`│   │   ├── RED method [[Metrics]] [[Application metrics]] [[SLO SLA SLI]]`
`│   │   ├── USE method [[Metrics]] [[Infrastructure metrics]] [[Monitoring]]`
`│   │   ├── Application metrics [[Metrics]] [[Custom metrics]] [[RED method]]`
`│   │   └── Infrastructure metrics [[Metrics]] [[Exporters]] [[USE method]]`
`│   ├── Tracing [[OpenTelemetry]] [[Spans]] [[Trace context]] [[Distributed tracing]]`
`│   │   ├── OpenTelemetry [[Tracing]] [[Spans]] [[Metrics]] [[Logging]]`
`│   │   ├── Spans [[Tracing]] [[Trace context]] [[Distributed tracing]]`
`│   │   ├── Trace context [[Tracing]] [[Structured logs]] [[Spans]]`
`│   │   └── Distributed tracing [[Tracing]] [[OpenTelemetry]] [[Sidecar containers]]`
`│   ├── Grafana [[Dashboards]] [[Panels]] [[Datasources]] [[Alerts]] [[Prometheus]] [[Loki]]`
`│   │   ├── Dashboards [[Grafana]] [[Panels]] [[SLO SLA SLI]]`
`│   │   ├── Panels [[Grafana]] [[Dashboards]] [[Datasources]]`
`│   │   ├── Datasources [[Grafana]] [[Prometheus]] [[Loki]]`
`│   │   └── Alerts [[Grafana]] [[Alertmanager]] [[Availability target]]`
`│   └── SLO SLA SLI [[Error budget]] [[Availability target]] [[Reliability indicators]] [[Alert routing]]`
`│       ├── Error budget [[SLO SLA SLI]] [[Availability target]] [[Progressive rollout]]`
`│       ├── Availability target [[SLO SLA SLI]] [[Health checks]] [[Pod disruption budgets]]`
`│       └── Reliability indicators [[SLO SLA SLI]] [[SLI]] [[Metrics]]`
`│`
`└── Security [[DevSecOps]] [[Secrets management]] [[TLS]] [[Certificates]] [[Container security]] [[Image scanning]] [[Vulnerability scanning]] [[RBAC]] [[Zero trust]]`
    `├── DevSecOps [[Shift left security]] [[Security gates]] [[Secure SDLC]] [[CI/CD]]`
    `│   ├── Shift left security [[DevSecOps]] [[SAST]] [[pre-commit]]`
    `│   ├── Security gates [[DevSecOps]] [[Merge checks]] [[Manual approval]]`
    `│   └── Secure SDLC [[DevSecOps]] [[Continuous integration]] [[Code review]]`
    `├── Secrets management [[Vault]] [[Environment secrets]] [[Secret rotation]] [[Secrets]]`
    `│   ├── Vault [[Secret engines]] [[Policies]] [[Tokens]] [[Dynamic secrets]] [[Secrets]]`
    `│   │   ├── Secret engines [[Vault]] [[Dynamic secrets]] [[Secrets management]]`
    `│   │   ├── Policies [[Vault]] [[IAM]] [[Least privilege]]`
    `│   │   ├── Tokens [[Vault]] [[Service accounts]] [[Certificates]]`
    `│   │   └── Dynamic secrets [[Vault]] [[External secrets]] [[Secret rotation]]`
    `│   ├── Environment secrets [[Secrets management]] [[Environment variables]] [[Secrets handling]]`
    `│   └── Secret rotation [[Secrets management]] [[Dynamic secrets]] [[Certificates]]`
    `├── TLS [[Handshake]] [[Certificates]] [[Cipher suites]] [[Mutual TLS]] [[Ingress]]`
    `│   ├── Handshake [[TLS]] [[Certificates]] [[Cipher suites]]`
    `│   ├── Certificates [[TLS]] [[CA]] [[CSR]] [[Certificate renewal]]`
    `│   ├── Cipher suites [[TLS]] [[Handshake]] [[Zero trust]]`
    `│   └── Mutual TLS [[TLS]] [[Zero trust]] [[Service accounts]]`
    `├── Certificates [[CA]] [[CSR]] [[Self signed certificate]] [[Certificate renewal]] [[TLS secrets]]`
    `│   ├── CA [[Certificates]] [[CSR]] [[Public key]]`
    `│   ├── CSR [[Certificates]] [[CA]] [[Private key]]`
    `│   ├── Self signed certificate [[Certificates]] [[CA]] [[TLS]]`
    `│   └── Certificate renewal [[Certificates]] [[Secret rotation]] [[TLS secrets]]`
    `├── Container security [[Runtime security]] [[Namespace isolation]] [[Seccomp]] [[AppArmor]] [[Docker security]]`
    `│   ├── Runtime security [[Container security]] [[Vulnerability scanning]] [[Monitoring]]`
    `│   ├── Namespace isolation [[Container security]] [[Namespaces]] [[Rootless containers]]`
    `│   ├── Seccomp [[Container security]] [[Capability dropping]] [[AppArmor]]`
    `│   └── AppArmor [[Container security]] [[Seccomp]] [[Runtime security]]`
    `├── Image scanning [[Base image vulnerabilities]] [[CVE detection]] [[Policy enforcement]] [[Docker security]]`
    `│   ├── Base image vulnerabilities [[Image scanning]] [[Base images]] [[CVE detection]]`
    `│   ├── CVE detection [[Image scanning]] [[Dependency scanning]] [[Vulnerability scanning]]`
    `│   └── Policy enforcement [[Image scanning]] [[Admission controllers]] [[Image signing]]`
    `├── Vulnerability scanning [[SAST]] [[DAST]] [[Dependency scanning]] [[Infrastructure scanning]] [[Security tests]]`
    `│   ├── SAST [[Vulnerability scanning]] [[Shift left security]] [[Code quality checks]]`
    `│   ├── DAST [[Vulnerability scanning]] [[Security tests]] [[Ingress]]`
    `│   ├── Dependency scanning [[Vulnerability scanning]] [[CVE detection]] [[Dependency cache]]`
    `│   └── Infrastructure scanning [[Vulnerability scanning]] [[Terraform plan]] [[Cloud]]`
    `├── RBAC [[Roles]] [[Permissions]] [[Least privilege]] [[IAM]] [[Service accounts]]`
    `│   ├── Roles [[RBAC]] [[ClusterRoles]] [[IAM]]`
    `│   ├── Permissions [[RBAC]] [[Policies]] [[Least privilege]]`
    `│   └── Least privilege [[RBAC]] [[IAM]] [[Zero trust]] [[sudo]]`
    `└── Zero trust [[Verify explicitly]] [[Least privilege access]] [[Assume breach]] [[Mutual TLS]] [[Network policies]]`
        `├── Verify explicitly [[Zero trust]] [[Mutual TLS]] [[PAM]]`
        `├── Least privilege access [[Zero trust]] [[Least privilege]] [[RBAC]]`
        `└── Assume breach [[Zero trust]] [[Audit logs]] [[Runtime security]]`