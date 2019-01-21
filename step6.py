# file 简单文件操作

# 可能因为异常导致未关闭文件
file = open("tmp/foo.txt")
data = file.read()
file.close()

file = open("tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()

with open("tmp/foo.txt") as file:
    data = file.read()

# 基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。


with open("tmp/in.txt", 'r') as file:
    # data = file.read()
    # line = file.readline()
    lines = file.readlines()

lines = map(lambda x: x.strip(), lines)  # 去换行符
lines = list(lines)
content = '\n'.join(lines)
with open("tmp/out.txt", 'w') as outfile:
    outfile.write(content)

# 中文问题 需明确编码
import codecs

with codecs.open("tmp/中文.txt", 'r', encoding='utf-8') as file:
    content = file.read()
print(content)
with codecs.open("tmp/out.txt", 'w', encoding='utf-8') as outfile:
    outfile.write(content)


import chardet

with open("tmp/中文.txt", 'rb') as file:
    data = file.read()
    charInfo = chardet.detect(data)  # {'confidence': 0.99, 'encoding': 'utf-8'}
    print(charInfo)
    content = data.decode(encoding=charInfo['encoding'])
    print(content)
