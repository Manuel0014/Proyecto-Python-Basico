numero_alumnos=int(input("Ingrese la cantidad de alumnos: "));
l1=[]
l3=[]
prom=[]
for i in range(numero_alumnos):
    nombre = input("Ingrese el nombre del alumno {}: ".format(i+1))
    # apellido = input("Ingrese el apellido: ")
    # seccion = input("Ingrese la seccion: ")
    # grado = input("Ingrese el grado: ")
    j=0
    l2=[]
    while 3 > j:
        notas = int(input("Ingrese la nota {}: ".format(j+1)))
        if notas < 0 or notas > 20:
            print("Error, usted ha ingresado una nota erronea.")
            continue
        l2.append(notas)
        j+=1;
    def promedio ():
        Promedio=round(sum(l2)/3, 1)
        return Promedio;
    
    prom.append(promedio()) #lista de promedios
    
    def promedio_mayor():
        max = prom[0]
        for x in prom:
            if x > max:
                max = x;
        
        return max
    
    encontrar_nota_mayor=prom.index(promedio_mayor())
    
    l3.append(l2)
    l1.append(nombre)
    
    print(promedio())
    print("\n")

def alumno_con_mejor_promedio():
    mejor_promedio=l1[encontrar_nota_mayor].upper()
    return mejor_promedio;
    
print(f'Lista de alumnos: {l1}') 
print(f'Lista de notas: {l3}')
print("-------------------------------------------------")
print(f'El alumno {alumno_con_mejor_promedio()} obtuvo el mejor promedio con : {promedio_mayor()}')

