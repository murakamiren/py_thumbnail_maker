from resize import resize_img


print("hello dev")

baseImgPath = "src/imgs"
imgName = "E7AB8BE88AB1E99FBF"
imgEx = "jpg"
imgPath = f"{baseImgPath}/{imgName}.{imgEx}"

distPath = "dist"

resize_img(imgPath, imgName, 300, distPath, 90)