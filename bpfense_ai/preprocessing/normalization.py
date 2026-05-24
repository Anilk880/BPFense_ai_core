from typing import Dict

NORMALIZATION_RANGES: Dict[str, float] = {

    "exec_count": 100.0,

    "shell_exec_count": 20.0,

    "sensitive_binary_execs": 20.0,

    "net_count": 50.0,

    "dns_requests": 100.0,

    "external_connections": 50.0,

    "unique_ips": 25.0,

    "unique_ports": 50.0,

    "exec_net_ratio": 20.0,

    "activity_ratio": 20.0,

    "burst": 50.0,

    "behavior_entropy": 10.0,

    "event_density": 10.0,

    "sequence_score": 100.0,

    "avg_exec_drift": 100.0,

    "avg_net_drift": 100.0,

    "time_delta_variance": 100.0,
}
