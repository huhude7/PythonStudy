# nameList = ['xiaoming','xianzhaong','xiaohua','xiaoming']
# delName = input()
# if delName in nameList:
#     for i in nameList:
#         if i == delName:
#             nameList.remove(i)
#     print(nameList)
# else:
#     print('not found')

# while delName in nameList:
#     nameList.remove(delName)
# print(nameList)
# nameList = ['xiaoming','xianzhaong','xiaohua','xiaoming']
# 将列表按升序排列
# numList = [1,2,3,4,5,6,7]
# # nameList.sort()
# print(sorted(numList,key=str.lower()))
# print(numList)
# # 当reverse属性值为true时，对列表进行降序排列
# nameList.sort(reverse=True)
# # 使用reverse方法，对列表的原有的顺序进行反转
# nameList.reverse()
# num = [4,5,2,7,5,6]
# for index,value in enumerate(num,1):
#     print ('%s %s' % (index,value))

# import random
# # ranNum = random.randint(0,2)
# names = ['a','b','c','d','e','f','g','h']
# offices = [[],[],[]]
# for i in names :
#     offices[random.randint(0,2)].append(i)
# for i in offices:
#     print('')

# nums = [1,343,456,7,345,6,74524,2]
# # 返回值为列表中个元素的累加和
# print(sum(nums))

# import random
# # 前一部分是列表中每个元素需要满足的条件，后一部分表示列表的长度
# ranNum = [random.randint(10,100) for i in range(10)]
# print(ranNum)


# price = [1200,5330,2988,6200,1998,8888]
# 还可以使用三部分来定制条件，后边加上条件表达式
# sale = [x for x in price if x>5000]
# print("价格高于5000的：",sale)

# lis = [x for x in range(1,101) if x % 2 == 0]
# print(lis)

# s = input()
# a = ''
# b = ''
# for index,item in enumerate(s):
#     if index % 2 == 0:
#         a += item
#     else:
#         b += item
# c = a+b
# print(c)
# #
# #
# A = ''
# B =''
# for i in range(len(c)):
#     if i <= round(len(c)/2):
#         A += c[i]
#     else:
#         B += c[i]
# d = ''
# for index,item in enumerate(A):
#     d += item
#     if index < len(B):
#         d += B[index]
# print(d)

# 列表生成式
# 生成指定范围的数值列表
# 根据列表生成制定需求的列表
# 从列表中选择符合条件的元素组成新的列表

# 生成嵌套列表
# lis = [[j for j in range(5)] for i in range(5)]
# print(lis)

# 元组
# tuple1 = ('zhu')
# tuple2 = ('zhu',)
# # print(type(tuple1))        # <class 'str'>
# # print(type(tuple2))        # <class 'tuple'>
#
# tup = [x for x in range(0,20)]
# tup = tuple(tup)
# print(tup[2:9])


# 字典的创建
# 使用zip方法
# 中间传递两个列表数据作为参数
# name = ['Mary','Lucy','Lily','Cherry']
# sign = ['水瓶座','射手座','双鱼座','双子座']
# dic = dict(zip(name,sign))
# print(dic)
# 传递键值对创建字典
# dic = dict(Mary='水瓶座',Lucy='射手座',Lily='双鱼座',Cherry='双子座')
# print(dic)
#
# # 使用字面量来创建字典
# # get中使用key
# name = ('Mary','Lucy','Lily','Cherry')
# sign = ['水瓶座','射手座','双鱼座','双子座']
# dic = {name:sign}
# print(dic)
# # print(dic['Mary'])
# print(dic.get('Mary'))
# print(dic.get('Mry','zhuyongqi'))

# 使用键来索引字典
# 找不到的话就会报错
# dic = dict(Mary='水瓶座',Lucy='射手座',Lily='双鱼座',Cherry='双子座')
# print(dic['Mary'])
#
# # 使用get方法
# # 如果该字典没有该键，则返回none
# print(dic.get('Mary'))
# dic['name'] = 'zhuyongqi'
# print(dic)

#
# dic = dict(Mary='水瓶座',Lucy='射手座',Lily='双鱼座',Cherry='双子座')
# print(dic.keys())
# # keys()方法返回字典中所有的键，可以通过for循环遍历
# for i in dic.keys():
#     print(i)
# # values()方法返回字典中所有的值，可以通过for循环遍历
# for i in dic.values():
#     print(i)
# # items()方法返回字典中所有的键值对，返回值是数组的形式，可以通过for循环遍历
# for i in dic.items():
#     print(i)
# # 还可以通过两个变量将键值对拆开
# for keys,values in dic.items():
#     print(keys,values)





# import random
# rand = {i:random.randint(10,100) for i in range(1,5)}
# print(rand)
#
#
# name = ('Mary','Lucy','Lily','Cherry')
# sign = ['水瓶','射手','双鱼','双子']
# dic = {i:j+'座' for i,j in zip(name,sign)}
# print(dic)

# name = ['Mary','Lucy','Lily','Cherry']
# sign = ['水瓶座','射手座','双鱼座','双子座']
# dic = dict(zip(name,sign))
# print(dic)
# print(zip(name,sign))


# zip()函数中间可以传递多个可迭代的数据，
# 将多个可迭代的数据中的每一个元素一一对应，
# 后面可以使用类型转换转换为相应的数据
name1 = 'zhuyongqi'
name2 = 'zhuzhuzhu'
name3 = 'yongqi'
name4 = list(zip(name1,name2,name3))
print(name4)





















