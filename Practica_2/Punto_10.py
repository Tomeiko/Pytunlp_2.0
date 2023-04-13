nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def generacion (alumnos, resultados_1, resultados_2):
    """ Esta funcion recibe tres paramatros que son listas que contienen los nombres, la primera nota y la segunda nota respectivamente.
    Lo primero que hace es crear un diccionario vacio (union) para despues limpiar y separar los nombres, con los nombres limpios y las resultados 1 y 2
    les aplica una funcion zip para juntarlos y gracias al for recorrer la estructura y tomar el nombre, la nota1 y la nota2 y agregarlos al diccionario 
    vacio de tuplas (union). Al finalizar el for la funcion retorna el diccionario con tuplas (union)"""
    union = {}
    alumnos_limpios = alumnos.lower().replace(" ", "").replace("\n", "").replace("'","").split(",")
    for nombre, nota1, nota2 in zip(alumnos_limpios, resultados_1, resultados_2):
        union[nombre] = (nota1, nota2)
    return union

def promestudiante (union):
    """ Esta funcion recibe un parametro que es un diccionario de tuplas (union) con el nombre y ambas notas del alumno.
    Lo primero que hace es crear un diccionario vacio (promedios) para luego tomar el nombre y las notas del diccionario
    (union) mediante un for a los items del diccionario (union), con los que agrega el promedio (mediante la funcion sum 
    a la tupla (valor) y luego dividirla por 2) a cada clave que va guardando en el nuevo diccionario llamado promedios.
    Retorna un diccionario con numeros reales"""
    promedios = {}
    for clave, valor in union.items():
        promedios[clave] = sum(valor)/2
    return promedios

def promcurso (promedios):
    """ Esta funcion recibe un parametro que es un diccionario de numeros reales con el nombre y el promedio de cada alumno.
    Lo primero que hace es iniciar una variable prom en 0 para luego tomar el promedio del diccionario(promedios) mediante un 
    for a los values del diccionario (promedios) y irselos sumando a la variable prom. Una vez que finaliza el for la funcion
    retorna prom divido la longitud del diccionario promedios ya que asi obtiene el promedio del diccionario"""
    prom = 0
    for valor in promedios.values():
        prom += valor
    return prom / len(promedios)

def notaalta (promedios):
    """ Esta funcion recibe un parametro que es un diccionario de numeros reales con el nombre y el promedio de cada alumno.
    Retorna el nombre del alumno con el promedio mas alto ya usa la funcion lambda para obtener los promedios y luego
    compararlos para obtener el nombre y asi finalmente el nombre del alumno con el mayor promedio"""
    return max(promedios, key= lambda nombre: promedios[nombre])

def notabaja (union):
    """ Esta funcion recibe un parametro que es un diccionario de tuplas (union) con el nombre y ambas notas del alumno.
    Retorna el nombre del alumno que tenia la nota mas baja mediante una funcion lambda que obtiene la nota minima entre
    las 2 notas de cada alumno y luego obtiene el alumno que tenia la nota minima entre las notas minimas"""
    return min(union, key= lambda nombre: min(union[nombre]))

union = generacion(nombres, notas_1, notas_2)
promedios = promestudiante(union)

print("-"*46)
print(f'Las notas de cada alumno son: \n {union}')
print("-"*46)
print(f'El promedio de cada alumnos es: \n {promedios}')
print("-"*46)
print(f'El promedio del curso es {round(promcurso(promedios),2)}')
print("-"*46)
print(f'El alumno con el promedio mas alto es {notaalta(promedios)}')
print("-"*46)
print(f'El alumno con la nota mas baja es {notabaja(union)}')
print("-"*46)