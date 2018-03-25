#list tuple set dict常规操作 与判断、循环语法

#list
a = ['a',0,1,2,3]
a.append(5)
a.insert(5,4)
a.pop(5)
a.pop(0)
len(a)
a.sort()



b = ('a','b','c')

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Bob']
#d['Alice'] #error

d.get('Alice') #none
d.get('Alice',60)

d['Jone'] = 99
'Thomas' in d
d.pop('Bob')

s = set([1, 2, 3])
s.add(4)
s.add(4)
s.remove(4)

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
print("done")

for i in range(10):#不含10
    print(i)

for i in range(0,10,2):
    print(i)

i = 0
while i<10:
    i= i+1#不支持i++
    if i==3:
        continue
    print(i)
    if i==7:
        break
else:
    print('while else')
print(i)

for x in a:
    print(x)

for x in b:
    print(x)

for x in d.keys():
    print(x)

for x in d.values():
    print(x)

for x in d.items():
    print(x[0],'=>', x[1])

for x in s:
    print(x)

for k,v in enumerate(a):
    print(k,'=>',v)

for k,v in enumerate(b):
    print(k,'=>',v)

for k,v in d.items():
    print(k,'=>',v)

for k,v in enumerate(s):
    print(k,'=>',v)
