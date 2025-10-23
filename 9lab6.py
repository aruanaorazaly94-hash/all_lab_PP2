def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

# Example
# print(count_lines("example.txt"))
