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
depths = []
for chunk in os.listdir(data_folder):
    current_chunk = os.path.join(data_folder, chunk)
    depth_folder = os.path.join(current_chunk, "depths")
    current_depths = [os.path.join(root_folder, os.path.join(chunk, os.path.join("depths", filename))) for filename in sorted(os.listdir(depth_folder))]
    depths.extend(current_depths)

with open(os.path.join(output_folder,"depth_list.txt"), "w") as outfile:
    outfile.write("\n".join(depths))
# todo depth_list.txt
# todo image_list.txt
# todo imageset_all.txt
# todo imageset_train.txt
# todo imageset_test.txt
