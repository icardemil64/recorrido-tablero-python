import numpy as np
matriz1 = np.array([[1,0,0,1,0],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,1,0],[0,1,0,0,0]])
matriz2 = np.array([[1,0,0],[0,1,0],[0,0,0]])
matriz3 = np.array([[0,1,0,1,0],[0,0,0,0,0],[0,0,0,1,0],[0,1,0,0,1],[1,0,0,0,0]])
matriz4 = np.array([[0,1,0,1,0],[0,0,0,0,0],[0,0,1,1,0],[0,1,0,0,1],[1,0,0,0,0]])

def moverCasilla(k,mPrin,mAux):
    for i in range(len(mAux)):
        for j in range(len(mAux[i])):
            if mAux[i][j] == k:
                if i>0 and mAux[i-1][j] == 0 and mPrin[i-1][j] == 0:
                    mAux[i-1][j] = k + 1
                if j>0 and mAux[i][j-1] == 0 and mPrin[i][j-1] == 0:
                    mAux[i][j-1] = k + 1
                if i<(len(mAux)-1) and mAux[i+1][j] == 0 and mPrin[i+1][j] == 0:
                    mAux[i+1][j] = k + 1
                if j<len(mAux[i])-1 and mAux[i][j+1] == 0 and mPrin[i][j+1] == 0:
                    mAux[i][j+1] = k+1
    print(mAux,"\n")
    return mAux
                

def verificarMatriz(matriz):
    #Obtiene el indice de la primera y ultima casilla no marcada
    res = np.where(matriz == 0)
    listCord = list(zip(res[0],res[1]))
    inicio = listCord[0]
    ultima = listCord[len(listCord)-1]

    #Inicializa matriz auxiliar
    matrizAux = np.zeros((len(matriz),len(matriz)))
    i,j = inicio
    matrizAux[i][j] = 1
    #Llama a la funcion para el primer paso por el tablero
    paso = 0
    while matrizAux[ultima[1]][0] == 0 and paso <= len(matrizAux):
        paso += 1
        moverCasilla(paso,matriz,matrizAux)
    
    return(True)

print("\nMatriz recorrida")
print(verificarMatriz(matriz2))