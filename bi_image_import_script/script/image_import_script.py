# Copyright 2023 bitigloo <http://www.bitigloo.com>
# License GPL-3.0 or laterGPL-3 or any later version (https://www.gnu.org/licenses/licenses.html#LicenseURLs).

import os
import base64
import csv

# Define the directories
csv_directory = "directory where the csv file must be created"
image_directory = os.path.join(csv_directory, "images directory")


def image_convert_b64():
    csv_data = []
    for root, dirs, files in os.walk(image_directory):
        for index, file in enumerate(files, start=1):
            with open(os.path.join(root, file), "rb") as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
            csv_data.append([index, file, file, file, img_base64])

    return csv_data


def create_csv(csv_data):
    csv_file_path = os.path.join(csv_directory, 'image_import.csv')

    # Note: a developer can simply map the external ids with the provided infos
    fields = ['No.', 'external_id', 'name', 'reference', 'image_1920']

    # Check if the CSV file exists, and write the header only if it doesn't
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fields)

    # Append the image data to the CSV file
    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_data)


if __name__ == "__main__":
    image_data = image_convert_b64()
    create_csv(image_data)
