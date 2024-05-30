import os
import gdown
import zipfile

# Get the current working directory
current_dir = os.getcwd()
dataset_folder = os.path.join(current_dir, 'downloads')

# Ensure the downloads directory exists
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

# Define the path to download the ZIP file
download_path = os.path.join(dataset_folder, 'data.zip')

# Download the ZIP file from Google Drive using the new link
gdown.download('https://drive.google.com/uc?id=1WqvLT06bbB2b5t3k7_V8VNneBYnOdRIN', 
               output=download_path, 
               quiet=False)

# Unzip the downloaded file
with zipfile.ZipFile(download_path, 'r') as ziphandler:
    ziphandler.extractall(dataset_folder)

print("Download and extraction completed.")
