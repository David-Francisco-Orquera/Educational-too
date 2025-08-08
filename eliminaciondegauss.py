import copy
#CREACION DE MATRIZ QUE SE VA A ANALIZAR PARA LA ELIMINACION DE GAUSS 
matriz = []
matrizordenada = []
#INGRESO DE LAS FILAS QUE SE DESEA QUE SE HAGA LA MATRIZ
fila = int(input("Ingresa la numero de filas que tiene tu matriz: "))
columna = int(input("Ingresa la numero de columnas que tiene tu matriz: "))
#RECORRE LAS FILAS
for i in range(fila):
#CREACION DEL VECTOR FILA    
    filas = []
#RECORRER EN EL VECTO FILAS LAS COLUMNAS
    for j in range(columna):
#INGRESO DE LOS ELEMENTOS DEL VECTOR FILA
        filas.append(float(input("Ingrese la constante en la posicion ["+str(i+1)+"]["+str(j+1)+"]: ")))
#ALMACENAMIENTO DEL VECTOR FILA EN LA PRIMERA FILA DE LA MATRIZ matriz
    matriz.append(filas)
#IMPRESION DE LA MATRIZ
for k in matriz:
    print(k)  
print(f"---------------------------------------------------------------------------")
#-----------------------------------------------------------------ORDENAR LA MATRIZ--------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# VERIFICACION QUE EL PRIMER ELEMENTO SEA 0
if matriz[0][0] == 0:
#BUSQUEDA EN LA MATRIZ DEL PRIMER ELEMENTO QUE SEA DIFERENTE DE 0 (NO TIENE CASO BUSCAR LOS QUE SON IGUAL A 0)
#RECORRIDO DE LA MATRIZ DESDE LA POSICISION 1 POR QUE LA 0 ES LA QUE NOS INTERESA CAMBIAR
    for i in range(1, len(matriz)):
#SI ENCUENTRA UNA FILA DONDE EL PRIMER ELEMENTO SEA DIFERENTE DE 0 ENTONCES LA USA SI NO NO ENTRA EN LA CONDICION
        if matriz[i][0] != 0:
#INTERCAMBIO DE LA PRIMERA FILA (QUE NOS INTERESA QUE NO SEA 0) CON LA FILA EN DONDE ENCONTRO UN NUMERO DIFERENTE DE 0
            matriz[0], matriz[i] = matriz[i], matriz[0]
            break
#AHORA VAMOS A MOVER TODOS LOS 0 EN LAS PRIMERAS POSICIONES PARA DEJAR LA MATRIZ LISTA PARA EMPEZAR LA ELIMINACION DE GAUSS  
#IGNORAMOS EL PRIMER ELEMENTO YA QUE ESTAMOS SEGUROS QUE ESE YA NO ES IGUAL 0 POR ESO EMPEZAMOS DESDE LA POSICION 1      
for i in range(1, len(matriz)):
#BUSQUEDA DEL PRIMER ELEMENTO QUE SEA DIFERENTE DE 0 DESPUES DEL PRIMER ELEMENTO
    if matriz[i][0] != 0:
#BUSQUEDA DE LA SIQUIENTE FILA EN DONDE EL PRIMER ELEMENTO SI SEA 0 E INTERCAMBIO DE LAS FILAS
        for j in range(i + 1, len(matriz)):
# SI EL ELEMENTO ES IGUAL A 0 ENTONCES SE ESCOJE ESA FILA
            if matriz[j][0] == 0:
# INTERCAMBIO DE FILAS EN DONDE TODAS LAS FILAS QUE SEAN 0 QUEDAN ORDENADAS ARRIBA DE LOS ELEMENTOS QUE SON DIFERENTES DE 0
                matriz[i], matriz[j] = matriz[j], matriz[i]
                break
#------------------------------------------------------------------PROCESO DE CALCULO------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#PRIMER FOR PARA LIMITAR EL CALCULO HASTA LAS COLUMNAS CORRESPONDIENTES (EJ. MATRIZ DE 3X3 HASTA LA COLUMNA 2)
for h in range(len(matriz)-1):
#FOR PARA QUE CUENTE DESDE EL ELEMENTO DESPUES AL QUE SE ENCUENTRA EL PIVOTE     
    for i in range(h+1, len(matriz)):
#MULTIPLICADOR PARA PODER HACER 0 A LOS ELEMENTOS DESPUES DEL PIVOTE        
        multiplicador=(matriz[i][h]/matriz[h][h])
#CONDICION PARA QUE SOLO ENTRE A LAS FILAS DONDE EL PRIMER ELEMENTO ES DIFERENTE DE 0
        if matriz[i][h] != 0:
#FOR PARA QUE SE MULTIPLIQUE EL MULTIPLICADORA TODOS LOS ELEMENTOS DE LA FILA (APLICANDO EL PROCESO VISTO EN CLASES)
            for j in range(len(matriz)+1):
                multiplicacion = matriz[h][j] * float(multiplicador) * -1
                suma = multiplicacion + matriz [i][j]
                matriz[i][j] = suma
    


    
for k in matriz:
    print(k) 
#-------------------------------------------------------------DESPEJE DE VARIABLES---------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
           









