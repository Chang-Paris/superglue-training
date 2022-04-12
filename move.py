import os
import shutil

inputs = "./data"
output = "./data_complete"

for folder in os.listdir(inputs):
  move = 0
  chunk_folder = os.path.join(inputs, folder)
  # subfolder should contain following folders: img_kpts undist_images basenames.txt geolabel
  if not os.path.exists(os.path.join(chunk_folder, "basenames.txt")):
    continue

  # read basenames.txt and get number of lines
  with open(os.path.join(chunk_folder, "basenames.txt"), "r") as f:
    contents = f.readlines()
    nbr_items = len(contents)
    move+=1

  # check if subfolder contains correct number of items
  for item in ["img_kpts", "undist_images", "depths"]:
    item_url = os.path.join(chunk_folder, item)
    if os.path.exists(item_url):
      if len(os.listdir(item_url)) == nbr_items:
        move+=1

  if os.path.exists(os.path.join(chunk_folder, "geolabel")):
      move+=1

  if move == 5:
    output_folder = os.path.join(output, folder)
    shutil.copytree(chunk_folder, output_folder)

