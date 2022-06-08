import shutil

from py_thumbnail_maker.path_isExists import makeCopyDir

def ai_to_pdf(path, dist_path, img_name):
    print("ai to pdf...")
    src = path
    copy_dir = f"src/copy/{dist_path}/ai_to_pdf"
    copy = f"{copy_dir}/{img_name}.pdf"
    makeCopyDir(copy_dir)
    shutil.copyfile(src,copy)
    print("done")