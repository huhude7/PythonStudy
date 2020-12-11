# s1= input()
# s2 =input()
# s1 = s1.replace(s2.upper(),'')
# s1 = s1.replace(s2.lower(),'')
# print(s1)

# s = input().split(' ')
# a = ''
# for index,item in enumerate(s) :
#     a += item[::-1]
#     if index < len(s)-1:
#         a += ' '
# print(a)


# nums = input().split()
# lis = []
# a= ''
# for i in nums:
#     i = int(i)
#     if i != 1 and i > 0:
#         for j in range(2,i):
#             if i % j == 0:
#                 lis.append(i)
#                 break
#     else:
#         lis.append(i)
# for index,item in enumerate(lis) :
#     a += str(item)
#     if index < len(lis)-1:
#         a += ' '
# print(a)



# num = int(input())
# dic = {}
# lis = []
# for i in range(num):
#         name, age = input().split(' ')
#         if name not in dic:
#             dic[name] =age
# for keys,values in dic.items():
#     values = int(values)
#     if values > 60:
#         lis.append(keys)
# for i in lis:
#     del dic[i]
# for keys,values in dic.items():
#     print(keys,values)


# num = int(input())
# dic = {}
# lis = []
# for i in range(num):
#         stuid, name = input().split(' ')
#         if stuid not in dic :
#             dic[stuid] = name
# for items in dic.items():
# #     items= list(items)
#     lis.append(items)
#     lis.sort()
# for i in lis:
#     print(i[0],i[1])
