import os
import shutil
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
    elif os.path.isfile(path):
        os.remove(path)
        tqdm.write(f"File {path} deleted.")
    else:
        tqdm.write(f"{Fore.YELLOW}Path {path} not found. Skipping.")

def main():
    dirs_to_delete = ["Blender Foundation", "blender-4.0.2-windows-x64"]
    file_to_delete = ".archive/blender-4.0.2-windows-x64.zip"

    print(f"{Fore.BLUE}Checking for files and directories...{Style.RESET_ALL}")
    paths_found = []
    for d in dirs_to_delete:
        if os.path.isdir(d):
            print(f"{Fore.GREEN}Found directory: {d}{Style.RESET_ALL}")
            paths_found.append(d)
        else:
            print(f"{Fore.RED}Directory not found: {d}{Style.RESET_ALL}")

    if os.path.isfile(file_to_delete):
        print(f"{Fore.GREEN}Found file: {file_to_delete}{Style.RESET_ALL}")
        paths_found.append(file_to_delete)
    else:
        print(f"{Fore.RED}File not found: {file_to_delete}{Style.RESET_ALL}")

    if not paths_found:
        print(f"{Fore.YELLOW}No files or directories to delete.{Style.RESET_ALL}")
        return

    confirm = input("Are you sure you want to delete these? (yes/no): ")
    if confirm.lower() != "yes":
        print(f"{Fore.CYAN}Deletion cancelled.{Style.RESET_ALL}")
        return

    print(f"{Fore.MAGENTA}Deleting...{Style.RESET_ALL}")
    for path in tqdm(paths_found, desc="Deleting", unit="item"):
        delete_with_progress(path)

    print(f"{Fore.GREEN}Deletion complete.{Style.RESET_ALL}")

if __name__ == "__main__":
    os.system("title Destroy Session Script")
    main()
    input(f"{Fore.CYAN}Press Enter to exit...{Style.RESET_ALL}\n")
