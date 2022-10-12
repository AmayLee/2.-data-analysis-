# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:50:54 2022

@author: HUOQINGHAI
"""
'''
一、类与对象
创建一个类，然后创建实际的“对象”

对象=属性（静态的特征）+方法（可以做的事情）

所谓“属性”就是写在类里面的“变量”，所谓“方法”就是写在类里面的“函数”

“实例化”就是将类赋值到一个变量中。t1就是Turtle类的对象，也叫“实例对象”，它就拥有了这个类的“属性”和“方法”


（一）面向对象的基本特征之一——封装

self是什么？





'''

class Turtle:
    head = 1
    eyes = 2
    legs = 4
    shell = True
    
    def crawl(self):
        print("人们总是抱怨我动作慢吞吞的，殊不知不积硅步，无以至千里的道理")
        
    def run(self):
        print("虽然我行动很慢，但如果遇到危险，还是会多名奔跑的")
        
    def bite(self):
        print("人善被人欺，龟善被人骑，我可是会咬人的")
        
    def eat(self):
        print("谁知盘中餐粒粒皆辛苦，吃得好，不如吃得饱")
        
    def sleep(self):
        print("Zzzzz...")
    
t=Turtle()
data=t.head
t.crawl()
t.bite()
t.eat()
t.run()


        
    