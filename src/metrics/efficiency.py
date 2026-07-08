"""
Efficiency metrics.
"""

import time


def throughput(samples, seconds):
    return samples / seconds


def samples_per_second(samples, runtime):
    return samples / runtime


def speedup(serial, parallel):
    return serial / parallel


def efficiency(speedup_value, processors):
    return speedup_value / processors

__all__ = [
    "efficiency_score",
    "compute_efficiency",
    "throughput_efficiency",
    "latency_efficiency",
    "memory_efficiency",
    "energy_efficiency",
    "accuracy_efficiency",
    "parameter_efficiency",
    "compute_per_parameter",
    "flops_per_second",
    "operations_per_second",
    "samples_per_second",
    "images_per_second",
    "tokens_per_second",
    "examples_per_second",
    "batch_efficiency",
    "scaling_efficiency",
    "parallel_efficiency",
    "speedup",
    "strong_scaling_efficiency",
    "weak_scaling_efficiency",
    "utilization",
    "resource_utilization",
    "hardware_efficiency",
    "compute_utilization",
    "io_efficiency",
    "cache_efficiency",
    "bandwidth_efficiency",
    "pipeline_efficiency",
    "overall_efficiency",
    "efficiency_summary",
    "efficiency_dataframe",
    "efficiency_report",
    "normalize_efficiency",
    "weighted_efficiency",
]
