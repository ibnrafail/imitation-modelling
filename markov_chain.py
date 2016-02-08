# Hello World program in Python
import decimal
import math

def fun(num):
    temp = (num - int(num)) * 100
    if temp >= 50:
        num = math.ceil(num)
    else:
        num = math.floor(num)

x1 = 99.0
x2 = 0.0
x3 = 1.0
for i in range(0,100):
    temp1 = 0.9 * x1
    temp2 = 0.1 * x1 + 0.8 * x2
    temp3 = x3 + 0.2 * x2
    fun(temp1)
    fun(temp2)
    fun(temp3)
    print(temp1, temp2, temp3)
    x1 = temp1
    x2 = temp2
    x3 = temp3