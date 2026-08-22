import cv2
import numpy as np
import os

def load_or_synth(size=(500, 500), color=(0, 128, 255)):
    w, h = size
    img = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (w, h), color, -1)
    return img

def run(image1_path=None, image2_path=None, output_path='task8_output.png'):
    img1 = cv2.imread(image1_path) if image1_path and os.path.exists(image1_path) else load_or_synth((500, 500), (0, 128, 255))
    img2 = cv2.imread(image2_path) if image2_path and os.path.exists(image2_path) else load_or_synth((500, 500), (128, 0, 200))
    img1 = cv2.resize(img1, (500, 500))
    img2 = cv2.resize(img2, (500, 500))
    mask = np.zeros((500, 500), dtype=np.uint8)
    cv2.circle(mask, (250, 250), 140, 255, -1)
    fg = cv2.bitwise_and(img1, img1, mask=mask)
    inv = cv2.bitwise_not(mask)
    bg = cv2.bitwise_and(img2, img2, mask=inv)
    combined = cv2.bitwise_or(fg, bg)
    cv2.imwrite(output_path, combined)
    print(f"Saved masked composition to {output_path}")

run()
