# BPFense AI

Behavioral AI Runtime SDK for local behavioral threat detection, anomaly analysis, and telemetry-driven security inference.

BPFense AI is an open-source behavioral ML framework designed for:

- local behavioral inference
- runtime anomaly detection
- offline telemetry analysis
- security research
- behavioral malware experimentation
- multi-backend threat scoring

The project provides a modular AI inference pipeline combining:

- deep learning behavioral analysis
- statistical anomaly detection
- ensemble confidence scoring
- deterministic replay validation

---

# Features

## Behavioral AI Runtime

- Local AI inference
- Offline behavioral analysis
- Deterministic preprocessing pipeline
- Replay-driven behavioral validation
- Multi-backend inference architecture

---

## AI Backends

### TensorFlow Runtime

Deep learning behavioral classification:

- runtime telemetry analysis
- malicious behavior classification
- behavioral scoring
- temporal behavior modeling

### sklearn Runtime

Statistical anomaly detection using:

- IsolationForest
- anomaly scoring
- behavioral deviation detection
- unsupervised threat analysis

---

## Ensemble Detection

- Weighted backend aggregation
- Unified threat scoring
- Confidence scoring
- Severity classification
- Deterministic inference

---

## Security Replay Testing

Golden replay validation for:

- reverse shells
- DNS beaconing
- crypto miners
- port scanning
- lateral movement
- privilege escalation
- command-and-control beaconing
- data exfiltration

---

# Architecture

```text
Telemetry
    ↓
Validation
    ↓
Preprocessing
    ↓
Behavioral AI Runtime
    ├── TensorFlow Behavioral Analysis
    ├── sklearn Anomaly Analysis
    └── Ensemble Aggregation
    ↓
Confidence Scoring
    ↓
Unified Threat Assessment
    ↓
PredictionResponse
```

---

# Project Structure

```text
BPFense_ml_core/
│
├── bpfense_ai/
│   ├── api/
│   ├── inference/
│   │   ├── _tensorflow/
│   │   ├── _sklearn/
│   │   ├── aggregation.py
│   │   ├── confidence.py
│   │   └── classifier.py
│   │
│   ├── preprocessing/
│   │   ├── validators.py
│   │   ├── normalization.py
│   │   ├── integrity.py
│   │   └── preprocessor.py
│   │
│   ├── testing/
│   ├── configs/
│   └── exports/
│
├── tests/
│   ├── golden/
│   ├── regression/
│   └── replay/
│
├── examples/
├── pyproject.toml
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Anilk880/BPFense_ai_core.git

cd bpfense-ai
```

---

## Install SDK

```bash
pip install -e .
```

---

# Quick Start

```python
from bpfense_ai import BPFenseClient

client = BPFenseClient()

client.load()

result = client.predict({

    "exec_count": 5,
    "shell_exec_count": 1,
    "net_count": 2,
    "dns_requests": 1,
    "external_connections": 0,
})

print(result)
```

---

# Example Output

```python
PredictionResponse(

    label='malicious',

    severity='high',

    score=0.912,

    confidence=0.884,

    backend='ensemble'
)
```

---

# Testing

## Run Full Test Suite

```bash
pytest tests/ -v
```

---

## Run Golden Behavioral Tests

```bash
pytest tests/golden/ -v -s
```

---

## Run Regression Tests

```bash
pytest tests/regression/ -v
```

---

# Threat Behaviors Covered

| Behavior | Detection |
|---|---|
| Reverse Shell | ✔ |
| DNS Beaconing | ✔ |
| Port Scanning | ✔ |
| Crypto Mining | ✔ |
| Data Exfiltration | ✔ |
| Privilege Escalation | ✔ |
| Lateral Movement | ✔ |
| C2 Beaconing | ✔ |

---

# Behavioral Feature Schema

The SDK uses a deterministic behavioral feature schema for:

- runtime telemetry
- anomaly analysis
- behavioral replay testing
- temporal inference

Current schema includes:

- execution telemetry
- network telemetry
- behavioral entropy
- sequence scoring
- drift analysis
- temporal variance

---

# Open Source Goals

BPFense AI aims to provide:

- transparent behavioral ML research
- reproducible security experimentation
- deterministic inference pipelines
- replay-driven validation
- extensible AI runtime architectures

---

# Roadmap

## Planned Features

- ONNX runtime optimization
- streaming inference
- eBPF telemetry ingestion
- temporal sequence ensembles
- calibration tooling
- benchmark suite
- Docker deployment
- online anomaly learning

---

# License

Open-source under the MIT License.

See `LICENSE` for details.

---

# Disclaimer

This project is intended for:

- defensive security research
- telemetry experimentation
- malware behavior analysis
- educational purposes

Users are responsible for complying with all applicable laws and regulations.
