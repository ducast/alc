def euler(f,x0,a,b,delta):
    print ("==== Integração Numérica de Euler ====")
    # Condicoes inciais em t0
    tk = a
    xk = x0
    # Iteracoes para t>0
    while tk+delta <= b:
        K1 = f(tk,xk)
        xk += delta*K1
        tk += delta
    print ("Valor encontrado: \n",xk)
    return xk

# def f1(t,fx):
#     return -2 * t * fx**2
#
# x0 = 1
# a = 0
# b = 2
# delta = 0.1
#
# euler(f1,x0,a,b,delta)
