from math import *

def taylor(Ft,x0,x1,a,b,delta):
    t = a
    while t+delta <= b:
        x2 = Ft(t,x0,x1)
        x0 += x1*delta + x2/2.0*delta**2
        x1 += x2*delta
        t += delta
    print ("Valor encontrado: \n",x0)
    return x0


def f1(t,x0,x1):
    F = 2*sin(0.5*t) + sin(2*0.5*t) + cos(3*0.5*t)
    return F - x0 - 0.2*x1

x0 = 0
x1 = 0
a = 0
b = 100
delta = 0.1

taylor(f1,x0,x1,a,b,delta)
