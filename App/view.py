"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
#from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control=controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, mapa,tamaño, fc,bandera):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control, mapa,tamaño, fc,bandera)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, N, code_country, level):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    sublist = controller.req_1(control, N, code_country, level)
    
    for element in lt.iterator(sublist):
        print(f"Fechas: {element['published_at']}")
        print(f"Titulo Oferta: {element['title']}")
        print(f"Empresa: {element['company_name']}")
        print(f"Nivel de experiencia: {element['experience_level']}")
        print(f"País: {element['country_code']}")
        print(f"Ciudad de la oferta: {element['city']}")
        print(f"Tamaño de la empresa: {element['company_size']}")
        print(f"Tipo de empleo: {element['workplace_type']}")
        print(f"Disponibilidad Ucranianos {element['open_to_hire_ukrainians']}\n\n")
         
    return sublist

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control, company_name, initial_date, final_date):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    lista_ofertas_empresa, juniors, mids, seniors  = controller.req_3(control, company_name, initial_date, final_date)

    print("Ofertas de trabajo publicadas por la empresa: " + company_name)
    print(lt.size(lista_ofertas_empresa))
    print("Ofertas de trabajo publicadas por la empresa por nivel de experiencia")
    print(f"Juniors: {juniors}" )
    print(f"Mids: {mids}" )
    print(f"Seniors: {seniors}" )
        
    counter = 0
    for job in lt.iterator(mp.valueSet(lista_ofertas_empresa)):
        
        if counter == 21:
            break
        print(f"Fechas: {job["elements"][0]['published_at']}")
        print(f"Titulo Oferta: {job["elements"][0]['title']}")
        print(f"Empresa: {job["elements"][0]['company_name']}")
        print(f"Nivel de experiencia: {job["elements"][0]['experience_level']}")
        print(f"País: {job["elements"][0]['country_code']}")
        print(f"Ciudad de la oferta: {job["elements"][0]['city']}")
        print(f"Tamaño de la empresa: {job["elements"][0]['company_size']}")
        print(f"Tipo de empleo: {job["elements"][0]['workplace_type']}")
        print(f"Disponibilidad Ucranianos {job["elements"][0]['open_to_hire_ukrainians']}\n\n")
        counter += 1


def print_req_4(control, n_pais, fecha_i, fecha_f):
    ofertas_pais , listado_empresas_o, map_cities= controller.req_4(control, n_pais, fecha_i, fecha_f)
    print("Ofertas de trabajo publicadas en el país: " + n_pais)
    print(lt.size(ofertas_pais))
    print("el total de empresas que publicaron al menos una oferta: {listado_empresas_o}".format(listado_empresas_o=listado_empresas_o))
    print("Número total de ciudades del país de consulta en las que se publicaron ofertas.1 {map_cities}".format(map_cities=map_cities))
    print("La ciudad con mayor número de ofertas es : con:")
    print("La ciudad con menor número de ofertas es: con:")
    counter = 0
    for job in lt.iterator(mp.valueSet(ofertas_pais)):
        
        if counter == 10:
            break
        print(f"Fecha de publicación de la oferta: {job['elements'][0]['published_at']}")
        print(f"Titulo de la oferta: {job['elements'][0]['title']}")
        print(f"Nivel de experiencia requerido: {job['elements'][0]['experience_level']}")
        print(f"Nombre de la Empresa: {job['elements'][0]['company_name']}")
        print(f"Ciudad de la oferta: {job['elements'][0]['city']}")
        print(f"Tipo de lugar de trabajo: {job['elements'][0]['employment_type']}")
        print(f"Tipo de trabajo, si es remoto o no: {job['elements'][0]['remote']}")
        print(f"Disponibilidad Ucranianos {job['elements'][0]['open_to_hire_ukrainians']}\n\n")
        counter += 1

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            print("_________________________________________")
            
            print("\nSeleccione una opción para continuar")
            print("\nTipos de mapa")
            print(" 1. PROBING \n 2. CHAINING")

            mapa= input("\nSeleccione un tipo de mapa: ")
    

            print("\nTamaño de los archivos: ")
            print(" 1. small\n 2.medium\n 3. large \n 4. 10 porciento\n 5. 20 porciento\n 6. 30 porciento\n 7. 40 porciento \n 8. 50 porciento \n 9. 60 porciento\n 10. 70 porciento\n 11. 80 porciento\n 12. 90 porciento")
    
            tamaño = input("\nSeleccione el tamaño de los archivos: ")
            
            print("\nFactor de carga del mapa: ")
            if mapa == "1":
                print(" 1) 0.1\n 2) 0.5\n 3) 0.7\n 4) 0.9")
            else:
                print(" 1) 2.00\n 2) 4.00\n 3) 6.00\n 4) 8.00")

            fc = input("\nSeleccione el factor de carga del mapa: ")
            print("\nQue quieres calcular")
            print(" 1. Tiempo \n 2. Memoria")

            bandera= input("\nSeleccione que quiere calcular: ")
            
            total_ofertas,total_empresas, total_ciudades ,delta_time, delta_memory = load_data(control, mapa,tamaño, fc,bandera)
            print("_______________________________")
            print("El total de ofertas de trabajo publicadas cargada"+str(total_ofertas))
            print("El total de empreas es: "+str(total_empresas))
            print("EL total de ciudades es: "+str(total_ciudades))
            if bandera =="2":
                print("memoria: "+str(delta_memory))
            print("tiempo: "+str(delta_time))

        elif int(inputs) == 2:
            N = int(input("Numero de ofertas a listar: "))
            code_country = input("Código del país: ")
            level = input("Nivel de experticia: ")
            print_req_1(control, N, code_country, level)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            company_name = input("Nombre de la empresa: ")
            initial_date = input("Fecha inicial (YYYY-MM-DD): ")
            final_date = input("Fecha final (YYYY-MM-DD): ")
            print_req_3(control, company_name, initial_date, final_date)

        elif int(inputs) == 5:
            n_pais = input("Codigo del país:")
            fecha_i = input("Fecha inicial (YYYY-MM-DD): ")
            fecha_f = input("Fecha final (YYYY-MM-DD): ")
            print_req_4(control, n_pais, fecha_i, fecha_f )

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            numero_ciudad = input("Número de ciudades para consulta: ")
            level = input("Nivel de experticia: ")
            year = input("año")
            print_req_6(control, numero_ciudad, level, year)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            level = input("Nivel de experticia: ")
            divisa = input("Divisa de la consulta")
            initial_date = input("Fecha inicial (YYYY-MM-DD): ")
            final_date = input("Fecha final (YYYY-MM-DD): ")
            print_req_8(control, level, divisa, initial_date, final_date)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
