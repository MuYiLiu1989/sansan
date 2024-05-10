# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:09:38 2024

@author: USER
"""
import random

#1.亂數產生5~100之間可以被5整除的數，產生5個且不可重覆
#  請用5個變數去儲存

F=[0,0,0,0,0]
for i in range(5):
    a = random.randrange(5,101,5)
    while a in F:
        a = random.randrange(5,101,5)
    F[i] = a
print(F)
    

#2.a,b,c三邊長
#  由使用者輸入邊長
#(1)是不是三角形
#(2)是不是直角三角形

a = eval(input("請輸入邊長:"))
b = eval(input("請輸入邊長:"))
c = eval(input("請輸入邊長:"))

if a+b>c and b+c>a and c+a>b:
    print("是三角形")
    if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("是直角三角形")
    else:
        print("不是直角三角形")
else:
    print("不是三角形")
