from pathlib import Path

fixed = 0

for path in Path(".").rglob("*.py"):
    try:
        raw = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    # If the file is only whitespace/newlines, give it one harmless line.
    if raw.strip() == "":
        if path.name == "__init__.py":
            new_text = '"""Package marker."""\n'
        else:
            new_text = '"""Placeholder module."""\n'
        path.write_text(new_text, encoding="utf-8")
        fixed += 1

print(f"Fixed {fixed} empty Python files.")
