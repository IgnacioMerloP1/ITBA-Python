def calcular_promedio(nota1,nota2,nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

def calcular_promedio_clase(prom_clase, cant_alum):
    promedio_clase = prom_clase / cant_alum
    return promedio_clase

def calculadora():
    cant_alum = int(input("Ingrese la cantidad de alumnos que tiene el curso: "))
    alumnos = []
    notamasalta = 0
    notamasbaja = 100
    prom_clase = 0

    for _ in range(cant_alum):
        alumno = input("Ingrese el nombre y apellido del alumno: ")
        nota1 = float(input("Ingrese el resultado del primer examen: "))
        nota2 = float(input("Ingrese el resultado del segundo examen: "))
        nota3 = float(input("Ingrese el resultado del tercer examen: "))
        
        promedio = calcular_promedio(nota1,nota2,nota3)
        prom_clase += promedio
        alumno_info = {
            'alumno': alumno,
            'nota1': nota1,
            'nota2': nota2,
            'nota3': nota3,
            'promedio': promedio
        }
        alumnos.append(alumno_info)

        
        if nota1 > notamasalta:
            notamasalta = nota1
        elif nota2 > notamasalta:
            notamasalta = nota2
        elif nota3 > notamasalta:
            notamasalta = nota3
        else: pass

        if nota1 < notamasbaja:
            notamasbaja = nota1
        elif nota2 < notamasbaja:
            notamasbaja = nota2
        elif nota3 < notamasbaja:
            notamasbaja = nota3
        else: pass
    prom_clase_final = calcular_promedio_clase(prom_clase, cant_alum)
    for alumno_info in alumnos:
        print(f"Alumno: {alumno_info['alumno']}, Promedio: {alumno_info['promedio']}")
    print(f"La nota mas alta del curso fue: {notamasalta}. La nota mas baja del curso fue: {notamasbaja}")
    print(f"El promedio de calificaciones de toda la clase es: {prom_clase_final} \n")
    print("Estudiantes por encima del promedio de la clase: ")
    for alumno_info in alumnos:
        if alumno_info['promedio'] > prom_clase_final:
            print(alumno_info['alumno'])
calculadora()
