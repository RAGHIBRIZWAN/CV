import cv2
import matplotlib.pyplot as plt

image_path = "Current-Bugatti.png"
image = cv2.imread(image_path)

if image is None:
    print("Image not found.")
else:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(8, 6))

    plt.imshow(image)

    plt.title(
        "Bugatti",
        fontsize=16,
        color="darkred",
    )

    plt.show()
