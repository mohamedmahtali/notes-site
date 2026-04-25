---
title: OpenTelemetry
tags:
  - intermediate
---
# OpenTelemetry

---

## Définition

OpenTelemetry (OTel) est le standard CNCF pour l'instrumentation de l'observabilité. Il unifie traces, métriques, et logs dans un seul SDK et protocole (OTLP), compatible avec tous les backends (Jaeger, Tempo, Datadog, etc.).

---

## Architecture OTel

```
Application (SDK OTel)
    ↓ OTLP
OTel Collector (agent/gateway)
    ├── → Jaeger/Tempo (traces)
    ├── → Prometheus (métriques)
    └── → Loki (logs)
```

---

## Installation

```bash
# Python
pip install opentelemetry-api opentelemetry-sdk   opentelemetry-instrumentation-fastapi   opentelemetry-exporter-otlp

# Go
go get go.opentelemetry.io/otel
go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp
```

---

## Configuration Python

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Setup
provider = TracerProvider()
exporter = OTLPSpanExporter(endpoint="http://otel-collector:4318/v1/traces")
provider.add_span_processor(BatchSpanProcessor(exporter))
trace.set_tracer_provider(provider)

# Auto-instrumentation FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
FastAPIInstrumentor.instrument_app(app)
```

---

## OTel Collector

```yaml
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318

exporters:
  jaeger:
    endpoint: jaeger:14250
  prometheus:
    endpoint: 0.0.0.0:8889

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [jaeger]
    metrics:
      receivers: [otlp]
      exporters: [prometheus]
```
