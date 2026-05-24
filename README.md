# BPFense AI

Behavioral security ML runtime and inference framework.

## Features

- Behavioral anomaly detection
- TensorFlow inference
- ONNX runtime
- IsolationForest support
- Temporal LSTM analysis
- Autoencoder anomaly scoring
- Streaming behavioral inference

---

## Installation

```bash
pip install -e .
```

---

## Example

```python
from bpfense_ai import BPFenseClient

client = BPFenseClient()

result = client.predict({

    "exec_count": 10,
    "net_count": 5,
    "dns_requests": 2,
})

print(result)
```

---

## Disclaimer

This project is intended for:

- behavioral security research
- telemetry analysis
- ML experimentation
- anomaly detection research

This is NOT a complete enterprise EDR/XDR platform.
