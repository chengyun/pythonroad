import os
import hashlib


def md5(file):
    md5_value = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            md5_value.update(data)
    return md5_value.hexdigest()


def processDir(dirname):
    md5dict = {}
    dupdict = {}
    emptylist = []

    for dirpath, subpaths, files in os.walk(dirname):
        for file in files:
            f = os.path.join(dirpath, file)
            if os.path.getsize(f) <= 0:
                emptylist.append(f)
                continue

            k = md5(f)
            if k not in md5dict:
                md5dict[k] = f
            else:
                dupdict[f] = k
    return md5dict, dupdict, emptylist


def saveFile(filename, content):
    with open(filename, "w") as fo:
        fo.write(content)


def process():
    md5dict, dupdict, emptylist = processDir(".")

    for f in emptylist:
        print("empty:", f)

    for f, k in dupdict.items():
        print("dup:", k, f, "size:", os.path.getsize(f) // (1024 * 1024), "M", "src:", md5dict[k])

    saveFile("emptylist.txt", "\n".join(emptylist))
    saveFile("duplist.txt", "\n".join(dupdict.keys()))


if __name__ == "__main__":
    process()
    print("done")
