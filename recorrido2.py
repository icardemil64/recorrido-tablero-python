import numpy as np
matriz1 = np.array([[1,0,0,1,0],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,1,0],[0,1,0,0,0]])
matriz2 = np.array([[1,0,0],[0,1,0],[0,0,0]])
matriz3 = np.array([[0,1,0,1,0],[0,0,0,0,0],[0,0,0,1,0],[0,1,0,0,1],[1,0,0,0,0]])
matriz4 = np.array([[0,1,0,1,0],[0,0,0,0,0],[0,0,1,1,0],[0,1,0,0,1],[1,0,0,0,0]])

def moverCasilla(k,mPrin,mAux):
    res = np.where(mAux == k)
    print(mAux)
    listaCasillas = list(zip(res[0],res[1]))
    for casilla in listaCasillas:
        print(casilla)
        i,j = casilla
        if i>0 and mAux[i-1][j] == 0 and mPrin[i-1][j] == 0:
            mAux[i-1][j] = k + 1
        if j>0 and mAux[i][j-1] == 0 and mPrin[i][j-1] == 0:
            mAux[i][j-1] = k + 1
        if i<(len(mAux)-1) and mAux[i+1][j] == 0 and mPrin[i+1][j] == 0:
            mAux[i+1][j] = k + 1
        if j<len(mAux[i])-1 and mAux[i][j+1] == 0 and mPrin[i][j+1] == 0:
            mAux[i][j+1] = k+1
    return mAux

def verificarMatriz(matriz):
    res = np.where(matriz == 0)
    listaCasillas = list(zip(res[0],res[1]))
    inicio = listaCasillas.pop(0)
    ultima = listaCasillas[len(listaCasillas)-1]
    matrizAux = np.zeros((len(matriz),len(matriz)))
    tam = len(matrizAux) * len(matrizAux)
    i,j = inicio
    matrizAux[i][j] = 1
    paso = 0
    while matrizAux[ultima[0]][ultima[1]] == 0 and paso <= tam:
        paso += 1
        moverCasilla(paso,matriz,matrizAux)
    return(matrizAux)
print(verificarMatriz(matriz2))