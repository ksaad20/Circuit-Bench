"""
CircuitBench Datasets Package

Provides dataset abstractions, loading, registration,
validation, preprocessing, and metadata management.
"""

from .base.dataset import Dataset
from .registry.registry import DatasetRegistry

__all__ = [
    "Dataset",
    "DatasetRegistry",
]
