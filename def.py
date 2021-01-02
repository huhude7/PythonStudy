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

'''
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

'''

# import time
# print(time.time())
# print(time.process_time())
# print(time.localtime())
# print(time.altzone)

# import calendar
# print(calendar.monthrange(2020,12))
# print(calendar.firstweekday)

# import random
# print(random.random())
# print(random.randrange(0,400,5))
#
#
# random.choice()


# 闭包

# def name(s):
#     def time(t):
#         return s +' will take at '+ t
#     return time
# math = name('math')
# print(math('9:00'))

# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))
# print(time.strftime("%x %X %U %w",time.localtime()))
# # 输出
# # 2020-12-19 16:23:12
# # Sat Dec 19 16:23:12 2020
# # 12/19/20 16:23:12 50 6
# print(time.gmtime())
# print(time.mktime(time.localtime()))
# 1608367527.0
# 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# print(time.altzone)
# print(time.timezone)
# 表示当地时区
# print(time.asctime(time.localtime()))
# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。



# import calendar
# # 中间传递四个参数，第一个为年，第二个为月，第三个为日历每列之间的间隔，第四个为日历每行之间的间隔
# calendar.month(2020,12,5,1)
# 返回指定年份的日历，三个月为一组显示
# # 中间传递四个参数，第一个为年份，第二个为显示的每列之间的间隔，第三个为显示每行之间的间隔，第四个为显示的每个月之间的间隔
# print(calendar.calendar(2020,5,1,1))
# # 中间输入一个年份，如果是闰年返回True，否则为false
# print(calendar.isleap(2020))
# # 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
# print(calendar. firstweekday())
# # 返回在Y1，Y2两年之间的闰年总数。
# print(calendar.leapdays(2010,2020))
# # 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始
# print(calendar.monthcalendar(2020,12))
# # [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 0, 0, 0]]
# # 输出的是一个元组；第一个元素表示该月第一天是周几。 第二个元素表示该月的天数；日从0（星期一）到6（星期日）;月从1到12。
# print(calendar.monthrange(2020,12))
# # 相当于print(calendar.calendar(year,w,l,c))
# calendar.prcal(2020,w=2,l=1,c=6)
# 设置每周的起始日期码。0（星期一）到6（星期日）,使用setfirstweekday（）方法可以查看
# calendar.setfirstweekday(6)
# print(calendar.firstweekday())
# 相当于 print(calendar.month（year，w，l，c））
# calendar.prmonth(2020,12,w=2,l=1)
# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）
# # 返回该日为周几
# print(calendar.weekday(2020,12,12))





import random
# # 用于生成一个0到1的随机浮点数: 0 <= n < 1.0。
# print(random.random())
# # 返回a,b之间的随机浮点数，范围[a,b]或[a,b]取决于四舍五入，a不一定要比b小。
# print(random.uniform(100,64))
# 返回a,b之间的整数，范围[a,b]，注意：传入参数。必须是整数，a一定要比b小。
# print(random.randint(2,6))
# ，可以设置step。只能传入整数
# # 随机返回区间内的一个整数，中间传递三个参数，第一个为起始值，第二个为末尾值，第三个为步长，默认为1
# print(random.randrange(12,86,2))
# # 从可迭代的数据中随机获取一个元素，列表、元组、字符串都属于sequence
# print(random.choice('zhuyongqi'))
# 用于将列表中的元素打乱顺序，俗称为洗牌。
# p = ["Python","is", "powerful","simple"]
# random.shuffle(p)
# print(p)
# 从指定序列中随机获取k个元素作为一个片段返回，sample函数不会修改原有序列.
# 第一个参数传递一个sequnence数据，第二个参数传递一个整型数
# print(random.sample('zhuyongqi',4))

# 闭包
# def name():
#     a = 1;
#     def zhu () :
#         b = a+1
#         return  b
#     return zhu
#
# print(name()())

# 装饰器
# import time
#
# def funct (func) :
#     def wrapper () :
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print(t2-t1)
#     return wrapper
#
# @funct
# def get_sleep():
#     time.sleep(1)
#     print('hello')
# get_sleep()

# def logger(func):
#     # 当确定装饰的函数的形参个数时，内部函数和内部函数调用的函数都要传入形参，
#     # 当不确定装饰的函数的形参的个数时，传入两个不定长参数。
#     def wrapper(*args, **kw):
#         # __name__是系统变量，装饰器参数的__name__是装饰的函数的名称。
#         print(f'我准备开始装饰{func.__name__}函数了:')
#         # 真正执行的是这行。
#         func(*args, **kw)
#     return wrapper
#
# @logger
# def add(x, y):
#     print(f'{x} + {y} = {x+y}')
# add(1,5)


# def dec(func):
#     def wrapper ():
#         print("装饰器函数中的代码")
#         # 装饰带有返回值的函数时，在内部调用函数时返回的是装饰的函数的返回值，所以要使用return返回，才能得到最终的返回值
#         return func()
#     return wrapper
#
# @dec
# def add():
#     return  123
#
# print(add())


# import time
# def timer(func):
#     def wrapper(*args, **kw):
#         t1=time.time()
#         # 这是函数真正执行的地方
#         func(*args, **kw)
#         t2=time.time()
#
#         # 计算下时长
#         cost_time = t2-t1
#         print("花费时间：{}秒".format(cost_time))
#     return wrapper
# @timer
# def want_sleep(sleep_time):
#     time.sleep(sleep_time)
#
# want_sleep(10)

# # 多个装饰器应用在一个函数上，调用顺序是从下至上。
# # 先执行全部装饰器外部函数的代码，执行完后执行从最后一个装饰器开始，执行内层函数的代码
# def dec1(func) :
#     def wrapper ():
#         print("装饰器1嵌套函数")
#         func()
#     print("装饰器1")
#     return wrapper
#
# def dec2 (func) :
#     def wrapper():
#         print("装饰器2嵌套函数")
#         func()
#     print("装饰器2")
#     return wrapper
#
# @dec1
# @dec2
# def add ():
#     print(1+1)
# add()
# from functools import reduce
# a = int(input())
# print(reduce(lambda x,y:x*y,[x for x in range(1,a+1)]))

# 因为装饰器函数中只能传入要使用装饰器的函数作为形参，所以
# 要再在装饰器函数的外层套一层函数，用于传递参数，传入的参数可以在最内层函数中调用
# 注意，除最内层调用函数外，每一层都要加返回值，返回值为向内一层的函数名
# def func_arg(args):
#     def func(function_name):
#         def funcin():
#             print('--记录日志--args=%s'%args)
#             function_name()
#         return funcin
#     return func
# @func_arg('haha')
# def test():
#     print('---test---')
# test()


# ？？？？？？？？？？？
# from functools import reduce
# scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},{'name':'Dennis Ritchie', 'age':76, 'gender':'male'},{'name':'Ada Lovelace', 'age':202, 'gender':'female'},{'name':'Frances E. Allen', 'age':84, 'gender':'female'})
# def group_by_gender(accumulator , value):
#     accumulator[value['gender']].append(value['name'])
#     return accumulator
# grouped = reduce(group_by_gender, scientists, {'male':[], 'female':[]})
# print(grouped)
