import timeit
# import numpy

sum_by_for = """
for d in data:
    s += d
"""
sum_by_sum="""sum(data)"""
print(1+2)

print(sum_by_sum)
# pass
print('------------')
def aa(i):
    return (i & (i-1)) == 0

print(aa(32))
print(aa(15))

print(type([1,2,"3"]))
print(type((1,"2")))
print(type({"a" : 1, 2:2}))
print(type(aa))
print(type(timeit))
class MyClass(object):
    pass

print(type(MyClass))
my_class = MyClass()
print(type(my_class))
print(type(type))

# try:
#     print(x)
# except expression as identifier:
#     print("expression")
import string
s = "   asd  "
s2 = "   asd  "
print(s.strip().lower().capitalize)
print(s+s2.strip().upper().lower().capitalize())

try:
    print(s.index("c"))
except ValueError:
    pass

print("Hello World".istitle())
print(str(5))
try:
    print(float(a))
except BaseException:
    pass

print(int('ff',16))
s3= "I love you"
orignalList = s3.split(" ")
print(orignalList)
orignalList.reverse()
print(orignalList)
x=None
if not x:
    print("none")
else:
    print("not none")

for i in range(1,10,2):
    print(i)

def func1(name, *num):
    print(type(num))

func1(1,2,3,4,5)

def func2(name, **kvm):
    print(kvm)
func2("aaa", k=1, k2=2, ke=3) 

ls = [1,2,3,4,{'k':1,'l':2},[1,2,3]]
for i in ls:
    print(i)

# ss = range(0,1000000000,2)
# for s in ss:
#     print(s)

ss2 = [ [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]
print(ss2)
print("-----------------")
def scan(ss3):
    startx = 0
    starty = 0
    endy = len(ss3)
    endx = len(ss3[0])
    print(endy)
    print(endx)
    print("-----------------")
    while((startx < endx) & (starty < endy)):
        for i in range(startx, endx):
            print(ss3[starty][i])

        starty+=1
        print("-----------------")
        for i in range(starty, endy):
            print(ss3[i][endx-1])
        endx-=1
        print("-----------------")
        # print(endx)
        # print(startx)
        for i in range(endx,startx,-1):
            # print(ss3[endy-1][i])
            # print(i-1)
            print(ss3[endy-1][i-1])
        print("-----------------")
        endy -=1
        for i in range(endy,starty,-1):
            # print(i-1)
            print(ss3[i-1][startx])
        startx+=1    





scan(ss2)