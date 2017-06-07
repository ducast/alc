def rkn(Ft,x0,x1,a,b,delta):
    t = a
    while t+delta <= b:
        x2 = Ft(t,x0,x1)

        K1 = 0.5*delta*x2
        Q = 0.5*delta*(x1+0.5*K1)
        K2 = 0.5*delta * Ft(t+0.5*delta, Q+x0, K1+x1)
        K3 = 0.5*delta * Ft(t+0.5*delta, Q+x0, K2+x1)
        L = delta*(K3+x1)
        K4 = 0.5*delta * Ft(t+delta, L+x0, 2*K3+x1)

        x0 += delta*( x1 + (K1+K2+K3)/3.0 )
        x1 += (K1 + 2*K2 + 2*K3 + K4)/3.0
        t += delta

    print ("Valor encontrado: \n",x0)
    return x0

def f1(t,x0,x1):
    return -9.84-x1*abs(x1)

x0 = 0
x1 = 0
a = 0
b = 1
delta = 0.1

rkn(f1,x0,x1,a,b,delta)
