import numpy as np
import numdifftools as nd

def broyden(Fx,x0,max_it,tol):
    print ("==== Método de Broyden para Matrizes Multi Dimensionais ====")
    Jx = []
    for f in Fx:
        # A jacobiana eh dada pela derivada parcial da funcao para cada dimensao,
        # resultando em um vetor de funcoes derivadas parciais
        jac = nd.Jacobian(f)
        Jx.append(jac)

    last_x = x0

    # Inicialização de B
    B0 = Jx[0](last_x)
    for j in Jx[1:]:
        B0 = np.vstack([B0, j(last_x)]) # append
    Bk = B0

    # Inicialização de F
    F0 = []
    for f in Fx:
        F0.append([f(last_x)])
    F0 = np.matrix(F0)
    Fk = F0

    for it in range(max_it):

        Jk = Bk
        Jk_1 = np.linalg.inv(Jk)

        # Cálculo do deltaX
        deltaX = -1 * Jk_1 * Fk
        deltaXT = deltaX.transpose()

        # Atualização do Xk
        Xk = np.matrix(last_x) + deltaXT

        # Atualização do Fk
        last_F = Fk
        Fk = []
        for f in Fx:
            Fk.append([f(Xk.tolist()[0])])
        Fk = np.matrix(Fk)

        # Atualização de Y
        Yk = Fk - last_F

        # Verificação da tolerância
        tolk = np.linalg.norm(deltaX)/np.linalg.norm(Xk)
        if tolk < tol:
            print ("Solução após %d iterações:\n Xk ="%(it+1),Xk)
            return Xk

        last_x = Xk.tolist()[0]
        Bk += (Yk-Bk*deltaX)*deltaXT/(deltaXT*deltaX)
        lastF = Fk
    print ("Não convergiu para %d iterações.\nXk = "%(it+1),Xk)

# def f1(X):
#     return X[0] + 2*X[1] - 2
#
# def f2(X):
#     return X[0]**2 + 4*X[1]**2 - 4
#
# broyden([f1,f2],[2,3],10000,10**(-4))
