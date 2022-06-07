import glob
import os

from path_to_img_info import path_to_img_info

base_path = "src/imgs"

def img_picker():
    img_list = []
    l = glob.glob(f"{base_path}/**/*", recursive=True)
    for f in l:
        if os.path.isfile(f):
            img_list.append(f)
    formatted_img_path = path_to_img_info(img_list)
    return formatted_img_path