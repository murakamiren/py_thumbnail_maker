import glob
import os

base_path = "src/imgs"

def img_picker():
    img_list = []
    l = glob.glob(f"{base_path}/**/*", recursive=True)
    for f in l:
        if os.path.isfile(f):
            img_list.append(f)
    return img_list