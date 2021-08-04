
import random
character = ['1.普通','2.稀有英雄','3.传奇英雄']
print('-------姐就是女王-------')
i = 0
while i<3:
    i+=1
    choose = int(input('请选择角色：'))
    a = random.randint(1,200)
    b = random.randint(1,200)
    c = random.randint(1,200)
    rnum = [a,b,c]
    if choose == 1 :
        print('普通英雄')
        init = 10
        d = random.choice(rnum)
        e = random.randint(0,1)
        if e==0 :
            init +=d
            if init > 100:
                print('任务成功！')
            elif init <= 0:
                print("任务失败")
        elif e==1 :
            print('稀有英雄')
            init -=d
            if init > 100:
                print('任务成功！')
            elif init <= 0:
                print("任务失败")
    elif choose == 2:
        print('传奇英雄')
        init1 = 30
        f = random.choice(rnum)
        g = random.randint(0, 1)
        if g == 0:
            init1 += f
            if init1 > 100:
                print('任务成功！')
            elif init1 <= 0:
                 print("任务失败")
        elif g == 1:
            init1 -= f
            if init1 > 100:
                print('任务成功！')
            elif init1 <= 0:
                print("任务失败")
    elif choose == 3:
           init2 = 10
           h = random.choice(rnum)
           init2 += h
           if init2 > 100:
               print('任务成功！')
           else:
               print("任务失败")
print('-----------------------')

'''
1.随机点名
2.随机生成棒棒糖

容器类型：
        int, str,double,boolean
        元组（tuple）：（）--不可修改
        列表(list)：[]
            append()添加数据，元素；pop():删除从后往前删除 角标最后一个为-1
        字典：{‘’：‘’} 键值对
              键   值   通过键获取值
'''
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