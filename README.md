# PortableBlenderManager

PortableBlenderManager simplifies the management of Blender's portable edition by automating setup, execution, and cleanup processes, enhancing user convenience. This tool focuses on clearing data after Blender's use and saving configurations to the script's folder for efficient workflow management.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
  - [Installation Guide](#installation-guide)
  - [How to Run](#how-to-run)
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

Once you have installed PortableBlenderManager, follow these steps to run it:

1. **Running the Downloader Script:**
   - Open Command Prompt.
   - Navigate to the `.archive` folder inside the PortableBlenderManager directory. For example:
     ```
     cd "C:\Users\%username%\Downloads\PortableBlenderManager\.archive"
     ```
   - Run the downloader script to download Blender:
     ```
     python downloader.py
     ```

2. **Starting Blender:**
   - After downloading Blender, navigate back to the main PortableBlenderManager directory and run the startup script:
     ```
     cd ..
     python startup.py
     ```

3. **Other Scripts:**
   - `destroy_session.py`: Completely removes all Blender elements from your system. Use this if you want to entirely uninstall Blender.
     ```
     python destroy_session.py
     ```
   - `reset_settings.py`: Resets Blender settings to their defaults. Useful for troubleshooting or starting fresh.
     ```
     python reset_settings.py
     ```

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

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Batch](https://img.shields.io/badge/Platform-Batch-blue.svg)](https://en.wikipedia.org/wiki/Batch_file)
[![Stable Release](https://img.shields.io/badge/Release-Stable-darkgreen.svg)](https://github.com/VermiNew/PortableBlenderManager/releases/tag/stable)
[![Contributor Friendly](https://img.shields.io/badge/Contributions-Welcome-darkgreen.svg)](https://github.com/VermiNew/PortableBlenderManager/blob/main/CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/VermiNew/PortableBlenderManager.svg)](https://github.com/VermiNew/PortableBlenderManager/stargazers)

## Dependencies

- Python

## License

This project is licensed under the [MIT License](LICENSE).
