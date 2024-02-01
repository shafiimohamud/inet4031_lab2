
import sys

print("Processing redirected input...\n")

for line in sys.stdin:
    line = line.strip()
    if line.startswith('#') or not line:
        continue
    parts = line.split(':')
    if len(parts) == 4:
        print(f"The user {parts[0]} has a password of {parts[1]} and has userid {parts[2]} and groupid {parts[3]}")


print("\nFinished processing input.")

