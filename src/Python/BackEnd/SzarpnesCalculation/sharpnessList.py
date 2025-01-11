import os
import re
import numpy
from skimage import filters, color, feature
from Python.BackEnd.SzarpnesCalculation.sharpnessMetrics import *
import matplotlib.pyplot as plt


def extract_integer(filename):
    match = re.search(r"1_([+-]?[0-9.]+)_([0-9.]+)\.([0-9.]+)\.png", filename)
    if match:
        return int(match.group(1))
    else:
        return None


def list_files_sorted_by_integer(folder_path):
    files = os.listdir(folder_path)
    png_files = sorted([file for file in files if file.endswith('.png')], key=extract_integer)
    return png_files


def calculate_sharpness(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # sharpness=edge_based_sharpness(img)
    # sharpness=lpc_based_sharpness(img)
    sharpness = image_sharpness2(img)
    return sharpness


def plot_sharpness(image_paths, sharpness_values):
    plt.figure(figsize=(10, 6))
    plt.bar(image_paths, sharpness_values, color='blue')
    plt.xlabel('Image')
    plt.ylabel('Sharpness')
    plt.title('Sharpness of Images')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def main(folder_path):
    image_paths = []
    sharpness_values = []

    sorted_files = list_files_sorted_by_integer(folder_path)
    # Calculate sharpness for each image
    for i, image_file in enumerate(sorted_files):
        print(i)
        image_path = os.path.join(folder_path, image_file)
        sharpness = calculate_sharpness(image_path)
        image_paths.append(image_file)
        sharpness_values.append(sharpness)

    # Plot the results
    plot_sharpness(image_paths, sharpness_values)

if __name__ == '__main__':
    folder_path = '..\\dane\\filmik'
    main(folder_path)
