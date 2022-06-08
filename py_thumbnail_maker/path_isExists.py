import os

# make dist dir if dose not exist
def distDirExist():
    isExist = os.path.exists("dist")
    if not isExist:
        os.mkdir("dist")
        print("make dist dir")

def makeCopyDir(copy_path):
    isExist = os.path.exists(copy_path)
    if not isExist:
        os.makedirs(copy_path, exist_ok=True)
        print(f"make copy dir {copy_path}")

# if the dir dose not exist, make the dir
def handleExists(isExist, p):
    if not isExist:
        if not p.split("/")[len(p.split("/")) - 1] == "ai_to_pdf":
            os.makedirs(f"dist{p}", exist_ok=True)
            print(f"make dir dist{p}")