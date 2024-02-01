def process_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.strip().split(':')
            if len(parts) == 4:
                print(f"The user {parts[0]} has a password of {parts[1]} and has userid {parts[2]} and grounpid {parts[3]}")


if __name__ == "__main__":
    process_file("fileprocessor.input")

