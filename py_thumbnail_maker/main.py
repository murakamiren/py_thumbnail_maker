import os
import time
from img_picker import img_picker
from py_thumbnail_maker.ai_to_pdf import ai_to_pdf
from py_thumbnail_maker.path_isExists import distDirExist, handleExists, makeCopyDir, makeSrcCopy
from resize import resize_img

time_start = time.perf_counter()
img_list = img_picker()

# print(img_list)

def run():
    distDirExist()
    makeSrcCopy()
    for list in img_list:
        p = list["format_path"]
        isExists = os.path.exists(f"dist{p}")
        handleExists(isExists, p)
        if list["img_ex"] == "ai":
            print("ai file detected")
            ai_to_pdf(list["base_path"], list["format_path"], list["img_name"])
        elif list["img_ex"] == "pdf":
            print("raw pdf detected")
            print(list)
            continue
        resize_img(list["base_path"], list["img_name"], 300, list["format_path"], 90, list["img_ex"])

    time_end = time.perf_counter()
    processing_time = round(time_end - time_start, 2)
    print(f"all resize done! processing time: {processing_time}")


run()