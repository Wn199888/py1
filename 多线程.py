from threading import  Thread
import  time

bread = 100
basket = 0
class cook(Thread):
   username = ''
   def run(self) -> None:
        global bread
        global basket
        count = 0
        while True:
            if bread>=1:
                bread = bread - 1
                basket = basket + 1
                count = count + 1
                print(self.username,'做了个面包','还需做',bread,'个面包')
            elif basket == 100:
                print(self.username,'共做了',count ,'个面包')
                break







class custom(Thread):
    username = ''


    def run(self) -> None:
        basket = 100
        num = 0
        money = 100

        while True:
            if basket >= 1:
                money -= 2
                basket -= 1
                num += 1
                print(self.username,'买了个面包')
            else:
                   if money == 0:
                     print(self.username,'共买了',num,'个面包')
                     break





c1 = cook()
c1.username = 'a'
c2 =cook()
c2.username = 'b'
c3 = cook()
c3.username = 'c'
c1.start()
c2.start()
c3.start()

c11 = custom()
c11.username='11'
c22 = custom()
c22.username='22'
c33 = custom()
c33.username='33'
c44 = custom()
c44.username='44'
c55 = custom()
c55.username='55'
c66 = custom()
c66.username='66'
c11.start()
c22.start()
c33.start()
c44.start()
c55.start()
c66.start()
