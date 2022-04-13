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
undist_imgs = []
chunks_set = []
chunks_train = []
chunks_test = []
for chunk in os.listdir(data_folder):
    current_chunk = os.path.join(data_folder, chunk)

    # get depth file list
    depth_folder = os.path.join(current_chunk, "depths")
    current_depths = [os.path.join(root_folder, os.path.join(chunk, os.path.join("depths", filename))) for filename in sorted(os.listdir(depth_folder))]
    depths.extend(current_depths)

    # get the images list
    undist_imgs_list = os.path.join(current_chunk, "undist_images")
    current_imgs_list = [os.path.join(root_folder, os.path.join(chunk, os.path.join("undist_images", filename))) for filename in sorted(os.listdir(undist_imgs_list))]
    undist_imgs.extend(current_imgs_list)

    # get chunk list
    chunks_set.append(chunk)

    # get training/test chunks list
    if chunk in original_train:
        chunks_train.append(chunk)
    else:
        chunks_test.append(chunk)


# depth_list.txt
with open(os.path.join(output_folder,"depth_list.txt"), "w") as outfile:
    outfile.write("\n".join(depths))

# image_list.txt
with open(os.path.join(output_folder,"image_list.txt"), "w") as outfile:
    outfile.write("\n".join(undist_imgs))

# imageset_all.txt
with open(os.path.join(output_folder,"imageset_all.txt"), "w") as outfile:
    outfile.write("\n".join(chunks_set))

# imageset_train.txt
with open(os.path.join(output_folder,"imageset_train.txt"), "w") as outfile:
    outfile.write("\n".join(chunks_train))

# imageset_test.txt
with open(os.path.join(output_folder,"imageset_test.txt"), "w") as outfile:
    outfile.write("\n".join(chunks_test))
