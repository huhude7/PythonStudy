# coding = utf-8

# while 循环


# import random
# yonghu = int(input('请输入0（剪刀），1（石头），2（布）,其他的为退出。:'))
# while yonghu == 0 or yonghu == 1 or yonghu == 2 :
#      diannao = random.randint(0, 2)
#      print('电脑生成的值为%d' % diannao)
#      if yonghu - diannao == -1 or yonghu - diannao == 2:
#          print('电脑赢')
#          yonghu = int(input('请输入0（剪刀），1（石头），2（布）,其他的为退出。:'))
#      elif diannao == yonghu :
#          print('平局')
#          yonghu = int(input('请输入0（剪刀），1（石头），2（布）,其他的为退出。:'))
#      else:
#          print('用户赢')
#          yonghu = int(input('请输入0（剪刀），1（石头），2（布）,其他的为退出。:'))
#
# i = 1
# while i < 6:
#     j= 0
#     while j < i:
#         print('* ',end=' ')
#         # print('i = %d,j = %d'%(i,j),end=' ')
#         j+= 1
#     print('\n')
#     i +=1
#
# i = 1
# while  i<6:
#     print('*'*i)
#     i +=1


# i = 1
# while i < 10:
#     j= 1
#     while j <= i:
#         print('%d*%d =%d'%(j,i,i*j),end=' ')
#         j+= 1
#     print('\n')
#     i +=1





# for循环
# sum = 0
# for i in range(1,101):
#     if i%2 == 0:
#         sum += i
# print(sum)
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d =%-2d'%(j,i,i*j),end=' ')
#     print('\n')

# #
# for i  in range(6):
#     for j in range(0,5-i): 		#打印空格
#            print(' ',end="")
#     for k in range(0,2*i+1):       #打印✳
#     	print('*',end='')
#     print()

for i in range(1,7):
    print(' '*(6-i),'*'*(2*i-1))

# even = []++++++++++++++++++++++++++++++++++++++++++++++++++++++
# odd = []
# for i in range(1,51):
#     if i %2 == 0:
#         even.append(i)
#     else :
#         odd.append(i)
# print(even)
# print(odd)

# print('请分别输入两个数值')
# even = []
# odd = []
# a = int(input('请输入第一个数值:'))
# b = int(input('请输入第二个数值:'))
# if a >b :
#     for i in range(b, a+1):
#         if i %2 == 0:
#             even.append(i)
#         else :
#             odd.append(i)
# elif a<b:
#     for i in range(a, b+1):
#         if i %2 == 0:
#             even.append(i)
#         else :
#             odd.append(i)
# else:
#     print('输入的两个整数之间中间没有整数')
# print(even)
# print(odd)

# for i in 'letter':
#     print('当前字母%s'%i)

# for i in range(1,10):
    # print(i)