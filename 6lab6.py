import os

def list_path_content(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("Directories:", dirs)
    print("Files:", files)
    print("All:", os.listdir(path))

# Example
list_path_content(".")
