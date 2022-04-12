"""
Recreate the images index file in list/comb/
"""

import os


output_folder = "./datadump/raw_images/list/comb"
original_file_folder = "./datadump/raw_images/list/comb (copy)"
data_folder = "./datadump/raw_images/data"

# Retrive original training chunks
with open(os.path.join(original_file_folder, "imageset_train.txt"), 'r') as f:
    original_train = [row.strip() for row in f.readlines()]

# Retrive original test chunks
with open(os.path.join(original_file_folder, "imageset_test.txt"), 'r') as f:
    original_test = [row.strip() for row in f.readlines()]


root_folder = "data"
for chunk in os.listdir(data_folder):
    print(chunk)
# todo depth_list.txt
# todo image_list.txt
# todo imageset_all.txt
# todo imageset_train.txt
# todo imageset_test.txt
