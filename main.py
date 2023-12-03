from real_time_object_detection import  object_detection
import json
import os
import pdb

# Path to the main "train" folder
main_folder_path = ".\dataset"
subfolder_name = "Coffeshop"
# Iterate over subfolders in the "train" folder
# for subfolder_name in os.listdir(main_folder_path):
JS_Path = os.path.join(main_folder_path, subfolder_name + "JS")
subfolder_path = os.path.join(main_folder_path, subfolder_name)


# Check if the item in the "train" folder is a directory
# if os.path.isdir(subfolder_path):
# pdb.set_trace()
# Iterate over files in the subfolder
for filename in os.listdir(subfolder_path):
    print(filename)
    # Check if the item is a file (not a subfolder)
    if os.path.isfile(os.path.join(subfolder_path, filename)):
        # Construct the full path to the image file
        image_path = os.path.join(subfolder_path, filename)
        data_annotations = object_detection(image_path)

        filename, extension = os.path.splitext(filename)
        full_path = os.path.join(JS_Path, filename + ".json")
        with open(full_path, "w") as outfile:
            json.dump(data_annotations, outfile)

        # Now, you can use the 'image_path' variable to access the image file
        print(f"Image Path: {image_path}")
# data_annotations = object_detection("./dataset/Coffeshop/001.jpg")
#
# with open("./sample.json", "w") as outfile:
#     json.dump(data_annotations, outfile)



