import numpy as np
import numdifftools as nd

def newtonMultiDim(Fx,x0,max_it,tol):
    print ("==== Método de Newton para Matrizes Multi Dimensionais ====")
    Jx = []
    for f in Fx:
        # A jacobiana eh dada pela derivada parcial da funcao para cada dimensao,
        # resultando em um vetor de funcoes derivadas parciais
        jac = nd.Jacobian(f)
        Jx.append(jac)

    last_x = x0
    for it in range(max_it):
        # Preenchimento de Fk
        Fk = []
        for f in Fx:
            Fk.append([f(last_x)])
        Fk = np.matrix(Fk)

        # Preenchimento de Jk
        Jk = Jx[0](last_x)
        for j in Jx[1:]:
            Jk = np.vstack([Jk, j(last_x)]) # append
        Jk_1 = np.linalg.inv(Jk)

        # Cálculo de Xk
        deltaX = -1 * Jk_1 * Fk
        Xk = np.matrix(last_x) + deltaX.transpose()

        # Verificação da tolerância
        tolk = np.linalg.norm(deltaX)/np.linalg.norm(Xk)
        if tolk < tol:
            print ("Solução após %d iterações:\n Xk ="%(it+1),Xk)
            return Xk
        last_x = Xk.tolist()[0]
    print ("Não convergiu para %d iterações.\nXk = "%(it+1),Xk)

# def f1(X):
#     return X[0] + 2*X[1] - 2
#
# def f2(X):
#     return X[0]**2 + 4*X[1]**2 - 4
#
# f = [f1,f2]
# x0 = [2,3]
# max_it = 10000
# tol = 10**(-4)
# newtonMultiDim(f,x0,max_it,tol)
