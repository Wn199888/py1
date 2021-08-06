
#乘法口诀
for i in range(1,10):
  for j in range(1,i+1):
     print(j,'*',i,'=',j*i,end=' ')
  print()

n = int(input('请输入一个数字：'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,'*',i,'=',j*i,end=' ')
    print()


data = { '13号线':{
                      '流星花园':
                                ['001','002','003'],

                      '育荣教育园区':
                               ['0001','0002','0003'],

                   },
         '1号线':{
                       '兴隆花园':
                               ['001','002','003',]
                                ,
                       '康家园小区':
                                ['0001','0002','0003']

                   },
            '昌平线':{
                       '博雅德园':
                                ['001','002','003',]
                                ,
                       '融泽家园':
                                 ['0001','0002','0003']
                                   }
        }

def print_adress(choose):
    for i in choose:
        print(i)

for x in data.keys():
    print(x)
line = input('请选择地铁线路：')
if line in data:
    print_adress(data[line])
    adress= input('请选择小区：')
    if adress in data[line]:
          print_adress(data[line][adress])
          num = input('请输入门牌号:')
          if num in data[line][adress]:
              print(num)
