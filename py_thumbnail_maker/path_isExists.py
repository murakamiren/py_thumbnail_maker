import os


def handleExists(isExists, p):
    if not isExists:
        os.makedirs(f"dist{p}", exist_ok=True)
        print(f"make dir dist{p}")