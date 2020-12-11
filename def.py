# def addNum (a,b):
#     return a+b
#
# print(addNum())

# def sushu (num = int(input())) :
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     if num > 2:
#         for i in range(2, num):
#             flag = ''
#             if num % i == 0:
#                 flag = True
#         if flag:
#                 return True
#         else:
#                 return False
# print(sushu())

'''
lis = []
def addName():
    name = input('输入要添加的名字')
    lis.append(name)
def delName():
    name = input('输入要删除的名字')
    num = lis.index(name, 0, len(lis))
    del lis[num]
def changeName():
    name1 = input('做出修改的名片:')
    name2 = input('修改为:')
    num = lis.index(name1, 0, len(lis) - 1)
    lis[num] = name2
def searchName ():
    name = input('输入要查询的名字')
    if name in lis:
        print(name)
    else:
        print('查无此人')
def displayAll ():
    for i in lis:
        print(i,end=',')
        print()
def quit ():
    flag = False
    print('成功退出系统')
def displayMenu():
    flag = True
    while flag:
        print('-'*30)
        print('名片管理系统')
        print('1.添加名片')
        print('2.删除名片')
        print('3.修改名片')
        print('4.查询名片')
        print('5.获取所有名片信息')
        print('6.退出系统')
        print('-'*30)
        inputNum = int(input('输入要执行的程序:'))
        if inputNum == 1:
            addName()
        if inputNum == 2:
            delName()
        if inputNum == 3:
            changeName()
        if inputNum == 4:
            searchName()
        if inputNum == 5:
            displayAll()
        if inputNum == 6:
            quit()
displayMenu()
'''

#
# name_list=[]
# def display_menu():
#     print('-'*30)
#     print("名片管理系统 V1.0")
#     print("1. 添加名片")
#     print("2. 删除名片")
#     print("3. 修改名片")
#     print("4. 查询名片")
#     print("5. 获取所有名片信息")
#     print("6. 退出系统")
#     print('-' * 30)
# def get_choice():
#     return int(input("请输入选择的序号："))
# def add_info():
#     name_list.append(input("请输入添加姓名："))
# def del_info():
#     n =input("请输入要删除的姓名：")
#     while n in name_list:
#         name_list.remove(n)
# def update_info():
#     old = input("请输入要修改的姓名：")
#     new = input("请输入修改后的姓名：")
#     for i in range(len(name_list)):
#         if name_list[i]== old:
#             name_list[i] =new
# def select_info():
#     n=input("请输入要查询的姓名关键字：")
#     for i in range(len(name_list)):
#         if n in name_list[i]:
#             print(name_list[i])
# def print_all():
#     print("-"*30)
#     for info in name_list:
#         print(info)
#     print("-" * 30)
# while True:
#     display_menu()
#     k = get_choice()
#     if k==1:
#         add_info()
#     elif k==2:
#         del_info()
#     elif k==3:
#         update_info()
#     elif k==4:
#         select_info()
#     elif k==5:
#         print_all()
#     elif k==6:
#         break
#     else:
#         print("输入错误，请重新输入")
#


#
# num1,num2,num3 = int(input().split(' '))
# lis = []
# lis.append(num1)
# lis.append(num2)
# lis.append(num3)
# lis.sort()
# print(lis)



# lis = []
# for i in range(3):
#     if i < 3:
#         num = float(input())
#         lis.append(num)
# lis = sorted(lis)
# if lis[0] + lis[1] > lis[2]:
#     print('yes')
# else:
#     print('no')

# # 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]
#
#
# # 列表
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#
# # 指定第二个元素排序
# random.sort(key=takeSecond)
#
# # 输出类别
# print('排序列表：', random)


# nonlocal b
# b = 100
# print(b)
# def test():
#     global a
#     a = 20
#     print(a)
# test()
# print(a)
# # print('a的值是%d'%a)


# def func(count):
#     if count == 0:
#         return 1
#     else:
#         return 1/(1*2) + 1/(3*4) + 1/(5*6)
# print(func())


# def func(count):
#     if count==0:
#         return 0
#     else:
#         result= ((-1)**(count-1)) / (count * (count+1)) + func(count-1)
#     return result
# number=int(input('请输入一个正整数：'))
# print(func(number))
#
# bookinfo = [('不一样的卡梅拉',22.5,30),("零基础学Python",65.1,28),('摆渡人',29,29),('福尔摩斯探案全集',22.5,128)]
# print("爬取到的商品信息：\n",bookinfo,'\n')
# bookinfo.sort(key=lambda x:(x[2],x[1]/x[2]))
# # print('排序后的商品信息：\n',bookinfo)
#
# import time
# print(time.perf_counter())
# print(time.process_time())
#
# print(time.time())

import time
# def proc():
#     a = 0
#     for i in range(10000000):
#         a += 1
# t0 = time.process_time()
# t_0 = time.time()
# proc()
# t1 = time.process_time()
# t_1 = time.time()
# print("cpu time is %f"%(t1-t0))
# print("wall time is %f"%(t_1-t_0))


# # localtime方法返回值是当地的时间，格式为time下的struct_time对象
# print(time.localtime())
# # time.struct_time(tm_year=2020, tm_mon=12, tm_mday=5, tm_hour=19, tm_min=57, tm_sec=10, tm_wday=5, tm_yday=340, tm_isdst=0)
# # 可以通过打点调用其中具体的值
# print(time.localtime().tm_wday)
# 第一个参数传递格式，第二个参数传递表示时间的struct_time对象
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
time_word = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(time_word,"%a %b %d %H:%M:%S %Y")))

















