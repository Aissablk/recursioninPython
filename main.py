import os

def python_files(path_target):
    if os.path.exists(path_target) and os.path.isdir(path_target):  
        python_files_list = []
        for f in os.listdir(path_target):
            if f.endswith(".py"):
                python_files_list.append(f)

        if python_files_list:
            print("Python files in the directory:", *python_files_list, sep="\n")
        else:
            print("No .py files in the directory.")
    else:
        print("The specified directory does not exist.")

if __name__ == "__main__":
    path_target = input("Enter the directory path: ")
    python_files(path_target)


    




os.walk()