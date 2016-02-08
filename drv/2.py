from fractions import Fraction
from prettytable import PrettyTable

x = [[1, Fraction(2, 6)], [2, Fraction(1, 6)], [3, Fraction(3, 6)]]
y = [[1, Fraction(1, 7)],[2, Fraction(2, 7)],[3, Fraction(4, 7)]]

def f(x, y):
    a = []
    b = []
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            if x[i][0] + y[j][0] not in a:
                a.append(x[i][0] + y[j][0])
                b.append(x[i][1] * y[j][1])
            else:
                index_in = a.index(x[i][0] + y[j][0])
                b[index_in] += x[i][1] * y[j][1]
    a.insert(0, "Z")
    b.insert(0, "P")
    table = PrettyTable(a)
    table.add_row(b)
    print(table)

f(x,y)



