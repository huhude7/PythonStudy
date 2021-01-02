# f = open("test.txt","w")
# f.write("python")
# f = open("test.txt","r")
# content = f.read()
# print(content)
# f.close()
# print(f.closed)

# pic
from PIL import Image
image1 = Image.open(r"E:\呼呼的\桌面\1.png")
image1.show()
print(image1.format)
print(image1.mode)
image1.save(r"E:\呼呼的\桌面\1.jpg")


# with
# with open('test.txt',"w") as file:
#     print("\n","="*10,"zhuzhuzhu","="*10)
#     print(file.closed)
# print(file.closed)

# f = open('test.txt')
# print(f.tell())
# f.read(5)
# print(f.tell())
# f.close()

# b = u'北京欢迎你'
# c = b.encode('utf-8')
# d = c.decode('utf-8')
# print(type(b))
# print(b)
# print(type(c))
# print(c)
# print(type(d))
# print(d)




# import os
# # f = open("test.txt","r+")
# # print(f.read())
# f = open("test.txt","w+")
# f.writelines("zhyongqi")
# f.write("python")
# f.seek(3,0)
# print(f.tell())
# f.close()
# os.remove("test.txt")

