from img_picker import img_picker
from resize import resize_img


print("hello dev")

baseImgPath = "src/imgs"
imgName = "E7AB8BE88AB1E99FBF"
imgEx = "jpg"
imgPath = f"{baseImgPath}/{imgName}.{imgEx}"

distPath = "dist"

img_list = img_picker()

print(img_list)

resize_img(imgPath, imgName, 300, distPath, 90)

