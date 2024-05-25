import os
import shutil
from colorama import init, Fore, Style
from tqdm import tqdm

init(autoreset=True)


class BlenderCleanup:
    def __init__(
        self,
        blender_config_files,
        source_folder,
        destination_folder,
        temp_folder,
        folders_to_delete,
    ):
        self.blender_config_files = blender_config_files
        self.source_folder = source_folder
        self.destination_folder = destination_folder
        self.temp_folder = temp_folder
        self.folders_to_delete = folders_to_delete

    def check_config_files_exist(self):
        return all(os.path.exists(file) for file in self.blender_config_files)

    def display_config_files(self):
        for file in self.blender_config_files:
            if os.path.exists(file):
                print(f"{Fore.GREEN}Found: {file}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Not found: {file}{Style.RESET_ALL}")

    def copy_folder(self):
        destination_path = os.path.join(self.destination_folder, "Blender Foundation")
        try:
            if os.path.exists(destination_path):
                print(f"{Fore.GREEN}Deleting old config...{Style.RESET_ALL}")
                shutil.rmtree(destination_path)

            os.makedirs(destination_path)

            for item in os.listdir(self.source_folder):
                s = os.path.join(self.source_folder, item)
                d = os.path.join(destination_path, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)

            print(
                f"{Fore.GREEN}Folder {Fore.YELLOW}'{self.source_folder}'{Fore.GREEN} has been copied to {Fore.YELLOW}'{destination_path}'{Style.RESET_ALL}."
            )
        except Exception as e:
            print(f"{Fore.RED}Error during copying folder: {e}{Style.RESET_ALL}")

    def delete_folders(self):
        for folder_name, folder_path in self.folders_to_delete.items():
            try:
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
                    print(
                        f"{Fore.GREEN}Folder {Fore.YELLOW}'{folder_name}'{Fore.GREEN} has been removed.{Style.RESET_ALL}"
                    )
                else:
                    print(
                        f"{Fore.GREEN}Folder {Fore.YELLOW}'{folder_name}'{Fore.GREEN} does not exist, skipping...{Style.RESET_ALL}"
                    )
            except Exception as e:
                print(
                    f"{Fore.RED}Error during deleting folder '{folder_name}': {e}{Style.RESET_ALL}"
                )

    def delete_blend_files_in_temp(self):
        try:
            blend_files = [
                file for file in os.listdir(self.temp_folder) if file.endswith(".blend")
            ]
            for file in tqdm(blend_files, desc="Deleting .blend files...", unit="file"):
                os.remove(os.path.join(self.temp_folder, file))
                print(
                    f"\n{Fore.GREEN}File {Fore.YELLOW}'{file}'{Fore.GREEN} has been removed from temp.{Style.RESET_ALL}"
                )
        except Exception as e:
            print(f"{Fore.RED}Error during deleting blend files: {e}{Style.RESET_ALL}")


def main():
    blender_config_files = [
        r"C:\Users\Misiu\AppData\Roaming\Blender Foundation\Blender\4.1\config\platform_support.txt",
        r"C:\Users\Misiu\AppData\Roaming\Blender Foundation\Blender\4.1\config\recent-files.txt",
        r"C:\Users\Misiu\AppData\Roaming\Blender Foundation\Blender\4.1\config\recent-searches.txt",
        r"C:\Users\Misiu\AppData\Roaming\Blender Foundation\Blender\4.1\config\userpref.blend",
    ]
    source_folder = r"C:\Users\Misiu\AppData\Roaming\Blender Foundation"
    script_directory = os.path.dirname(os.path.realpath(__file__))
    destination_folder = script_directory
    temp_folder = os.path.expandvars(r"%temp%")

    folders_to_delete = {
        "Blender Foundation AppData Roaming": source_folder,
        "Blender Foundation AppData Local": r"C:\Users\Misiu\AppData\Local\Blender Foundation",
    }

    cleaner = BlenderCleanup(
        blender_config_files,
        source_folder,
        destination_folder,
        temp_folder,
        folders_to_delete,
    )

    cleaner.display_config_files()
    confirm = input(
        f"{Fore.CYAN}Do you want to proceed with copying and cleaning Blender folders? (Y/N): {Style.RESET_ALL}"
    ).lower()
    if confirm in ["y", "yes"]:
        cleaner.copy_folder()
        cleaner.delete_folders()
        cleaner.delete_blend_files_in_temp()
    else:
        print(f"{Fore.YELLOW}Operation cancelled.{Style.RESET_ALL}")


if __name__ == "__main__":
    os.system("title Portable Blender Cleanup Script")
    main()
