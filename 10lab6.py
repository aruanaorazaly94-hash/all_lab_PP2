def write_list_to_file(filename, lst):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")

# Example
write_list_to_file("output.txt", ["apple", "banana", "cherry"])
