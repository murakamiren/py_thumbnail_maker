import os
import time
from img_picker import img_picker
from py_thumbnail_maker.path_isExists import distDirExist, handleExists
from resize import resize_img

time_start = time.time()
img_list = img_picker()

print(img_list)

def run():
    distDirExist()
    for list in img_list:
        p = list["format_path"]
        isExists = os.path.exists(f"dist{p}")
        handleExists(isExists, p)
        if list["img_ex"] == "ai":
            print("ai file detected")
        else:
            resize_img(list["base_path"], list["img_name"], 300, list["format_path"], 90, list["img_ex"])
    time_end = time.time()
    processing_time = time_end - time_start
    print(f"all resize done! processing time: {processing_time}")


run()