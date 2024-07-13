'''
Bonus Track 1: edades

Un desarrollador anterior a nosotros creó un reporte con las edades de los estudiantes que
utilizan la aplicación. El mismo solamente devuelve un arreglo desordenado con las posibles
edades de los mismos (sin repeir). El resultado para nuestros 6 estudiantes fue un arreglo con
los siguientes valores estáticos:

edades = [21, 18, 20, 19, 23, 24]

Teniendo en cuenta el resultado de dicho reporte, se pide un algoritmo que primero ordene
dicho arreglo, y luego realice una búsqueda secuencial para detectar si hay algún “hueco” en las
edades detectadas. Llámese hueco a un número faltante para poder tener una secuencia
autoincremental. Por ejemplo, en la secuencia 1,2,3,5 tendríamos 1 hueco, y el elemento
faltante sería 4.


Bonus Track 2: matcheos combinados

Sacando desde nuestro arreglo la cantidad de usuarios estudiantes cargados, calcular la cantidad
de matcheos posibles, suponiendo que cualquier estudiante podría matchear con cualquier
estudiante que no sea sí mismo, independientemente del sexo.
'''
def bonus1():
    edades = [21, 18, 20, 19, 23, 24]
    contador = 0
    print("~"*50, "|Bonus track 1|", "~"*50)
    for i in range(len(edades)):
        for j in range(len(edades)):
            if edades[i] < edades[j]:
                aux = edades[j] 
                edades[j] = edades[i]
                edades[i] = aux
    print(edades)
    for i in range(len(edades)-1):
        if int(edades[i]) != int(edades[i+1]) -1:
            contador += 1
            print("hay", contador, "hueco/s")
    

bonus1()