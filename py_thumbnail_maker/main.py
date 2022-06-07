import os
from img_picker import img_picker
from py_thumbnail_maker.path_isExists import handleExists
from resize import resize_img
import asyncio


print("hello dev")

baseImgPath = "src/imgs"
imgName = "E7AB8BE88AB1E99FBF"
imgEx = "jpg"
imgPath = f"{baseImgPath}/{imgName}.{imgEx}"

distPath = "dist"

img_list = img_picker()

print(img_list)

def run():
    for list in img_list:
        p = list["format_path"]
        isExists = os.path.exists(f"dist{p}")
        handleExists(isExists, p)
        resize_img(list["base_path"], list["img_name"], 300, list["format_path"], 90)


run()