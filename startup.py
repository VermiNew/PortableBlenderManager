import os
import zipfile
import subprocess
import shutil
from tqdm import tqdm
from colorama import init, Fore, Style

init(autoreset=True)

class BlenderManager:
    def __init__(self):
        self.blender_folder = "blender-4.0.2-windows-x64"
        self.archive_folder = ".archive"
        self.blender_archive = "blender-4.0.2-windows-x64.zip"
        self.appdata_folder = os.path.expandvars(r"%APPDATA%\Blender Foundation")

    def unpack_archive(self, archive_path, extract_to):
        try:
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                for file in tqdm(file_list, desc="Unpacking Blender", unit="file"):
                    zip_ref.extract(file, extract_to)
            print(f"{Fore.GREEN}Blender archive unpacked successfully.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error unpacking archive: {e}{Style.RESET_ALL}")

    def check_blender_structure(self, blender_folder):
        expected_files = [
            "4.0", "blender-launcher.exe", "blender.crt", "blender.exe",
            "blender.pdb", "blender.shared", "blender_debug_gpu.cmd",
            "blender_debug_gpu_glitchworkaround.cmd", "blender_debug_log.cmd",
            "blender_factory_startup.cmd", "blender_oculus.cmd", "BlendThumb.dll",
            "BlendThumb.lib", "copyright.txt", "cycles_kernel_oneapi_aot.dll",
            "license", "oculus.json", "python3.dll", "python310.dll", "readme.html"
        ]
        return all(os.path.exists(os.path.join(blender_folder, file)) for file in expected_files)

    def copy_blender_foundation(self):
        source = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Blender Foundation")
        if os.path.exists(source):
            if os.path.exists(self.appdata_folder):
                shutil.rmtree(self.appdata_folder)
            shutil.copytree(source, self.appdata_folder)
            print(f"{Fore.GREEN}Blender Foundation folder copied successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Blender Foundation folder not found in script directory.{Style.RESET_ALL}")

    def run_blender_and_cleanup(self):
        try:
            if not os.path.exists(self.blender_folder):
                if os.path.exists(os.path.join(self.archive_folder, self.blender_archive)):
                    confirm = input(f"{Fore.CYAN}Blender folder not found. Unpack archive? (yes/no): {Style.RESET_ALL}").lower()
                    if confirm in ['yes', 'y']:
                        self.unpack_archive(os.path.join(self.archive_folder, self.blender_archive), '.')

            if os.path.exists(self.blender_folder):
                if self.check_blender_structure(self.blender_folder):
                    self.copy_blender_foundation()
                    print(f"{Fore.GREEN}Starting Blender...{Style.RESET_ALL}")
                    process = subprocess.Popen([os.path.join(self.blender_folder, "blender.exe")])
                    print(f"{Fore.CYAN}Awaiting Blender shutdown...{Style.RESET_ALL}")
                    process.wait()  # Wait for Blender to close
                    print(f"{Fore.CYAN}Initiating cleaning process...{Style.RESET_ALL}")
                    subprocess.run(["python", "cleanup.py"])
                    print(f"{Fore.GREEN}The cleaning process has been successfully completed.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Blender folder structure is incorrect.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Blender folder does not exist and the archive is not available.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

def main():
    os.system("title Blender Portable Version [Handler]")
    blender_manager = BlenderManager()
    blender_manager.run_blender_and_cleanup()
    input(f"{Fore.CYAN}Click ANYTHING to quit{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
