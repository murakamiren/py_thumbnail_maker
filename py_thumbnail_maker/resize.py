from pathlib import Path
from PIL import Image
from psd_tools import PSDImage
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from pdf2image import convert_from_path

from py_thumbnail_maker.path_isExists import makeCopyDir

base_dist = "dist"

# pdf to png
def pdf_format(dist_path, img_name):
    print("pdf file convert into png...")
    i = convert_from_path(f"src/copy{dist_path}/ai_to_pdf/{img_name}.pdf")
    i[0].save(f"src/copy{dist_path}/{img_name}.png")
    print("convert done!")

# psd to png
def psd_format(path, dist_path, img_name):
    print("psd file convert into png...")
    p = PSDImage.open(path)
    makeCopyDir(f"src/copy{dist_path}")
    p.composite().save(f"src/copy{dist_path}/{img_name}.png")
    print("convert done!")

def resize_img(img_path: str, img_name: str, w: int, dist_path: str, resize_quality: int, img_ex: str):
    # convert png to be able to resize on PIL
    if img_ex == "svg":
        print("svg file convert into png...")
        drawing = svg2rlg(img_path)
        makeCopyDir(f"src/copy{dist_path}")
        renderPM.drawToFile(drawing, f"src/copy{dist_path}/{img_name}.png", fmt="PNG")
    elif img_ex == "psd":
        psd_format(img_path, dist_path, img_name)
    elif img_ex == "ai":
        pdf_format(dist_path, img_name)

    # png files are RGBA so they need to convert from RGB to save image as jpg
    if img_ex == "png":
        print("png file convert into RGB...")
        img = Image.open(img_path).convert("RGB")
        print("convert done! imported this file as img to resize")
    elif img_ex == "svg":
        print("png file convert into RGB...")
        img = Image.open(f"src/copy{dist_path}/{img_name}.png",).convert("RGB")
        print("convert done! imported this file as img to resize")
    elif img_ex == "psd":
        print("png file convert into RGB...")
        img = Image.open(f"src/copy{dist_path}/{img_name}.png",).convert("RGB")
        print("convert done! imported this file as img to resize")
    elif img_ex == "ai":
        print("png file convert into RGB...")
        img = Image.open(f"src/copy{dist_path}/{img_name}.png",).convert("RGB")
        print("convert done! imported this file as img to resize")
    else:
        print("normal file import...")
        img = Image.open(img_path)
        print("import done!")

    # img size
    img_w = img.width
    img_h = img.height

    # resizing ratio
    resize_ratio = w / img_w
    resize_size = (w, round(img_h * resize_ratio))

    # resize
    resized_img = img.resize(resize_size)

    # save to dist dir
    resized_img.save(f"{base_dist}{dist_path}/{img_name}.jpg", quantiles=resize_quality)
    print(f"resize done!: saved as {base_dist}{dist_path}/{img_name}.jpg")