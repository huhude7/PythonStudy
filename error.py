# try :
#     a = int(input())
#     b = int(input())
#     print(a/b)
# except Exception as res:
#     print(f"error: {res}");


# while True:
#     try:
#         x = int(input())
#         y = int(input())
#         assert x >1 and y>1,'a 和 b的值必须大于1'
#         a = x
#         b = y
#         if a < b:
#             a,b=b,a
#         while b!=0:
#             temp = a % b
#             a = b
#             b = temp
#         else:
#             print('%s 和 %s 的最大公约数是：%s'%(x,y,a))
#             break
#     except Exception as result:
#         print('异常：',result)

# 1.假设成年人的体重（整数）和身高（整数）存在此种关系：
#     身高（厘米）-100 = 标准体重（千克）
# 如果一个人的体重与其标准体重的差值在正负5%之间，显示“体重正常”，其他则显示“体重超标”或者“体重不达标”。
# 编写程序根据用户输入的体重、身高判断体重正常、超标或不达标。能处理用户输入的异常，
# 并且使用自定义异常类来处理身高小于130cm、大于250cm的异常情况。
'''
class error_range(Exception):
    def __init__(self,height):
        self.height = height;


while True:
    try :
        h = int(input())
        w = int(input())
        if h > 250 or h < 130 :
            raise error_range(h)
        stdw = h- 100
        check = w - stdw
        if check < 0.05 and check > -0.05:
            print("体重正常")
            break
        elif check > 0.05 :
            print("体重超标")
            break
        else:
            print("体重不达标")
            break
    except error_range as res:
        print(f"输入的身高为{h},不在测试的范围内。")
    except Exception as res:
        print(res)
'''


# 2.录入一个学生的成绩，如学生的成绩属于[90,100]的区间则转换为A；
# 如学生的成绩属于[80,90)的区间则转换为B；如学生的成绩属于[60,70)的区间则转换为C；
# 如学生的成绩属于[0,60)的区间则转换为D。要求使用assert断言处理分数负数或超过100的不合理的情况。

# score = int(input())
# assert 0< score < 100, "score的值必须在合理范围内。"
# layer = int(score /10)
# if layer >= 9:
#     print("A")
# elif  layer >= 8 and layer < 9:
#     print("B")
# elif  layer >= 6 and layer < 7:
#     print("C")
# elif layer >= 0 and layer < 6:
#     print("D")

try :
    a = 1
    assert a >10
    # assert a >10,"error"
    print(a)
except:
    print("ERROR")



