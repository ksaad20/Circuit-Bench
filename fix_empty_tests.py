from pathlib import Path

count = 0

for f in Path("tests").rglob("*.py"):
    if f.read_bytes() == b"\n":
        f.write_text('"""Placeholder test module."""\n', encoding="utf-8")
        count += 1

print(f"Fixed {count} empty test files.")
