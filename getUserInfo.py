import os


def read_contents():
    with open(os.getcwd() + "\\userinfo.txt", "r") as f:
        data = f.read().splitlines()
        f.close()
    return data
