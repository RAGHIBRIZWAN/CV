import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("/content/image.webp")

if image is None:
    print("Error: Image could not be loaded.")
else:
    # --- Build 2x2 Scaling Matrix manually ---
    scale_x = 3.0  # 300% on x-axis
    scale_y = 3.0  # 300% on y-axis

    # Manual 2x2 scaling matrix
    scaling_matrix = np.array([
        [scale_x, 0],
        [0,       scale_y]
    ])
    print("2x2 Scaling Matrix:")
    print(scaling_matrix)

    # --- Apply scaling using cv2.resize (equivalent to applying the matrix) ---
    scaled = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

    # --- Calculate centering offsets ---
    original_h, original_w = image.shape[:2]
    scaled_h, scaled_w = scaled.shape[:2]

    # How much the image grew
    offset_x = (scaled_w - original_w) / 2
    offset_y = (scaled_h - original_h) / 2

    print(f"\nOriginal size : {original_w} x {original_h}")
    print(f"Scaled size   : {scaled_w} x {scaled_h}")
    print(f"Offset to keep centered — X: {offset_x}, Y: {offset_y}")

    # --- Convert BGR to RGB for display ---
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    scaled_rgb = cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB)

    # --- Plot side by side ---
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(scaled_rgb)
    plt.title("Scaled Image (300% x 300%)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
