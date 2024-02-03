import os
from tqdm import tqdm
from colorama import Fore, Style, init
init(autoreset=True)

def delete_with_progress(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
                tqdm.write(f"File {name} deleted.")
            for name in dirs:
                os.rmdir(os.path.join(root, name))
                tqdm.write(f"Directory {name} deleted.")
        os.rmdir(path)
    else:
        tqdm.write(f"{Fore.YELLOW}Directory {path} not found. Skipping.")

def main():
    dir_to_delete = "Blender Foundation"

    print(f"{Fore.BLUE}Checking for the directory...{Style.RESET_ALL}")
    if os.path.isdir(dir_to_delete):
        print(f"{Fore.GREEN}Found directory: {dir_to_delete}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Directory not found: {dir_to_delete}{Style.RESET_ALL}")
        return

    confirm = input("Are you sure you want to delete this directory? (yes/no): ")
    if confirm.lower() != "yes":
        print(f"{Fore.CYAN}Deletion cancelled.{Style.RESET_ALL}")
        return

    print(f"{Fore.MAGENTA}Deleting...{Style.RESET_ALL}")
    delete_with_progress(dir_to_delete)

    print(f"{Fore.GREEN}Deletion complete.{Style.RESET_ALL}")

if __name__ == "__main__":
    os.system("title Reset Blender Configuration Script")
    main()
    input(f"{Fore.CYAN}Press Enter to exit...{Style.RESET_ALL}\n")
