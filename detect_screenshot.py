from PIL import Image
import numpy as np
import requests
import os
import sys

FILE_PATH = "ggb.screenshot.png"
WHITE_THRESHOLD = 0.95
BLACK_THRESHOLD = 0.95
SCAN_HEIGHT = 100
TOLERANCE = 10  # for near-white pixels
WEBHOOK_URL = "https://n8n.boom.box.ca/webhook/a39a038b-cf26-4531-8e49-074f97fc0e71"
WEBHOOK_SECRET = os.environ.get("GGB_WEBHOOK_SECRET")

def is_white(region, tolerance=TOLERANCE):
    white_pixels = np.all(region >= (255 - tolerance), axis=-1)
    return np.mean(white_pixels)

def is_black(region):
    return np.mean(np.all(region < 20, axis=-1))

def analyze_image(image_path):
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
    reason = analyze_image(FILE_PATH)
    if reason:
        print(f"Issue detected: {reason}")
        trigger_webhook(reason)
    else:
        print("Screenshot passed.")

if __name__ == "__main__":
    main()
