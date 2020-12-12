# 1
# 0，1，1，2，3，5，8，13，21，34，55，89，144
'''
n = int(input())
def fib(n):
    if n==1 :
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))
'''



# 2
'''
num1,num2 = map(int,input().split( ))
lis1 = []
lis2 = []
lis3 = []
for i in range(1,num1+1):
    if num1 % i == 0:
        lis1.append(i)
for i in range(1,num2+1):
    if num2 % i == 0:
        lis2.append(i)
for i in lis1:
    if i in lis2:
        lis3.append(i)
lis3 = sorted(lis3,reverse=True)
print(lis3[0])
'''
'''
a,b = map(int,input().split( ))
def find_divisor(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return find_divisor(b,a%b)
print(find_divisor(6,8))
'''


# 4  a * (1 + b)**c - a

'''
a,b,c = map(float,input().split())
def singleProfit(a,b,c):
    return round(a * b * c ,1)
def doubleProfit(a,b,c):
    return round(a * (1 + b)**c - a ,1)
print(singleProfit(a,b,c))
print(doubleProfit(a,b,c))
'''

# # 5
n = float(input())
def getResult(n):
    if n == 0:
        return 0
    else:
        return ((-1)**(n-1))*1/((n+1)*n) + getResult(n-1)

print(getResult(n))