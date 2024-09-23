# question 1 task 1

import os 

def list_directory_contents(path):
    try:
        entries = os.listdir(path)

        for entry in entries:
            full_path = os.path.join(path, entry)

            if os.path.isdir(full_path):
                print(f"Directory: {entry}")
            elif os.path.isfile(full_path):
                print(f"File: {entry}")
            else:
                print(f"Other: {entry}")
    
    except FileNotFoundError:
        print("Error: Directory does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    path = input("Enter directory path: ")
    list_directory_contents(path)

if __name__ == "__main__":
    main()