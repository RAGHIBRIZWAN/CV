import cv2
import numpy as np
import os

def load_or_synth(path=None, size=(800, 600)):
    if path and os.path.exists(path):
        img = cv2.imread(path)
        if img is not None:
            return img
    w, h = size
    img = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (w, h), (200, 200, 200), -1)
    return img

def run(image_path=None, output_path='task6_output.png'):
    img = load_or_synth(image_path)
    h, w = img.shape[:2]
    y_start = int(h * 0.8)
    overlay = np.zeros_like(img)
    overlay[y_start:h, :] = (255, 0, 0)
    blended = cv2.addWeighted(img, 0.7, overlay, 0.3, 0)
    text = 'Sample Title'
    font = cv2.FONT_HERSHEY_SIMPLEX
    (tw, th), _ = cv2.getTextSize(text, font, 1.0, 2)
    tx = (w - tw) // 2
    ty = y_start + (h - y_start + th) // 2
    cv2.putText(blended, text, (tx, ty), font, 1.0, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imwrite(output_path, blended)
    print(f"Saved blended image to {output_path}")

run()
