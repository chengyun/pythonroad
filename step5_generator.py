#列表生成式 generator and map/reduce and lambda
list(range(1, 11))

[x * x for x in range(1, 11)]

[x * x for x in range(1, 11) if x % 2 == 0]

[m + n for m in 'ABC' for n in 'XYZ']


g = (x * x for x in range(10))
next(g)

g = (x * x for x in range(10))
ll = list(g)


g = (x * x for x in range(10))
for x in g:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1 #多个值直接赋值
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)


def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
r #<map object at 0x105167f98>
list(r)

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

from functools import reduce
reduce(lambda x,y:x+y,[1,2,3,4]) #lambda 不能使用return

