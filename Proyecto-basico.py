# Crear un programa para mostrar el promedio de calificación de alumnos, utilizando los fundamentos de Python.

cantidad_alumnos = int(input("Ingrese la cantidad de estudiantes: "));

for i in range(cantidad_alumnos):
    print(f'Datos del estudiante {i+1}')
    nombre = input("Nombre: ".format(i))
    apellido = input("Apellido: ".format(i))
    seccion = input("Seccion: ".format(i))
    grado = input("Grado: ".format(i))
    cantidad_notas = int(input("Ingrese la cantidad de notas: "));
    j=0
    acumulado=0
    mayor = 0
    menor = 21
    if cantidad_notas == 0 or cantidad_notas < 0:
        print("Usted esta descalificado")
        continue
    while cantidad_notas > j:
        notas = int(input("Nota {}: ".format(j+1)));
        if notas > 20 or notas < 0 :
            print("Error, usted ha ingresado una nota incorrecta")
            continue
        if notas > mayor:
            mayor = notas
        if notas < menor:
            menor = notas
        acumulado = acumulado + notas
        j +=1;
        
    promedio = acumulado/cantidad_notas
    if promedio < 10.5:
        print("Ha desaprobado el curso")
    else:
        print("Felicidades, aprobó el curso")  
    print(f'La nota mayor es: {mayor}')
    print(f'La nota menor es: {menor}')  
    print(f'El promedio del estudiante es {promedio}')
    print("\n")

