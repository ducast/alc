from math import *
import numpy as np

def inverseInterpolation(f,X,max_it,tol):
    print ("==== Método da Interpolação Inversa ====")
    x0 = 10**36
    Y=[]
    for x in X:
        Y.append(f(x))

    for it in range(max_it):
        xk = 0
        for current_y in range(len(Y)):
            result = 1
            for y in range(len(Y)):
                if current_y != y:
                    result *= Y[y] / (Y[current_y] - Y[y])
            xk += result * X[current_y]

        tolk = abs(xk - x0)
        print (xk, tolk)

        if tolk < tol:
            print ("Convergiu para %d iterações. \nXk = "%(it+1), xk)
            return xk
        else:
            x0 = xk
            max_value, max_index = 0, -1
            for i in range(len(Y)):
                if abs(Y[i]) > max_value:
                    max_value = abs(Y[i])
                    max_index = i

            X[max_index] = xk
            Y[max_index] = f(xk)

            X.sort()
            Y.sort()

    print ("Não convergiu para %d iterações.\nXk = "%it,xk)

def f1(x):
    return x**2-4*cos(x)
    # return log(cosh(x * sqrt(9.806 * 0.00341))) - 50

# f=f1
# x0 = [3,5,10]
# max_it = 10000
# tol = 5*10**(-4)
#
# inverseInterpolation(f1,x0,max_it,tol)
