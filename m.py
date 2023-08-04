import os

def generate_file_tree(path, indent=''):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            print(indent + '|--', item)
        elif os.path.isdir(item_path):
            print(indent + '|--', item)
            generate_file_tree(item_path, indent + '|   ')

if __name__ == '__main__':
    root_path = input("Enter the root path for file tree generation: ")
    if not os.path.exists(root_path):
        print("Error: The provided path does not exist.")
    else:
        print("File tree:")
        generate_file_tree(root_path)
