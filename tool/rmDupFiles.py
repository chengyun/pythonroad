import os

with open("emptylist.txt", "r") as fi:
    while True:
        f = fi.readline()
        if not f:
            break
        f = f.strip()
        print(f)
        os.remove(f)

with open("duplist.txt", "r") as fi:
    while True:
        f = fi.readline()
        if not f:
            break
        f = f.strip()
        print(f)
        os.remove(f)
