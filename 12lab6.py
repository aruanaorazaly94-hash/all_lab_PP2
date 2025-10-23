def copy_file(src, dest):
    with open(src, 'r') as f1, open(dest, 'w') as f2:
        f2.write(f1.read())

# Example
# copy_file("output.txt", "copy_output.txt")
