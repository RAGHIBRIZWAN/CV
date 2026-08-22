import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_or_synth(path=None, size=1200):
    if path and os.path.exists(path):
        img = cv2.imread(path)
        if img is not None:
            return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    x = np.linspace(0, 1, size)
    y = np.linspace(0, 1, size)
    xv, yv = np.meshgrid(x, y)
    r = (xv * 255).astype(np.uint8)
    g = (yv * 255).astype(np.uint8)
    b = (((1 - xv) * (1 - yv)) * 255).astype(np.uint8)
    return np.dstack([r, g, b])

def run(image_path=None, output_path='task5_output.png'):
    img = load_or_synth(image_path)
    blurred = cv2.GaussianBlur(img, (25, 25), 0)
    h, w = img.shape[:2]
    cx, cy = w // 2, h // 2
    half = 150
    x1, x2 = cx - half, cx + half
    y1, y2 = cy - half, cy + half
    roi_orig = img[y1:y2, x1:x2]
    roi_blur = blurred[y1:y2, x1:x2]
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(roi_orig)
    axes[0].axis('off')
    axes[0].set_title('Original ROI', fontsize=12, color='black')
    axes[1].imshow(roi_blur)
    axes[1].axis('off')
    axes[1].set_title('Blurred ROI', fontsize=12, color='black')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"Saved comparison to {output_path}")

run()
