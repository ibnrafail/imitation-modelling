import decimal
import math
from fractions import Fraction


def round_(num):
    temp = (num - int(num)) * 100
    if temp >= 50:
        num = math.ceil(num)
    else:
        num = math.floor(num)
    return num

x1 = 99
x2 = 0
x3 = 1

def check_conflict(a, b, c):
    if a + b + c > 100:
        a -= 1
    if a + b + c < 100:
        b += 1
    return a, b, c

output = []

for i in range(0, 100):
    temp1 = 0.9 * x1
    temp2 = 0.1 * x1 + 0.8 * x2
    temp3 = x3 + 0.2 * x2
    temps1 = round_(temp1)
    temps2 = round_(temp2)
    temps3 = round_(temp3)
    if 0 < temp1 < 1 and 0 < temp2 < 1 and 98.0 < temp3 < 99.0:
        output.append([0, 1, 99])
        output.append([0, 0, 100])
        break
    temps1, temps2, temps3 = check_conflict(temps1, temps2, temps3)
    if [temps1, temps2, temps3] not in output:
        output.append([temps1, temps2, temps3])
    x1 = temp1
    x2 = temp2
    x3 = temp3

for i in output:
    print(i)
