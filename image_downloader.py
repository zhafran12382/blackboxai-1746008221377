import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def create_folder(folder_name):
    """Create folder if it doesn't exist"""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def is_valid_image_url(url):
    """Check if URL is valid and points to an image"""
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg', '.ico']
    parsed = urlparse(url)
    return any(parsed.path.lower().endswith(ext) for ext in image_extensions)

def download_images(url):
    """Download all images from the given URL"""
    try:
        # Create images folder
        folder_name = 'images'
        create_folder(folder_name)
        
        # Get webpage content
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        
        if not img_tags:
            print("No images found on the webpage!")
            return
        
        # Download each image
        downloaded = 0
        for img in img_tags:
            # Get image URL
            img_url = img.get('src')
            if not img_url:
                continue
                
            # Make URL absolute
            img_url = urljoin(url, img_url)
            
            # Skip if not valid image URL
            if not is_valid_image_url(img_url):
                continue
            
            try:
                # Download image
                img_response = requests.get(img_url, headers=headers)
                img_response.raise_for_status()
                
                # Generate filename from URL
                file_name = os.path.join(folder_name, os.path.basename(urlparse(img_url).path))
                if not file_name[-4:].lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']:
                    file_name += '.jpg'
                
                # Save image
                with open(file_name, 'wb') as f:
                    f.write(img_response.content)
                
                print(f"Downloaded: {file_name}")
                downloaded += 1
                
            except Exception as e:
                print(f"Error downloading {img_url}: {str(e)}")
                
        print(f"\nDownload completed! Total images downloaded: {downloaded}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("=== Website Image Downloader ===")
    url = input("Enter website URL: ")
    print("\nStarting download...")
    download_images(url)

if __name__ == "__main__":
    main()
