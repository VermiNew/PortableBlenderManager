# PortableBlenderManager

PortableBlenderManager simplifies the management of Blender's portable edition by automating setup, execution, and cleanup processes, enhancing user convenience. This tool focuses on clearing data after Blender's use and saving configurations to the script's folder for efficient workflow management.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
  - [Installation Guide](#installation-guide)
  - [How to Run](#how-to-run)
    - [Automated Setup](#simplified-setup-process)
    - [Manual Installation](#manual-installation-for-advanced-users)
- [FAQ](#faq)
- [Credits](#credits)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [Badges](#badges)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

PortableBlenderManager offers a streamlined way to manage Blender's portable version, focusing on ease of setup, use, and cleanup. It's designed to save time and improve user experience by handling routine tasks automatically.

**Note:** This tool does not include Blender itself but provides a script to download and manage the portable version of Blender.

## Features

- **Automated Cleanup:** Ensures a clean environment after each Blender session by automatically removing temporary files and data.
- **Configuration Management:** Stores and retrieves Blender configurations directly from the script's folder, allowing for quick setup and consistent user environments.
- **Streamlined Workflow:** Offers a hassle-free experience for Blender users, especially those who frequently move between different systems or need a quick setup.
- **Portable Convenience:** Ideal for users who prefer or require a portable setup, keeping Blender's settings and data contained and easily manageable.

## Usage

### Installation Guide

To install and set up PortableBlenderManager, follow these steps:

1. **Prerequisites:**
   - Ensure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
   - Make sure Python is added to your system's PATH. This is usually an option during the installation of Python.

2. **Download PortableBlenderManager:**
   - Go to the PortableBlenderManager GitHub repository.
   - Click the "Code" button and select "Download ZIP".
   - Save the ZIP file to a convenient location on your computer.

3. **Extract Files:**
   - Locate the downloaded ZIP file.
   - Right-click on the file and choose "Extract All...".
   - Extract the files to a directory of your choice.

4. **Install Required Libraries:**
   - Open Command Prompt.
   - Navigate to the directory where you extracted PortableBlenderManager. For example:
     ```
     cd "C:\Users\%username%\Downloads\PortableBlenderManager"
     ```
   - Install the required Python libraries by running:
     ```
     pip install -r requirements.txt
     ```

### How to Run

After installing PortableBlenderManager, here are the steps to get it up and running:

### Simplified Setup Process

For those who do not have the necessary Python dependencies installed globally, you can still run PortableBlenderManager effortlessly using a prepared batch file. This method is ideal for users seeking a hassle-free setup.

**Instructions:**

1. **Prepare the Batch File:**
   - Make sure there's an `execute.bat` file within your PortableBlenderManager directory. This file is designed to automate the environment setup, install all required dependencies, and execute the necessary scripts for you.

2. **Access Command Prompt Quickly:**
   - Simply navigate to the PortableBlenderManager directory in File Explorer, click on the address bar, type `cmd`, and press `Enter`. This opens Command Prompt directly in the desired directory.

3. **Run the Batch File:**
   - In Command Prompt, start the `execute.bat` by typing its name and hitting `Enter`:
     ```
     execute.bat
     ```

This approach automatically sets up everything needed to run PortableBlenderManager, including the creation of a virtual environment and installation of dependencies, ensuring a smooth start even for those new to Python environments.

### Manual Installation for Advanced Users

For users comfortable with managing Python environments and dependencies:

1. **Download Blender:**
   - Open Command Prompt by typing `cmd` in the File Explorer address bar within the PortableBlenderManager directory.
   - Move to the `.archive` subdirectory:
     ```
     cd ".archive"
     ```
   - Initiate the download script:
     ```
     python downloader.py
     ```

2. **Launch Blender:**
   - Return to the main directory of PortableBlenderManager:
     ```
     cd ..
     ```
   - Start Blender using the startup script:
     ```
     python startup.py
     ```

3. **Utility Scripts:**
   - For complete removal of Blender:
     ```
     python destroy_session.py
     ```
   - To reset Blender settings to defaults:
     ```
     python reset_settings.py
     ```

This manual method provides more control over the installation and running processes of PortableBlenderManager for users with specific requirements or preferences.

## FAQ

**Q: What is PortableBlenderManager?**  
A: PortableBlenderManager is a tool designed to automate the management of Blender's portable version. It simplifies the process of downloading, setting up, and cleaning up Blender, making it more convenient for users who frequently switch between systems.

**Q: How does PortableBlenderManager download Blender?**  
A: The script `downloader.py` located in the `.archive` directory handles the downloading of Blender's portable version. By running this script, users can easily download the latest version available in the repository.

**Q: Does PortableBlenderManager automatically update its repository?**  
A: No, PortableBlenderManager itself does not automatically update its repository. Users can manually change the download URL in the `config.ini` file within the `.archive` folder to get the latest version of Blender. Alternatively, they can wait for an update to the PortableBlenderManager repository, which will include changes or new versions of Blender when available.

**Q: Is PortableBlenderManager free to use?**  
A: Yes, PortableBlenderManager is free and open-source, licensed under the MIT License.

**Q: Can I use PortableBlenderManager on multiple computers?**  
A: Yes, PortableBlenderManager is ideal for users who work with Blender on different systems, as it maintains Blender configurations and data in a portable format.

**Q: Is it safe to use PortableBlenderManager?**  
A: Yes, PortableBlenderManager is safe to use. However, it's always a good practice to scan files using antivirus software and ensure you download from the official repository.

**Q: Can I contribute to PortableBlenderManager?**  
A: Absolutely! Contributions are welcome. Feel free to open an issue or create a pull request on GitHub with your suggestions, bug reports, or code improvements.

**Q: Where can I report a bug or suggest a feature?**  
A: Please report bugs or suggest features through the GitHub Issues page for PortableBlenderManager. Your input is crucial for the tool's improvement.

**Q: Is there a user guide or documentation for PortableBlenderManager?**  
A: Detailed usage instructions are provided in the README.md file. For more specific queries or advanced usage, feel free to open an issue on GitHub.

**Q: Can I use PortableBlenderManager for commercial purposes?**  
A: Yes, PortableBlenderManager is licensed under the MIT License, which permits both personal and commercial use. Make sure to also comply with Blender's licensing terms.

**Q: I'm new to Blender. Will PortableBlenderManager be easy to use?**  
A: PortableBlenderManager is designed to simplify the management of Blender's portable version. While user-friendly, basic knowledge of Blender and its functionalities can be beneficial.

## Credits

- **Blender:** Developed by the Blender Foundation. Visit [Blender.org](https://www.blender.org/) for more information.

- **Script Author:** Michael

## Disclaimer

PortableBlenderManager is an independent project and not affiliated with the Blender Foundation. It's designed to enhance the experience of using Blender's portable version.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

## Badges

[![License: MIT](https://img.shields.io/github/license/VermiNew/PortableBlenderManager.svg?style=flat-square)](LICENSE)
[![Batch](https://img.shields.io/badge/Platform-Batch-blue.svg)](https://en.wikipedia.org/wiki/Batch_file)
[![Python](https://img.shields.io/badge/Platform-Python-orange.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/travis/com/VermiNew/PortableBlenderManager/master.svg?style=flat-square)](https://travis-ci.com/VermiNew/PortableBlenderManager)
[![Coverage Status](https://img.shields.io/codecov/c/github/VermiNew/PortableBlenderManager/master.svg?style=flat-square)](https://codecov.io/gh/VermiNew/PortableBlenderManager)
[![Stable Release](https://img.shields.io/badge/Release-Stable-darkgreen.svg)](https://github.com/VermiNew/PortableBlenderManager/releases/tag/stable)
[![Contributor Friendly](https://img.shields.io/badge/Contributions-Welcome-darkgreen.svg)](https://github.com/VermiNew/PortableBlenderManager/blob/main/CONTRIBUTING.md)
[![GitHub Issues](https://img.shields.io/github/issues/VermiNew/PortableBlenderManager.svg?style=flat-square)](https://github.com/VermiNew/PortableBlenderManager/issues)
[![GitHub Stars](https://img.shields.io/github/stars/VermiNew/PortableBlenderManager.svg?style=social&label=Stars)](https://github.com/VermiNew/PortableBlenderManager/stargazers)

## Dependencies

- Python

## License

This project is licensed under the [MIT License](LICENSE).
