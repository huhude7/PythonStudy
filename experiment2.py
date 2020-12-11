# coding = utf-8
#




#
#
a,b,c,d = map(int,input().split())
lists = []
count = 0
if a < b and a >0 :
    for i in range(a,b+1):
        if i % c == 0 and i % d != 0 :
            lists.append(i)
        if lists != []:
            for i in lists:
                count += 1
                print(i, end=' ')
                if count % 5 == 0:
                    print('\b')
            print(end='\b')
elif a == b and a>0:
    if a % c == 0 and a % d != 0:
        print(a)




# A,B = input().split()
# A = int(A)
# B = int(B)
# count = 0
# sum = 0
# if -100<=A<=B<=100 :
#     for i in range(A,B+1):
#         print('%5d'%i,end='')
#         count += 1
#         if count % 5 == 0:
#             print(end='\n')
#     for j in range(A,B+1):
#         sum += j
#     if count % 5 !=0:
#         print(end='\n')
#         print('sum=%d'%sum)
#     else:
#         print('sum=%d'%sum)



# n = int(input())
# lists1 = []
# if 1<= n <= 9:
#     for i in range(1,101):     # 之间结尾是n或能被n整除的数的个数
#         if i % 10 == n or i % n == 0 or (i % 10 == n and i % n== 0):
#             lists1.append(i)
# print(len(lists1))
# lists1 = []
# lists2 = []
# str1 = ','
# num = 0
# for i in range(1,39):
#     lists1.append(i)
#
# for i in lists1:
#     print(i,end=',')
#     num += 1
#     if num % 5 == 0 :
#         print()
# hangshu = len(lists1) // 5
# yushu = len(lists1) % 5
# print(hangshu)
# # print(yushu)
# num = 0
# s = []
# for i in range(1, 101):
#     s.append(i)
# # print(s)
# # s = ','.join(s)
# # s = s.split(',')
# # print(s)
# # for i in s:
# #     print(i)
# #     print(i)
#     # num += 1
#     # if num % 5 == 0:
#     #     print()
# for i in range(int(s[0]),int(s[1])+1):
#     num += 1
#     if i<int(s[1]) and num%5!=0:
#         print(i,end=",")
#     elif i==int(s[1]):
#         print(i,end="")
#     else:
#         print(i)


# ls = list(input().split(' '))
# a,b,c,d = ls[0] ,ls[1],ls[2],ls[3]
# x = 1
# for i in range(int(a),int(b)+1 ):
#     if i % int(c) != 0:
#         continue
#     else:
#         if i % int(d) != 0:
#             if x%5 == 0:
#                 print(i,end='\n')
#             else:
#                 print(i,end=' ')
#             x += 1

a,b,c,d=map(int,input().split())
j=0
if a > 0 and a< b:
    for i in range (a,b+1):
        if i%c==0 and i%d!=0 :
            j=j+1
            if j%5==0 and i!=b:      # 每行中的最后一个
                print(i)
            elif i==b :               #全部输出的最后一个
                print(i)
            else :
                print(i,end=' ')    #每一行前四个
elif a == b:
     if a % c == 0 and a % d != 0:
         print(a)


