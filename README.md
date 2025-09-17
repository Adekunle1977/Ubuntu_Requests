# Ubuntu_RequestsUbuntu-Inspired Image Fetcher

"I am because we are" – Ubuntu philosophy

This project is a Python script that downloads images from the internet in the spirit of Ubuntu: community, sharing, and respect.

The program allows you to:

Enter one or multiple image URLs

Or just press Enter to use the provided default URLs

Download and save the images inside a Fetched_Images folder

Avoid duplicate files by renaming them automatically

Handle errors gracefully (bad links, timeouts, large files, etc.)

Check HTTP headers to make sure only safe images are saved

Features

✅ Multiple URL support (comma-separated input)
✅ Default URLs (Ubuntu wallpaper + logo)
✅ Prevents duplicate file names
✅ Skips non-image links
✅ Skips files larger than 5 MB
✅ User-Agent headers added (to avoid 403 Forbidden errors)
✅ Clean terminal messages in Ubuntu style

Requirements

Python 3.7 or later

Install the required library:

pip install requests

How to Run

Clone this repository or copy the script.

Open your terminal or PowerShell in the project folder.

Run:

python Fetched_image.py


When prompted:

Enter one or more image URLs (separated by commas), or

Just press Enter to use the default test URLs.

Example Run
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (comma-separated),
or press Enter to use default URLs: 

✓ Successfully fetched: Fronalpstock_big.jpg
✓ Image saved to Fetched_Images/Fronalpstock_big.jpg
✓ Successfully fetched: ubuntu-logo32.png
✓ Image saved to Fetched_Images/ubuntu-logo32.png

Connection strengthened. Community enriched.

Ubuntu Principles in the Code

Community → Connects to the wider web to fetch images

Respect → Handles errors gracefully

Sharing → Saves images neatly for later use

Practicality → Useful tool for mindful downloading

Repository Name

When submitting, push this project to GitHub in a repo called:

Ubuntu_Requests
