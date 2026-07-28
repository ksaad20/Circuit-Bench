import os

def fix_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    
    # Remove trailing whitespace, keep newline chars
    lines = [line.rstrip() + '\n' for line in lines]
    
    # Remove extra blank lines at end, ensure exactly one
    while len(lines) > 1 and lines[-1] == '\n' and lines[-2] == '\n':
        lines.pop()
    
    # Ensure file ends with newline
    if lines and not lines[-1].endswith('\n'):
        lines[-1] += '\n'
    if not lines or lines[-1] != '\n':
        lines.append('\n')
    
    with open(path, 'w') as f:
        f.writelines(lines)

for folder in ['src', 'tests']:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.py'):
                fix_file(os.path.join(root, file))

print("Done")
