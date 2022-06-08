import os

# make dist dir if dose not exist
def distDirExist():
    isExist = os.path.exists("dist")
    if not isExist:
        os.mkdir("dist")
        print("make dist dir")

# if the dir dose not exist, make the dir
def handleExists(isExist, p):
    if not isExist:
        os.makedirs(f"dist{p}", exist_ok=True)
        print(f"make dir dist{p}")