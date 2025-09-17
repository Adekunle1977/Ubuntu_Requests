import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_images():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Default test URLs (2 images)
    default_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg",
        "https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png"
    ]

    # Ask user for multiple URLs
    urls = input("Please enter one or more image URLs (comma-separated),\n"
                 "or press Enter to use default URLs: ").strip()

    if not urls:
        urls = default_urls
    else:
        urls = [u.strip() for u in urls.split(",") if u.strip()]

    # Create directory if not exists
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    for url in urls:
        try:
            # Download with headers to avoid 403 errors
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/140.0.0.0 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)

            # ✅ must call the function with ()
            response.raise_for_status()

            # Check content type is an image
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipped (not an image): {url}")
                continue

            # Check file size (limit 5MB)
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 5 * 1024 * 1024:
                print(f"✗ Skipped (too large > 5MB): {url}")
                continue

            # Extract filename
            parsed = urlparse(url)
            filename = os.path.basename(parsed.path)
            if not filename:
                filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

            filepath = os.path.join(folder, filename)

            # Avoid duplicates
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(filepath):
                filename = f"{base}_{counter}{ext}"
                filepath = os.path.join(folder, filename)
                counter += 1

            # Save image
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.MissingSchema:
            print(f"✗ Invalid URL format: {url}")
        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP error for {url}: {e}")
        except requests.exceptions.ConnectionError:
            print(f"✗ Connection failed for {url}")
        except requests.exceptions.Timeout:
            print(f"✗ Request timed out for {url}")
        except Exception as e:
            print(f"✗ Unexpected error for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    fetch_images()
