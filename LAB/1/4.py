import cv2
import numpy as np

def run(output_path='task4_output.png'):
    size = 800
    img = np.zeros((size, size, 3), dtype=np.uint8)
    center = (size // 2, size // 2)
    outer_radius = int(size * 0.4)
    step = int(outer_radius / 5)
    colors = [(255, 255, 255), (0, 0, 255)]
    for i in range(5):
        r = outer_radius - i * step
        color = colors[i % 2]
        cv2.circle(img, center, r, color, -1)
    tl = (center[0] - outer_radius, center[1] - outer_radius)
    br = (center[0] + outer_radius, center[1] + outer_radius)
    cv2.rectangle(img, tl, br, (0, 255, 0), 2)
    print(f"Canvas center coordinates: {center}")
    cv2.imwrite(output_path, img)

if __name__ == '__main__':
    run()
