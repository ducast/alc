def rungeKutta4(f,x0,a,b,delta):
    print ("==== Integração Numérica de Runge-Kutta (4ª Ordem) ====")
    # Condicoes inciais em t0
    tk = a
    xk = x0
    # Iteracoes para t>0
    while tk+delta <= b:
        K1 = f(tk, xk)
        K2 = f(tk+delta/2, xk+delta/2*K1)
        K3 = f(tk+delta/2, xk+delta/2*K2)
        K4 = f(tk+delta, xk+delta*K3)
        xk += delta/6.0*(K1 + 2*K2 + 2*K3 + K4)
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
# rungeKutta4(f1,x0,a,b,delta)
