import numpy as np
matriz1 = np.array([[1,0,0,1,0],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,1,0],[0,1,0,0,0]])
matriz2 = np.array([[1,0,0],[0,1,0],[0,0,0]])
matriz3 = np.array([[0,1,0,1,0],[0,0,0,0,0],[0,0,0,1,0],[0,1,0,0,1],[1,0,0,0,0]])
matriz4 = np.array([[0,1,0,1,0],[0,0,0,0,0],[0,0,1,1,0],[0,1,0,0,1],[1,0,0,0,0]])
matriz5 = np.array([[0,0,1,0,0],[1,0,0,0,1],[0,0,1,0,0],[0,1,0,0,1],[1,0,0,0,0]])
matriz6 = np.array([[0,0,1,0,0],[1,0,0,0,1],[0,0,1,0,0],[0,1,0,0,1],[1,0,1,0,0]])
matriz7 = np.array([[0,0,1,0,0],[1,0,0,0,1],[0,0,1,0,0],[0,1,0,0,1],[1,0,0,1,0]])
def moverCasilla(k,mPrin,mAux):
    res = np.where(mAux == k)
    listaCasillas = list(zip(res[0],res[1]))
    for casilla in listaCasillas:
        i,j = casilla
        if i>0 and mAux[i-1][j] == 0 and mPrin[i-1][j] == 0:
            mAux[i-1][j] = k + 1
        if j>0 and mAux[i][j-1] == 0 and mPrin[i][j-1] == 0:
            mAux[i][j-1] = k + 1
        if i<(len(mAux)-1) and mAux[i+1][j] == 0 and mPrin[i+1][j] == 0:
            mAux[i+1][j] = k + 1
        if j<len(mAux)-1 and mAux[i][j+1] == 0 and mPrin[i][j+1] == 0:
            mAux[i][j+1] = k+1
    return mAux

def verificarMatriz(matriz):
    res = np.where(matriz == 0)
    listaCasillas = list(zip(res[0],res[1]))
    inicio = listaCasillas.pop(0)

    matrizAux = np.zeros((len(matriz),len(matriz)))
    tamano = len(matrizAux) * len(matrizAux)
    cantMarcados = np.sum(matriz == 1)
    i,j = inicio

    for ultimo in listaCasillas:
        matrizAux[:] = 0
        matrizAux[i][j] = 1
        m,n = ultimo
        paso = 0
        while matrizAux[m][n] == 0 and paso <= tamano:
            paso+=1
            moverCasilla(paso,matriz,matrizAux)
        cantRecorrido = np.sum(matrizAux != 0)
        if((cantRecorrido + cantMarcados) == tamano):
            return(True)
    return(False)
#print(verificarMatriz(matriz7))
print(matriz1)
