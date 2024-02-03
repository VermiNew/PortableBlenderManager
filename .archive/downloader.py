import requests
from tqdm import tqdm
from hashlib import sha256
from colorama import Fore, Style, init
import os
import configparser

init(autoreset=True)

def download_file(url, filename):
    if os.path.exists(filename):
        print(f"{Fore.YELLOW}The file {Fore.LIGHTMAGENTA_EX}{filename}{Fore.YELLOW} already exists. If the existing archive is corrupted, please manually delete the .zip file and rerun the script.{Style.RESET_ALL}")
        return False
    
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print(f"{Fore.RED}ERROR: Something went wrong during the download{Style.RESET_ALL}")
        return False
    return True

def verify_file(filename):
    sha256_hash = sha256()
    with open(filename,"rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

config = configparser.ConfigParser()
config.read('config.ini')
url = config.get('Download', 'url')
filename = config.get('Download', 'filename')
tmp_filename = filename + ".tmp"

try:
    print(f"{Fore.BLUE}Starting download...{Style.RESET_ALL}")
    if download_file(url, filename):
        print(f"{Fore.GREEN}Download completed successfully.{Style.RESET_ALL}")

        print(f"{Fore.BLUE}Verifying file...{Style.RESET_ALL}")
        first_checksum = verify_file(filename)
        print(f"{Fore.CYAN}First checksum: {first_checksum}{Style.RESET_ALL}")

        print(f"{Fore.BLUE}Downloading the file again for secondary verification...{Style.RESET_ALL}")
        if download_file(url, tmp_filename):
            print(f"{Fore.GREEN}Second download completed successfully.{Style.RESET_ALL}")

            print(f"{Fore.BLUE}Verifying file again...{Style.RESET_ALL}")
            second_checksum = verify_file(tmp_filename)
            print(f"{Fore.CYAN}Second checksum: {second_checksum}{Style.RESET_ALL}")
            os.remove(tmp_filename)

            if first_checksum == second_checksum:
                print(f"{Fore.GREEN}File verification successful!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}File verification failed. The two downloads do not match.{Style.RESET_ALL}")

except requests.exceptions.RequestException as e:
    print(f"{Fore.RED}Error downloading file: {e}{Style.RESET_ALL}")
except Exception as e:
    print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
