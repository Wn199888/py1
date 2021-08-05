#姐就是女王游戏
import random
list = ['普通','稀有','传奇']
# print(list[random.randint(0,len(list)-1)])
name = list[random.randint(0,len(list)-1)]
list = [1,2]
num ,num2 = 10,30
while True:
    if name == '普通' :
        print('您获得普通英雄 ')
        i =0
        ranumber = []
        while i<3:
            i+=1
            a = random.randint(5,20)
            ranumber.append(a)
        print('请选择一个数:',ranumber[0],ranumber[1],ranumber[2])
        num1 = ranumber[random.randint(0, len(ranumber) - 1)]
        print(num1)
        ran1 = list[random.randint(0,len(list)-1)]
        if ran1 == 1:
            num = num+num1
            print(num)
        else:
            num =num - num1
        if num>100:
            print('任务成功！你的分数为：',num)
            break
        elif num <= 0:
            print('任务失败！你的分数为：',num)
            break
    elif name == '稀有' :
        print('您获得稀有英雄 ')
        i = 0
        ranumber1 = []
        while i < 3:
            i += 1
            b = random.randint(5, 20)
            ranumber1.append(b)
        print('请选择一个数:', ranumber1[0], ranumber1[1], ranumber1[2])
        num3 = ranumber1[random.randint(0, len(ranumber1) - 1)]
        print(num3)
        ran1 = list[random.randint(0, len(list) - 1)]
        if ran1 == 1:
            num2 = num2 + num3
            print(num2)
        else:
            num2 = num2 - num3
        if num2 > 100:
            print('任务成功！你的分数为：', num2)
            break
        elif num2 <= 0:
            print('任务失败！你的分数为：', num2)
            break
    else:
        print('您获得传奇英雄 ')
        i = 0
        ranumber2 = []
        while i < 3:
            i += 1
            b = random.randint(5, 20)
            ranumber2.append(b)
        print('请选择一个数:', ranumber2[0], ranumber2[1], ranumber2[2])
        num4 = ranumber2[random.randint(0, len(ranumber2) - 1)]
        print(num4)
        num2 =num2+num4
        if num2 > 100:
            print('任务成功！，你的分数为：',num2)
            break


#
# import random
# print('-------姐就是女王-------')
# character = ['1.普通英雄','2.稀有英雄','3.传奇英雄']
# init = [10,30]
# ran = [random.randint(5,20),random.randint(5,20),random.randint(5,20)]
# cha = random.choice(character)
# list = [1,2]
# score = init[0]
# while 1:
#     if cha == character[0]:
#         print("您获得的英雄是：", cha)
#         print('请选择一个数：',ran[0],ran[1],ran[2])
#         sele = int(input())
#         if sele == ran[0]:
#             a = list[random.randint(0,len(list)-1)]
#             if a == 1:
#                 score += sele
#             else :
#                 score += sele
#             if score>100:
#                 print('任务成功，你的分数为：',score)
#                 break
#             elif score<=0:
#                 print('任务失败，你的分数为：',score)
#                 break
#         if sele == ran[1]:
#             a = list[random.randint(0,len(list)-1)]
#             if a == 1:
#                 score += sele
#             else :
#                 score += sele
#             if score>100:
#                 print('任务成功，你的分数为：',score)
#                 break
#             elif score<=0:
#                 print('任务失败，你的分数为：',score)
#                 break
#         if sele == ran[2]:
#             a = list[random.randint(0,len(list)-1)]
#             if a == 1:
#                 score += sele
#             else :
#                 score += sele
#             if score>100:
#                 print('任务成功，你的分数为：',score)
#                 break
#             elif score<=0:
#                 print('任务失败，你的分数为：',score)
#                 break


# '''
# 1.随机点名
# 2.随机生成棒棒糖
#
# 容器类型：
#         int, str,double,boolean
#         元组（tuple）：（）--不可修改
#         列表(list)：[]
#             append()添加数据，元素；pop():删除从后往前删除 角标最后一个为-1
#         字典：{‘’：‘’} 键值对
#               键   值   通过键获取值
# '''
# name = (1,2,3,4,5)
# print(type(name))

# name1 = [11,2,3,4,5]
#  print(type(name1))
#  name1.append(6)
# name1.pop
# print(name1.remove(3))
# print(name1)


# import random
# name = ['a', 'b', 'c', 'd']
# i=0
# while i<2:
#     i+=1
#     print("请输入您的业务（1、点名，2发棒棒糖）：")
#     choose = input()
#     if choose == '1':
#       a = len(name)
#       index=random.randint(0,a-1)
#       print("您被点到了：",name[index])
#     elif choose =="2":
#       index1 = random.randint(0,a-1)
#       num = random.randint(5,10)
#       print(name[index1],':','获得了',num,'个棒棒糖')
#     else:
#         print('非法输入！')
#         break
