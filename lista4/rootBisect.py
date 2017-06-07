from math import *

def rootBisect(f,a,b,tol):
    print ("==== Método da Bisseção ====")
    it = 0
    while abs(b - a) >= tol:
        it += 1
        xi = (a + b) / 2.0
        fi = f(xi)
        if fi > 0.0:
            b = xi
        else:
            a = xi

    print ("Convergiu para %d iterações.\nXi = "%it, xi)
    return xi
# 
# def f1(x):
#     return x**2-4*cos(x)
# f=f1
# a = 0
# b = 10
# tol = 10**(-4)
#
# rootBisect(f1,a,b,tol)
