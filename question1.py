import os

def list_directory_contents():
    directory = input("Please enter the directory path: ")
    if not os.path.isdir(directory):
        print("The provided path is not a valid directory.")
        return
    print(f"Contents of the'{directory}' are as follows:\n")
    
    for item in os.listdir(directory):
        print(item)
        #item_path = os.path.join(directory, item)
        # if os.path.isdir(item_path):
        #     print(f"Directory: {item}")
        # elif os.path.isfile(item_path):
        #     print(f"File: {item}")
        # else:
        #     print(f"Other: {item}")

list_directory_contents()