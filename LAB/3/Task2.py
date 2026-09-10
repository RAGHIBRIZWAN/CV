import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("/content/image.webp")

if img is None:
    print("Error: image.jpg not found")
else:
    h, w = img.shape[:2]

    # --- Manual 2x2 Rotation Matrix (45 degrees) ---
    theta_deg = 45
    theta_rad = np.deg2rad(theta_deg)  # Convert to radians

    c = np.cos(theta_rad)
    s = np.sin(theta_rad)

    # Manual 2x2 rotation matrix
    rot_2x2 = np.array([
        [c, -s],
        [s,  c]
    ])

    print("2x2 Rotation Matrix (45°):")
    print(rot_2x2)

    # --- Manually Calculate New Dimensions (so corners don't get chopped) ---
    # New width and height after rotation
    out_w = int(abs(w * c) + abs(h * s))
    out_h = int(abs(w * s) + abs(h * c))

    print(f"\nOriginal size : {w} x {h}")
    print(f"New size after rotation: {out_w} x {out_h}")

    # --- Build Full 2x3 Affine Matrix with centering offset ---
    # Shift so the rotated image stays centered in the new canvas
    mid_x = w / 2
    mid_y = h / 2

    shift_x = (out_w / 2) - (c * mid_x - s * mid_y)
    shift_y = (out_h / 2) - (s * mid_x + c * mid_y)

    # Full affine matrix (2x3): rotation + translation
    transform_matrix = np.array([
        [c, -s, shift_x],
        [s,  c, shift_y]
    ])

    # --- Apply rotation with new canvas size ---
    result = cv2.warpAffine(img, transform_matrix, (out_w, out_h))

    # --- Convert BGR -> RGB for display ---
    img_rgb    = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    # --- Display ---
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Before: Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result_rgb)
    plt.title("After: Rotated 45° (No Cropping)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
