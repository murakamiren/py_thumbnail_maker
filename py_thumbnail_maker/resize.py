from PIL import Image
from psd_tools import PSDImage
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

base_dist = "dist"

def psd_format(path, dist_path, img_name):
    p = PSDImage.open(path)
    p.composite().save(f"src/imgs{dist_path}/{img_name}.png")

def resize_img(img_path: str, img_name: str, w: int, dist_path: str, resize_quality: int, img_ex: str):
    if img_ex == "svg":
        drawing = svg2rlg(img_path)
        renderPM.drawToFile(drawing, f"src/imgs{dist_path}/{img_name}.png", fmt="PNG")
    if img_ex == "png":
        img = Image.open(img_path).convert("RGB")
    elif img_ex == "svg":
        img = Image.open(f"src/imgs{dist_path}/{img_name}.png",).convert("RGB")
    elif img_ex == "psd":
        img = Image.open(img_path)
    else:
        img = Image.open(img_path)
    img_w = img.width
    img_h = img.height
    resize_ratio = w / img_w
    resize_size = (w, round(img_h * resize_ratio))
    resized_img = img.resize(resize_size)
    resized_img.save(f"{base_dist}{dist_path}/{img_name}.jpg", quantiles=resize_quality)