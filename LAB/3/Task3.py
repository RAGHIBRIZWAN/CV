import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img_input = cv2.imread("/content/image.webp")

if img_input is None:
    print("Error: image.jpg not found")
else:
    img_height, img_width = img_input.shape[:2]

    # --- Manual 2x2 Shear Matrix ---
    # Negative shear_factor to "push back" the slant (correct a right-leaning shear)
    shear_factor = -0.5  # shear factor: negative = push left to straighten

    # Manual 2x2 shear matrix
    shear_mat_2x2 = np.array([
        [1,  shear_factor],
        [0,   1]
    ])

    print("2x2 Shear Matrix:")
    print(shear_mat_2x2)

    # --- Calculate new canvas width so nothing gets chopped ---
    # When shear_factor is negative, left side shifts; we need extra space on left
    canvas_width = int(img_width + abs(shear_factor) * img_height)

    print(f"\nOriginal size : {img_width} x {img_height}")
    print(f"New width after shear correction: {canvas_width} x {img_height}")

    # --- Build full 2x3 Affine Matrix ---
    # If shear_factor is negative, add an x-offset to shift image back into frame
    x_shift = abs(shear_factor) * img_height if shear_factor < 0 else 0

    affine_mat = np.float32([
        [1,  shear_factor, x_shift],
        [0,   1,                 0]
    ])

    print(f"\nFull 2x3 Affine Matrix applied:")
    print(affine_mat)

    # --- Apply shear correction ---
    img_corrected = cv2.warpAffine(img_input, affine_mat, (canvas_width, img_height))

    # --- Convert BGR -> RGB ---
    img_input_rgb     = cv2.cvtColor(img_input,     cv2.COLOR_BGR2RGB)
    img_corrected_rgb = cv2.cvtColor(img_corrected, cv2.COLOR_BGR2RGB)

    # --- Display ---
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_input_rgb)
    plt.title("Before: Slanted (Sheared) Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(img_corrected_rgb)
    plt.title("After: Shear Corrected (Back to Rectangle)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
