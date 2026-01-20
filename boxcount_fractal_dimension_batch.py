import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import glob
import csv

def measure_block_counting(img, box_size):
    block_count = 0
    for i in range(0, img.shape[0], box_size):
        for j in range(0, img.shape[1], box_size):
            block = img[i:i + box_size, j:j + box_size]
            if np.any(block):  # Only count non-empty blocks
                block_count += 1
    return block_count

def differential_box_counting(img, min_box_size=5, num_boxes=20):
    assert len(img.shape) == 2, "Image must be grayscale"
    N = img.shape[0]
    sizes = np.logspace(np.log2(min_box_size), np.log2(N), num=num_boxes, base=2).astype(int)
    counts = []

    for size in sizes:
        block_count = measure_block_counting(img, size)
        counts.append(block_count)

    counts = np.array(counts)
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
    return -coeffs[0]

def process_images_in_folder(folder_path, output_csv):
    # Supported image formats
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.tiff']
    image_paths = []
    for ext in image_extensions:
        image_paths.extend(glob.glob(os.path.join(folder_path, ext)))

    if not image_paths:
        print(f"No images found in folder: {folder_path}")
        return

    # Open CSV file to save results
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image', 'Fractal Dimension'])  # Write header

        for idx, img_path in enumerate(image_paths):
            print(f"Processing image {idx + 1}/{len(image_paths)}: {os.path.basename(img_path)}")
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Error: Unable to read image {img_path}")
                continue

            # Thresholding to extract regions of interest
            _, thresholded = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            # Calculate fractal dimension
            fd = differential_box_counting(thresholded, min_box_size=5, num_boxes=20)
            print(f"Fractal Dimension: {fd:.4f}")

            # Save result to CSV
            writer.writerow([os.path.basename(img_path), fd])

    print(f"Results saved to {output_csv}")

def main():
    folder_path = 'D:/shalegas/17a'  # Replace with your folder path
    output_csv = 'fractal_dimensions.csv'  # Output CSV file name
    process_images_in_folder(folder_path, output_csv)

if __name__ == '__main__':
    main()