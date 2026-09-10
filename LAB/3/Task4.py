import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img_map = cv2.imread("/content/image.webp")

if img_map is None:
    print("Error: image.jpg not found")
else:
    map_height, map_width = img_map.shape[:2]

    # --- The map is hidden: 150px to the LEFT and 80px UP ---
    # To bring it BACK into view, we translate: +150 right, +80 down
    shift_x = 150   # shift right to recover hidden left side
    shift_y = 80    # shift down to recover hidden top side

    # --- 3x3 Homogeneous Translation Matrix ---
    translation_mat_3x3 = np.array([
        [1, 0, shift_x],
        [0, 1, shift_y],
        [0, 0,       1]
    ], dtype=np.float32)

    print("3x3 Translation Matrix:")
    print(translation_mat_3x3)

    print(f"\nOriginal size  : {map_width} x {map_height}")
    print(f"Translation    : tx = +{shift_x} (right), ty = +{shift_y} (down)")
    print(f"Map was hidden : 150px left, 80px up → now restored to frame")

    # --- Extract 2x3 portion for cv2.warpAffine ---
    # (OpenCV uses 2x3, but we built the full 3x3 as required by task)
    affine_mat = translation_mat_3x3[:2, :]  # Take first 2 rows from 3x3

    # --- Apply translation ---
    map_translated = cv2.warpAffine(img_map, affine_mat, (map_width, map_height))

    # --- Convert BGR -> RGB ---
    img_map_rgb        = cv2.cvtColor(img_map,         cv2.COLOR_BGR2RGB)
    map_translated_rgb = cv2.cvtColor(map_translated,  cv2.COLOR_BGR2RGB)

    # --- Display ---
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_map_rgb)
    plt.title("Before: Misaligned Map (X hidden)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(map_translated_rgb)
    plt.title("After: Translated (+150 right, +80 down)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
