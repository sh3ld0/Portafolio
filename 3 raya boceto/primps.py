import random
def mostrar(M,f):
    j=0
    k=1
    l=2
    print("+-------+-------+-------+")
    for i in range(f):
        print(f"|       |       |       |\n|   {M[i][j]}   |   {M[i][k]}   |   {M[i][l]}   |\n|       |       |       |")
        print("+-------+-------+-------+")
def ganador(M,f,c):
    columnas=0
    filas=0
    diagonalPrincipal=0
    diagonalSecundaria=0
    for i in range (f):
        for j in range(c):
            if "x"==M[i][j]:
                filas+=1
            if "x"==M[j][i]:
                columnas+=1
            if "x"==M[j][j]:
                diagonalPrincipal+=1
            if "x"==M[j][c-1-j]:
                diagonalSecundaria+=1
        if filas==3 or columnas==3 or diagonalPrincipal==3 or diagonalSecundaria==3:
            maquina=1
            return maquina
        else:
            diagonalPrincipal=0
            filas=0
            columnas=0
            diagonalSecundaria=0
    filasu=0
    columnasu=0
    diagonalPrincipalu=0
    diagonalSecundariau=0
    for i in range (f):
        for j in range(c):
            if "0"==M[i][j]:
                filasu+=1
            if "0"==M[j][i]:
                columnasu+=1
            if "0"==M[j][j]:
                diagonalPrincipalu+=1
            if "0"==M[i][c-1-j]:
                diagonalSecundariau+=1
        if filasu==3 or columnasu==3 or diagonalPrincipalu==3 or diagonalSecundariau==3:
            usuario=2
            return usuario
        else:
            diagonalPrincipalu=0
            filasu=0
            diagonalSecundariau=0
            columnasu=0
    return 0

def comprobarPosicion(posicion,OCUPADOS):
    posic=0
    for i in range(len(OCUPADOS)):
        if posicion==OCUPADOS[i] and posicion>0 and posicion<10:
            posic+=1
    if posic==0:
        return 1
    else:
        return 0
def ingresarPosicionUsuario(posicion,M,f,c,OCUPADOS):
    cont=0
    comprobado=comprobarPosicion(posicion,OCUPADOS)
    if comprobado== 1:
        OCUPADOS.append(posicion)
        cont=0
        for i in range(f):
            for j in range(c):
                cont+=1
                if cont==posicion:
                    M[i][j]="0"
    else:
        print("ya esta marcada esa posicion, vuelve a marcar")
        posicion=int(input("ingresar posicion a marcar"))
        ingresarPosicionUsuario(posicion,M,f,c,OCUPADOS)
def ingresarPosicionMaquina(posicion,M,f,c,OCUPADOS):
    cont=0
    comprobado=comprobarPosicion(posicion,OCUPADOS)
    if comprobado == 1:
        OCUPADOS.append(posicion)
        cont=0
        for i in range(f):
            for j in range(c):
                cont+=1
                if cont==posicion:
                    M[i][j]="x"
                    print("la maquina ya marco te toca marcar")
                    mostrar(M,f)
    else:
        posiMaquina=random.randint(1,9)
        ingresarPosicionMaquina(posiMaquina,M,f,c,OCUPADOS)
def quienIngresa(M,f,c,OCUPADOS):
    while ganador(M,f,c)==0:
        posiUsua=int(input("ingresar la posicion a marcar: "))
        posiMaquina=random.randint(1,9)
        ingresarPosicionUsuario(posiUsua,M,f,c,OCUPADOS)
        if ganador(M,f,c)==2:
            print("ganador usuario")
            mostrar(M,f)
            return 2
        ingresarPosicionMaquina(posiMaquina,M,f,c,OCUPADOS)
        if ganador(M,f,c)==1:
            print("ganador Maquina")
            mostrar(M,f)
            return 1
        if len(OCUPADOS)==9:
            print("empate")
            mostrar(M,f)
            return 0
def decirQuienGano(M,f,c,OCUPADOS):
    gano=quienIngresa(M,f,c,OCUPADOS)
    print(gano)
    if gano==1:
        print("ganador maquina ")
        mostrar(M,f)
    elif gano==2:
        print("ganador usuario")
        mostrar(M,f)
    elif gano==0:
        print("empate")
        mostrar(M,f)
M=[[1,2,3],[4,"x",6],[7,8,9]]
f=len(M)
c=len(M[0])
OCUPADOS=[5]
mostrar(M,f)
quienIngresa(M,f,c,OCUPADOS)