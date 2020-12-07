import math
import sys
a = 0
b = 0
c = 0
while(True):
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        break
    except BaseException:
        print("Ошибка ввода параметров или параметры отсутствуют")
        try:
            print("A = ", end = '')
            a = float(input())
            print("B = ", end = '')
            b = float(input())
            print("C = ", end = '')
            c = float(input())   
            break 
        except ValueError:
            print("Ошибка ввода")

D = b*b-4*a*c
if D < 0:
    print("Нет действительных корней")
elif D == 0:
    try:
        print("x1 =", math.sqrt(-b/(2*a)))
        print("x2 =", -1 * math.sqrt(-b/(2*a)))
    except ValueError:
        print("Нет действительных корней")
else:
    t1 = (-b + math.sqrt(D))/(2*a)
    t2 = (-b - math.sqrt(D))/(2*a)

    if t1 > 0:
        print("x1 =", math.sqrt(t1))
        print("x2 =", -1*math.sqrt(t1) )
        if t2 > 0:
            print("x3 =",math.sqrt(t2))
            print("x4 =",-1*math.sqrt(t2))
        elif t2 == 0:
            print("x3 = 0")
    elif t1 == 0:
        print("x1 = 0")
        if t2 > 0:
            print("x2 =",math.sqrt(t2))
            print("x3 =",-1*math.sqrt(t2))
    elif t2 > 0:
        print("x1 =", math.sqrt(t2))
        print("x2 =", -1*math.sqrt(t2) )
    elif t2 == 0:
        print("x = 0")
    else:
        print("Нет действительных корней")

