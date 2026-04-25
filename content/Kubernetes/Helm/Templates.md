---
title: Templates
tags:
  - intermediate
---
# Templates

---

## Définition

Les templates [[Helm]] sont des fichiers YAML utilisant la syntaxe Go template. Ils permettent de paramétrer les manifests [[Kubernetes]] avec des valeurs dynamiques, des [[Conditions]], et des boucles.

---

## Syntaxe de base

```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-app      # nom de la release
  namespace: {{ .Release.Namespace }}
  labels:
    app: {{ .Chart.Name }}
    version: {{ .Chart.AppVersion }}
spec:
  replicas: {{ .Values.replicaCount }}  # depuis values.yaml
  template:
    spec:
      containers:
      - name: app
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: {{ .Values.service.port }}
        {{- if .Values.resources }}    # conditionnel
        resources:
          {{- toYaml .Values.resources | nindent 10 }}
        {{- end }}
```

---

## Helpers (_helpers.tpl)

```
{{/*
Common labels
*/}}
{{- define "myapp.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end }}
```

```yaml
# Utilisation dans un template
metadata:
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
```

---

## Variables contextuelles

```
.Values       → valeurs de values.yaml + overrides
.Release      → .Release.Name, .Release.Namespace, .Release.IsInstall
.Chart        → .Chart.Name, .Chart.Version, .Chart.AppVersion
.Files        → accès aux fichiers du chart
.Capabilities → .Capabilities.KubeVersion
```
