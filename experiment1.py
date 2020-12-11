# coding = utf-8

# 1.
'''
a = int(input())
b = int(input())
if a >= b:
    print('A')
else:
    print('B')
'''
# 2.
'''
a = float(input())
b = float(input())
if a > b:
    print('A')
elif a == b:
    print('B')
else:
    print('C')
'''
# 3.
'''
height = float(input())
weight = float(input())
result = weight / (height * height)
if result < 18:
    print('thin')
elif 18 <= result <25 :
    print('standard')
elif result < 27 and result >= 25:
    print('little fat')
else:
    print('fat')
'''
# 4.
'''
a = int(input())
b = int(input())
print(a+b,a-b,a*b,a/b)
'''
# 5.
'''
a = input()
sum = 0
for i in a:
    i = int(i)
    sum += i**3
a = int(a)
if sum == a:
    print('Yes')
else:
    print('No')
'''
# 6.
'''
r = int(input())
h = int(input())
square = (3.14*r**2)*h
print(square)
'''
# 7.
'''
year = int(input())
# 能被四整除，不能被100整除，或者能被400整除
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('%s是闰年'%year)
else:
    print('不是闰年')
'''
# 8.
'''
x = float(input())
if 0.4<= x <1.4:
    y = 1 - 2*x
    print(y)
elif 2.4<= x <4.4:
    y = x
    print(y)
elif 5.4<= x <6.4:
    y = 1 + 2*x
    print(y)
'''
# 9.素数和孪生素数
'''
import math
x,y = input().split()
x = int(x)
y = int(y)
li = []
if x >= y :
    print('illegal')              
else:
    for i in range(x, y+1):          
        flag = True
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j == 0:
                flag =False
                break
        if flag and i >1 :          # 1不是素数，2是素数
            li.append(i)
 
for i in range(0,len(li)-1):
    if li[i]  == li[i+1] - 2 :
        print(li[i],li[i+1])

'''

# 10.杨辉三角

n= int(input())
if n < 2:
    print(1)
else:
    print(1)
    print(1,1)
    list1 = [1,1]
    for i in range(3,n+1):
        list2 = []
        list2.append(1)
        print(list2[0],end=' ')
        for j in range(1,i-1):
            list2.append(list1[j-1]+list1[j])
            print(list2[j],end=' ')
        list2.append(1)
        print(list2[-1])
        list1 = list2













