import cv2
import numpy as np
import pandas as pd
import os

def load_or_synth(path=None, size=(400, 400)):
    if path and os.path.exists(path):
        img = cv2.imread(path)
        if img is not None:
            return img
    w, h = size
    img = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (w, h), (50, 150, 200), -1)
    cv2.circle(img, (w//2, h//2), 80, (200, 50, 100), -1)
    return img

def run(image_path=None, output_csv='task9_pixels.csv'):
    img = load_or_synth(image_path)
    b = img[:, :, 0].flatten()
    g = img[:, :, 1].flatten()
    r = img[:, :, 2].flatten()
    df = pd.DataFrame({'Red': r, 'Green': g, 'Blue': b})
    desc = df.describe()
    print(desc)
    df.to_csv(output_csv, index=False)
    print(f"Wrote flattened pixel CSV to {output_csv}")

run()
