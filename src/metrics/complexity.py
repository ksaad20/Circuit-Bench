"""
Model complexity metrics.
"""

import os


def model_size(filepath):
    return os.path.getsize(filepath)


def parameter_count(model):
    return sum(p.numel() for p in model.parameters())


def trainable_parameters(model):
    return sum(
        p.numel()
        for p in model.parameters()
        if p.requires_grad
    )


def compression_ratio(original, compressed):
    return original / compressed
