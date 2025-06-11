from PIL import Image
import numpy as np
import requests
import os
import sys

STAGING_FILE_PATH = "staging.ggb.screenshot.png"
FINAL_FILE_PATH = "ggb.screenshot.png"
WHITE_THRESHOLD = 0.95
BLACK_THRESHOLD = 0.95
SCAN_HEIGHT = 100
TOLERANCE = 10
WEBHOOK_URL = "https://n8n.boom.box.ca/webhook/a39a038b-cf26-4531-8e49-074f97fc0e71"
WEBHOOK_SECRET = os.environ.get("GGB_WEBHOOK_SECRET")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = "danielraffel/ggb"

def is_white(region, tolerance=TOLERANCE):
    white_pixels = np.all(region >= (255 - tolerance), axis=-1)
    return np.mean(white_pixels)

def is_black(region):
    return np.mean(np.all(region < 20, axis=-1))

def analyze_image(image_path):
    if not os.path.exists(image_path):
        return f"Staging image {image_path} not found"
        
    image = Image.open(image_path).convert("RGB")
    array = np.array(image)

    top_white = is_white(array[:SCAN_HEIGHT])
    bottom_white = is_white(array[-SCAN_HEIGHT:])
    whole_black = is_black(array)

    print(f"Top white ratio: {top_white:.2f}")
    print(f"Bottom white ratio: {bottom_white:.2f}")
    print(f"Overall black ratio: {whole_black:.2f}")

    if top_white > WHITE_THRESHOLD:
        return "Top white bar detected"
    if bottom_white > WHITE_THRESHOLD:
        return "Bottom white bar detected"
    if whole_black > BLACK_THRESHOLD:
        return "All black image detected"
    return None

def get_file_sha(file_path):
    """Get the SHA of a file from GitHub API"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('sha')
    return None

def copy_staging_to_final(staging_path, final_path):
    """Copy staging file content to final file, keeping staging file intact"""
    # Get the content of the staging file
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{staging_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to get staging file: {response.status_code}")
        return False
    
    staging_data = response.json()
    content = staging_data['content']
    
    # Get SHA of existing final file (if it exists)
    final_sha = get_file_sha(final_path)
    
    # Create/update the final file with staging content
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{final_path}"
    payload = {
        "message": "Update screenshot with validated content from staging",
        "content": content
    }
    
    if final_sha:
        payload["sha"] = final_sha
    
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code not in [200, 201]:
        print(f"Failed to update final file: {response.status_code} - {response.text}")
        return False
    
    print("Successfully copied staging image to final")
    return True

def trigger_webhook(reason):
    headers = {
        "x-ggb-auth": WEBHOOK_SECRET,
        "Content-Type": "application/json"
    }
    payload = {"issue": reason}
    try:
        res = requests.post(WEBHOOK_URL, headers=headers, json=payload)
        print(f"Webhook triggered: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"Failed to trigger webhook: {e}")

def main():
    reason = analyze_image(STAGING_FILE_PATH)
    if reason:
        print(f"Issue detected: {reason}")
        trigger_webhook(reason)
        # Don't promote the bad image
    else:
        print("Screenshot passed validation.")
        # Copy staging to final (keeping staging file intact)
        if copy_staging_to_final(STAGING_FILE_PATH, FINAL_FILE_PATH):
            print("Image successfully copied from staging to final.")
        else:
            print("Failed to copy image. Triggering webhook for retry.")
            trigger_webhook("Failed to copy staging image")

if __name__ == "__main__":
    main()
