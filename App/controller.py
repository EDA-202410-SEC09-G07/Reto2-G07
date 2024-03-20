"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control={"model" :None}
    return control


# Funciones para la carga de datos
def compare( mapa,tamaño, fc1,bandera):
    
    mapa = int(mapa)
    tamaño = int(tamaño)
    fc1 = int(fc1)
    
   
    if mapa == 1:
        fc = 0.1
        estructura = "PROBING"
        if fc1 == 1: 
            fc = 0.1
        if tamaño == 2:
            fc = 0.5
        if tamaño == 3:
            fc = 0.7
        if tamaño == 4:
            fc = 0.9
    else:
        estructura = "CHAINING"
        fc = 1
        if fc1 == 1: 
            fc = 2
        if tamaño == 2:
            fc = 4
        if tamaño == 3:
            fc = 6
        if tamaño == 4:
            fc = 8
  
    tm = 'small-'
    if tamaño == 2:
        tm = "medium-"
    if tamaño == 3:
        tm = "large-"
    if tamaño == 4:
        tm = "10-por-"
    if tamaño == 5:
        tm = "20-por-"
    if tamaño == 6:
        tm = "30-por-"
    if tamaño == 7:
        tm = "40-por-"
    if tamaño == 8:
        tm = "50-por-"
    if tamaño == 9:
        tm = "60-por-"
    if tamaño == 10:
        tm = "70-por-"
    if tamaño == 11:
        tm = "80-por-"
    if tamaño == 12:
        tm = "90-por-"
    
      
    if bandera == "2":
        flag = True
    else:
        flag = False
        
    return estructura, tm,fc,flag

def load_data(control, mapa,tamaño, fc1,bandera):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    estructura, tm,fc,flag=compare( mapa,tamaño, fc1,bandera)
    control['model'] = model.new_data_structs(estructura, fc)

    # inicializa el proceso para medir memoria
    if flag:
        tracemalloc.start()
        start_memory = get_memory() # Mido la memmoria antes de inicializar los datos, o antes de la carga de datos
    
    start_time = get_time()

    total_ofertas,total_empresas, total_ciudades = load_jobs(control['model'], tm)
    
    

    # finaliza el proceso para medir memoria
    Delta_memory = 0
    Delta_time = 0

    if flag:
        stop_memory = get_memory() # La memoria que se esta usando al finalizar la carga de datos
        tracemalloc.stop()
        # calcula la diferencia de memoria
        Delta_memory = delta_memory(stop_memory, start_memory)
    
        # toma el tiempo al final del proceso
    stop_time = get_time()
        # calculando la diferencia en tiempo
    Delta_time = delta_time(start_time, stop_time)

    return total_ofertas,total_empresas, total_ciudades, Delta_time,Delta_memory

def load_jobs(control, size):
    jobs = cf.data_dir + str(size) + "jobs.csv"
    input_file = csv.DictReader(open(jobs, encoding="utf-8"), delimiter=";") # Lista de diccionariuos de las de python
    count=0
    for job in input_file:
        model.add_jobs(control, job)
        count=count+1
    print("----------")
    print(count)

    
    
    total_ofertas=model.size_mapa(control['jobs'])
    total_empresas=model.size_mapa(control['jobs_empresa'])
    total_ciudades=model.size_mapa(control['jobs_ciudad'])
    
    return total_ofertas, total_empresas, total_ciudades
    
    


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
