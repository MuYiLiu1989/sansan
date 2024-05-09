# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:44:33 2024

@author: USER
"""

#1. 利用 for 計算 1~100 要印出奇數和

#1-1 加總可被7整除的數

#1-2 列出同時可被5和15整除的數

odd = 0
seven = 0
for i in range(1,101,1):
    if i%2==1:
        odd += i
    if i%7==0:
        seven +=i
    if i%5==0 and i%15==0:
        print('1-2',i)
print('1.奇數和:',odd)
print('1-1被7整除之和:',seven)
