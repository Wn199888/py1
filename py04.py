# 求每个人的总成绩
luoen = [23,35,44]
hali = [60,77,68,88,90]
hemin = [97,99,89,91,95,90]
maerfu = [100,85,90]
grade1,grade2,grade3,grade4= 0,0,0,0
for x in range(len(luoen)):
    grade1 += luoen[x]
print('罗恩的成绩为：',grade1)
for x in range(len(hali)):
    grade2 +=hali[x]
print('哈利的总成绩为：',grade2)
for x in range(len(hemin)):
    grade3 +=hemin[x]
print('赫敏的总成绩为：',grade3)
for x in range(len(maerfu)):
    grade4 +=maerfu[x]
print('哈利的总成绩为：',grade4)
print('--------------------')
#阅读程序并回答问题
num = int(input('请输入一个数：'))
while num != 0:
    print(num % 10)
    num = num // 10
#输入25 ---- 5 , 2
print('--------------------')
#一个列表求其中是5的倍数的数的和
a = [1,5,21,30,15,9,90,24]
sum = 0
for a1 in a:
    if a1 % 5 == 0:
        sum += a1
print("列表中是5的倍数的和为：",sum)
print('--------------------')
#实现列表中的数据翻转
list = [1,2,3,4,5,6,7,8,9]
list1 = []
for i in range(9):
    a = list.pop()
    list1.append(a)
list = list1
print(list)
print('--------------------')
#统计列表中每个数字出现的次数 两种方法
list = [1,4,7,5,8,2,1,3,4,5,7,9,7,6,1,0]
dict = {}
for x in list:
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] +=1
print(dict)

# list = [1,4,7,5,8,2,1,3,4,5,7,9,7,6,1,0]
# dict = {}
# for x in list :
#     dict[x] = list.count(x)
# print(dict)
