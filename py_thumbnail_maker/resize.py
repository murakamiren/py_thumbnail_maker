from PIL import Image

base_dist = "dist"

def resize_img(img_path: str, img_name: str, w: int, dist_path: str, resize_quality: int, img_ex: str):
    if img_ex == "png":
        img = Image.open(img_path).convert("RGB")
    else:
        img = Image.open(img_path)
    img_w = img.width
    img_h = img.height
    resize_raito = w / img_w
    resize_size = (w, round(img_h * resize_raito))
    resized_img = img.resize(resize_size)
    resized_img.save(f"{base_dist}{dist_path}/{img_name}.jpg", quantiles=resize_quality)