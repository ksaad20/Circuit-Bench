"""Export benchmark results."""

from __future__ import annotations


def export(args) -> None:
    """Export benchmark results."""
    if hasattr(args, "output"):
        print(f"Exporting results to: {args.output}")
    else:
        print("Exporting benchmark results.")


# Backward compatibility
execute = export
