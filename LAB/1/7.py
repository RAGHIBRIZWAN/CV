import cv2
import numpy as np
import os

def load_or_synth(path=None, size=(800, 600)):
    if path and os.path.exists(path):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            return img
    w, h = size
    img = np.full((h, w), 255, dtype=np.uint8)
    cv2.putText(img, 'TEST', (50, h//2), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,), 10, cv2.LINE_AA)
    return img

def rotate_image(img, angle, scale=0.8):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=255)

def run(image_path=None, output_path='task7_output.png'):
    img = load_or_synth(image_path)
    _, th_global = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    th_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    th_adapt_rot = rotate_image(th_adaptive, 45, 0.8)
    combined = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    stacked = np.hstack([cv2.cvtColor(th_global, cv2.COLOR_GRAY2BGR), cv2.cvtColor(th_adaptive, cv2.COLOR_GRAY2BGR), cv2.cvtColor(th_adapt_rot, cv2.COLOR_GRAY2BGR)])
    cv2.imwrite(output_path, stacked)
    print(f"Saved thresholds comparison to {output_path}")

run()
