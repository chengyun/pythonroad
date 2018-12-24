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

    for dir_path, subpaths, files in os.walk(dirname):
        for file in files:
            f = os.path.join(dir_path, file)
            if os.path.getsize(f) <= 0:
                emptylist.append(f)
                continue

            k = md5(f)
            if md5dict.get(k) is None:
                md5dict[k] = f
            else:
                dupdict[f] = k
    return md5dict, dupdict, emptylist


def saveFile(filename, content):
    with open(filename, "w") as fo:
        fo.write(content)


md5dict, dupdict, emptylist = processDir(".")

for f in emptylist:
    print("empty:", f)

for f, k in dupdict.items():
    print("dup:", k, f, "size:", os.path.getsize(f) // (1024 * 1024), "M", "src:", md5dict[k])

saveFile("emptylist.txt", "\n".join(emptylist))
saveFile("duplist.txt", "\n".join(dupdict.keys()))
