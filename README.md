
Built by https://www.blackbox.ai

---

```markdown
# Website Image Downloader

## Project Overview
Website Image Downloader is a Python script that allows users to download all images from a specified webpage. It uses the Requests library to fetch webpage content and BeautifulSoup to parse the HTML and locate image tags. This tool is helpful for users who want to save images from various websites quickly.

## Installation
To set up the project, ensure you have Python installed on your machine. You will also need to install the required dependencies.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/website-image-downloader.git
   cd website-image-downloader
   ```

2. Install the required Python packages. It's recommended to create a virtual environment before installing:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install requests beautifulsoup4
   ```

## Usage
To use the Website Image Downloader, run the script and input the desired webpage URL when prompted.

1. Launch the script:
   ```bash
   python image_downloader.py
   ```

2. When prompted, enter the URL of the website from which you want to download images.

3. The images will be downloaded to a folder named `images` within the project directory.

## Features
- Automatically creates a directory to store downloaded images.
- Validates image URLs to ensure only images are downloaded.
- Handles various image file formats including PNG, JPG, GIF, and more.
- Displays error messages for any issues that arise during the download process.
- Provides feedback on the number of images successfully downloaded.

## Dependencies
The project requires the following Python packages:
- `requests`: For making HTTP requests to fetch webpage content.
- `beautifulsoup4`: For parsing HTML and extracting image tags.

You can install all dependencies by running:
```bash
pip install -r requirements.txt
```
*Note: If a `requirements.txt` file is not present in your project, it's okay to install the packages manually as instructed.*

## Project Structure
```
/website-image-downloader
│
├── image_downloader.py   # Main script for downloading images from a webpage
└── images                 # Folder where downloaded images will be stored
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to this project or report any issues you encounter! Happy downloading!
```