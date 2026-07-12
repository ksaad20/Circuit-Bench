from pathlib import Path

fixed = 0

for path in Path(".").rglob("*.py"):
    try:
        original = path.read_bytes()

        # Normalize line endings
        text = original.decode("utf-8", errors="ignore")
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Remove ALL blank lines at EOF
        text = text.rstrip()

        # Add exactly one newline
        text += "\n"

        new = text.encode("utf-8")

        if new != original:
            path.write_bytes(new)
            fixed += 1

    except Exception as e:
        print(path, e)

print(f"Fixed {fixed} files.")
