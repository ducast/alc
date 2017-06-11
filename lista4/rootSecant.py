from math import *

def rootSecant(f,x0,max_it,tol):
    print ("==== Método de Newton para Raízes ====")

    deltaX = 0.001
    x1 = x0 + deltaX
    fa = f(x0)
    for it in range(max_it):
        fi = f(x1)
        x2 = x1 - (fi * (x1 - x0)) / (fi - fa)
        tolk = abs(x2 - x1)

        print (int(it),round(x1,2))

        if tolk < tol:
            print ("Convergiu para %d iterações.\nXi = "%(it+1),x1)
            return x1
        fa = fi
        x0, x1 = x1, x2
    print ("Não convergiu para %d iterações.\nXk = "%(it+1),x1)

# def f1(x):
#     return x**2-4*cos(x)
#
# f=f1
# x0 = 10
# max_it = 10000
# tol = 10**(-4)
#
# rootSecant(f1,x0,max_it,tol)
