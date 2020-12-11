# coding = utf-8
# 条件判断

# 身高和体重，体重比的大小来判断胖瘦
# 体指数t = 体重 w / (身高 h *身高 h)
# 当t<18时，为thin；
# 当18≤t<25时，为standard；
# 当25≤t<27时，为little fat；
# 当t≥27时，为fat
height = float(input('请输入身高(cm)：'))
weight = float(input('请输入体重(kg)：'))
bili = weight / (height * height)
if bili < 18:
    print('thin')
elif bili >= 27:
    print('fat')
elif bili < 27 and bili >= 25:
    print('little fat')
else:
    print('standard')





# #根据输入的出生年月日判断是否成年
# import time
# localtime = time.localtime(time.time())
# year = int(input("出生年份: "))
# month = int(input("出生月份: "))
# day = int(input("出生日期: "))
# if localtime.tm_year - year > 18:
#     print("-----已经成年------")
# elif localtime.tm_year - year < 18:
#     print("-----未成年------")
# elif localtime.tm_mon - month < 0:
#     print("-----未成年-----")
# elif localtime.tm_mon - month > 0:
#     print("-----已经成年------")
# elif localtime.tm_mday - day < 0:
#     print("--_--未成年-----")
# elif localtime.tm_mday - day >= 0:
#     print("-----已经成年-----")
# print("-----if判断结束------")

# 猜拳游戏

# import random
# diannao = random.randint(0,2)
# yonghu = int(input('请输入0（剪刀），1（石头），2（布）:'))
# print(diannao)
# if yonghu - diannao == -1 or yonghu - diannao == 2:
#     print('电脑赢')
# elif diannao == yonghu :
#     print('平局')
# else:
#     print('用户赢')