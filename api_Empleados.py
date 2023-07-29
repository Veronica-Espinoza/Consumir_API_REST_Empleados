from statistics import mean
import requests

def obtener_empleados(ruta):
    #Acceso a la ruta
    empleados = requests.get(ruta, headers={'User-Agent':'insomnia/2022.1.1', 'accept': '/'})

    #Extraccion API
    #print (empleados.text)
    print(empleados.text)
    empleados = empleados.json()

    #Extraccion de los datos del api
    datos = empleados['data']

    #Creacion de listas de salario y edad
    nombre = []
    salario = []
    edad = []
    for dato in datos:
        nombre.append(dato['employee_name'])
        salario.append(dato['employee_salary'])
        edad.append(dato['employee_age'])

    #Impresion de las listas con la informacion de la Api
    print('Datos a utilizar:')
    #print('Nombres de los empleados:', nombre)
    print('Salario de los empleados:', salario)
    print('Edad de los empleados:', edad)
    print('')

    #Resultados de los  datos  API :
    print('Consumir Api')
    # Cuantos empleados son:
    print('Total de empleados:', len(datos),'empleados')
    # Cual es promedio de salario de los empleados,
    print('Promedio del salario de los empleados: ', mean(salario))
    # Cual es el promedio de edad de los empleados,
    print('Promedio de edad de los empleados:', mean(edad))

    # cual es salario mínimo y máximo,
    print('Salario Minimo: $', min(salario))
    print('Salario Maximo: $', max(salario))
    # cual es es la edad menor y mayor de los empleados.
    print('Edad menor de los empleados:', min(edad))
    print('Edad mayor de los empleados:', max(edad))

if __name__ == '__main__':
    ruta = 'https://dummy.restapiexample.com/api/v1/employees'
    obtener_empleados(ruta)
