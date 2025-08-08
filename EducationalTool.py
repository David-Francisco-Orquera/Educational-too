# TODOS LOS DATOS DE ENTRADA ESTAN EN CENTIMETROS
base = float(input("Ingresa la base de la viga (cm): "))
recu = float(input("Ingresa el recubrimiento (cm): "))
dia_estribo = float(input("Ingresa el diametro del estribo (cm): "))
# MATRIZ DE DATOS, TABLA DE ACEROS
acero = float(input("Ingresa el acero que estas buscando (cm²): "))
limitante_d = int(input("Ingresa hasta que diametro de varilla quieres tomar en cuenta (mm): "))
tolerancia_error = float(input("Ingrese la tolerancia de su busqueda (ej. 0.05 para 0.05 cm²): "))
# TABLA DE ACEROS
TA = [[0,1,2,3,4,5,6,7,8,9,10,11,12],
    [6,0.28,0.57,0.85,1.13,1.41,1.70,1.98,2.26,2.54,2.83,3.11,3.39],
    [8,0.50,1.01,1.51,2.01,2.51,3.02,3.52,4.02,4.52,5.03,5.53,6.03],
    [10,0.79,1.57,2.36,3.14,3.93,4.71,5.50,6.28,7.07,7.85,8.64,9.42],
    [12,1.13,2.26,3.39,4.52,5.65,6.79,7.92,9.05,10.18,11.31,12.44,13.57],
    [14,1.54,3.08,4.62,6.16,7.70,9.24,10.78,12.32,13.85,15.39,16.93,18.47],
    [16,2.01,4.02,6.03,8.04,10.05,12.06,14.07,16.08,18.10,20.11,22.12,24.13],
    [18,2.54,5.09,7.63,10.18,12.72,15.27,17.81,20.36,22.90,25.45,27.99,30.54],
    [20,3.14,6.28,9.42,12.57,15.71,18.85,21.99,25.13,28.27,31.42,34.56,37.70],
    [22,3.80,7.60,11.40,15.21,19.01,22.81,26.61,30.41,34.21,38.01,41.81,45.62],
    [25,4.91,9.82,14.73,19.63,24.54,29.45,34.36,39.27,44.18,49.09,54.00,58.90],
    [28,6.16,12.32,18.47,24.63,30.79,36.95,43.10,49.26,55.42,61.58,67.73,73.89],
    [32,8.04,16.08,24.13,32.17,40.21,48.25,56.30,64.34,72.38,80.42,88.47,96.51],
    [38,11.34,22.68,34.02,45.36,56.71,68.05,79.39,90.73,102.10,113.40,124.8,136.1]]

def calcular_espaciamiento(num_varillas, diametro_varilla_mm, base_val, recu_val, dia_estribo_val):
    if num_varillas <= 1:
        return float('inf')
    diametro_varilla_cm = diametro_varilla_mm / 10.0
    espaciamiento = (base_val - (2 * recu_val) - (num_varillas * diametro_varilla_cm) - (2 * dia_estribo_val)) / (num_varillas - 1)
    return espaciamiento

def calcular_espaciamiento_combinado(num_varillas1, diametro1_mm, num_varillas2, diametro2_mm, base_val, recu_val, dia_estribo_val):
    diametro1_cm = diametro1_mm / 10.0
    diametro2_cm = diametro2_mm / 10.0
    
    total_varillas = num_varillas1 + num_varillas2
    if total_varillas <= 1:
        return float('inf')
    espaciamiento = (base_val - (2 * recu_val) - (2 * dia_estribo_val) - (num_varillas1 * diametro1_cm) - (num_varillas2 * diametro2_cm)) / (total_varillas - 1)
    return espaciamiento
    

def buscar_acero(acero_obj):
    for i in range(len(TA)):
        if limitante_d == TA[i][0]:
            for j in range(2,len(TA[0])):
                for k in range(1,i):
                    if acero_obj == TA[k][j]:
                        espaciamiento = calcular_espaciamiento(TA[0][j], TA[k][0], base, recu, dia_estribo)
                        if (espaciamiento >= 2.5):
                            print(f"necesitas {TA[0][j]} varillas de {TA[k][0]}  mm de diametro ")
                            print(f"el espaciamiento es {espaciamiento:.2f} cm")
                            print(f"la cantidad de acero es {acero_obj} cm²")
                            exit()
            
            for m in range(1,i):
                for n in range(1,len(TA[0])):
                    for l in range(m+1,m+3):
                        for o in range(2,len(TA[0])):
                            if l < len(TA) and TA[l][0] <= limitante_d:
                                suma = round((TA[m][n] + TA[l][o]),2)
                                espaciamiento2 = calcular_espaciamiento_combinado(TA[0][n], TA[m][0], TA[0][o], TA[l][0], base, recu, dia_estribo)
                                if (acero_obj == suma) and (espaciamiento2 >= 2.5):
                                    print(f"necesitas {TA[0][n]} varillas de {TA[m][0]}  mm de diametro y")
                                    print(f"{TA[0][o]} varillas de {TA[l][0]}  mm de diametro ")
                                    print(f"{TA[m][n]} + {TA[l][o]} = {suma} cm²")
                                    print(f"el espaciamiento es {espaciamiento2:.2f} cm")
                                    exit()
    return False

acero_inicial = acero
diametro_limitante_existe = False
for z in range(len(TA)):
    if limitante_d == TA[z][0]:
        diametro_limitante_existe = True
        break

if diametro_limitante_existe:
    i_entero = int((tolerancia_error*100)+1)
    for i in range(0,i_entero):
        buscar_acero(round(acero_inicial + (i * 0.01), 2))
else:
    print("Diametro no valido")
    exit()

print("No se a encontrado su requerimiento")

exit()
