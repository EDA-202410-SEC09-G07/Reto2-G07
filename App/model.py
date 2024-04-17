﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from datetime import datetime
from math import sqrt

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(estructura,fc):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    control = {
            'jobs': None,
            'skills': None,
            'employment': None,
            'multilocation': None}
    

    control['jobs'] = mp.newMap(1000,
                                 maptype=estructura,
                                 loadfactor=fc)
    control['skills'] = mp.newMap(1000,
                                     maptype=estructura,
                                     loadfactor=fc
                                     )
    control['employment'] = mp.newMap(1000,
                                    maptype=estructura,
                                    loadfactor=fc
                                    )
    control['multilocation'] = mp.newMap(1000, 
                                        maptype=estructura,
                                        loadfactor=fc)
    control['jobs_country'] = mp.newMap(1000, 
                                        maptype=estructura,
                                        loadfactor=fc)
    control['jobs_empresa'] = mp.newMap(7000, 
                                        maptype=estructura,
                                        loadfactor=fc)
    control['jobs_ciudad'] = mp.newMap(7000, 
                                        maptype=estructura,
                                        loadfactor=fc)
    
    

    
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    return control


# Funciones para agregar informacion al modelo

def add_jobs(control, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    jobs=control["jobs"]
    ID=data["id"] # 123
    mp.put(jobs, ID,data) # Pasi es colombia
    # Primer mapa, quie es un mapa de jobs, por llave de ID

            
    entry = mp.get(control["jobs_country"], data["country_code"])
    # Segfundo mapa que es un mapa de jobs, y la llave es el pais
    if entry is not None:
        lst = me.getValue(entry)
        lt.addLast(lst, data) 
    else:
        lst = lt.newList("ARRAY_LIST")
        lt.addLast(lst, data)
        mp.put(control["jobs_country"], data["country_code"], lst)

    entry = mp.get(control["jobs_empresa"], data["company_name"])
    # Tercer mapa nombre de la compañia
    if entry is not None:
        lst = me.getValue(entry)
        lt.addLast(lst, data) 
    else:
        lst = lt.newList("ARRAY_LIST")
        lt.addLast(lst, data)
        mp.put(control["jobs_empresa"], data["company_name"], lst)


    entry = mp.get(control["jobs_ciudad"], data["city"])
    # Tercer mapa ciudad
    if entry is not None:
        lst = me.getValue(entry)
        lt.addLast(lst, data) 
    else:
        lst = lt.newList("ARRAY_LIST")
        lt.addLast(lst, data)
        mp.put(control["jobs_ciudad"], data["city"], lst)
    return control
  
    


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def values (mapa):
    lista_values=mp.valueSet(mapa)
    return lista_values
def keys (mapa):
    lista_keys=mp.keySet(mapa)
    return lista_keys
def size_mapa(mapa):
    return mp.size(mapa)

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs)


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(control, company_name, initial_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3

    mapa_ofertas_empresa = control['jobs_empresa']
    valores = mp.valueSet(control['jobs_empresa'])
    
    lista_ofertas_empresa = me.getValue(mp.get(mapa_ofertas_empresa, company_name))
    
    
    junior = 0
    mid = 0
    senior = 0
    print(type(mapa_ofertas_empresa))
    
    for job in lt.iterator(valores):
        if job["elements"][0]['company_name'] == company_name and str(job["elements"][0]['published_at']) >= initial_date and str(job["elements"][0]['published_at']) <= final_date:
            lt.addLast(lista_ofertas_empresa, job)
            if job["elements"][0]['experience_level'] == 'junior':
                junior += 1
            elif job["elements"][0]['experience_level'] == 'mid':
                mid += 1
            else:
                senior += 1
    return mapa_ofertas_empresa, junior, mid, senior

def req_4(control, n_pais, fecha_i, fecha_f):
    """
    Función que soluciona el requerimiento 4
    """
    mapa_ofertas_pais = control["jobs_country"]
    valores = mp.valueSet(mapa_ofertas_pais)
    ofertas_pais = me.getValue(mp.get(mapa_ofertas_pais, n_pais))
    listado_empresas_o = mp.newMap(numelements=100, maptype='PROBING', cmpfunction=None)
    
    # Crear un mapa para almacenar el número de ofertas por ciudad
    map_cities = mp.newMap(numelements=100, maptype='PROBING', cmpfunction=None)
    val_menor_map_cities = 10000
    val_mayor_map_cities = 0
    
    for job in lt.iterator(valores):
        if job["elements"][0]["country_code"] == n_pais and str(job["elements"][0]["published_at"]) >= fecha_i and str(job["elements"][0]['published_at']) <= fecha_f:
            lt.addLast(ofertas_pais, job)
            
            # Contar empresas
            if not mp.contains(listado_empresas_o, job['company_name']):
                mp.put(listado_empresas_o, job['company_name'], 1)
            else:
                mp.put(listado_empresas_o, job['company_name'], mp.get(listado_empresas_o, job['company_name']) + 1)
                
            # Contar ciudades
            if not mp.contains(map_cities, job['city']):
                mp.put(map_cities, job['city'], 1)
            else:
                mp.put(map_cities, job['city'], mp.get(map_cities, job['city']) + 1)
                
                val_menor_map_cities = min(val_menor_map_cities, mp.get(map_cities, job['city']))
                val_mayor_map_cities = max(val_mayor_map_cities, mp.get(map_cities, job['city']))

    
    return mapa_ofertas_pais, listado_empresas_o, map_cities, val_mayor_map_cities, val_menor_map_cities

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(control, numero_ciudad, level, year):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    valores = mp.getValue(control['jobs_ciudad'])
    llaves = mp.getKeys(control["jobs_ciudad"])
    mapa = mp.newMap(numelements=10,
           prime=20,
           maptype='PROBING',
           loadfactor = 1,
           cmpfunction=None)
    for job in lt.iterator(valores):
        for llave in lt.iterator(llaves):
            if job["elements"][0]["experience_level"] == level and (job["elements"][0]["published_at"])[0:4] == year:
                mp.put(mapa, llave, job)
                
    mapa_retorno = mp.newMap(numelements=10,
           prime=20,
           maptype='PROBING',
           loadfactor = 1,
           cmpfunction=None)
    valores2 = mp.getValue(mapa)
    llaves2 = mp.getKeys(mapa)
    
    i = 0
    while i < int(numero_ciudad):
        inicial_size = 0 
        job3 = ""
        llave3= ""
        for job in valores2:
            for llave in llaves2:
                size = len(job["elements"])
                if size > inicial_size:
                    inicial_size = size 
                    job3 = job["elements"]
                    llave3 = llave 
        valores2["elements"].remove(job3)
        llaves2["elements"].remove(llave3)
        mp.put(mapa_retorno, llave3, job3) 
        i += 1
    return mapa_retorno 
            

def req_7(data_structs, n_paises, year, month):
    """
    Función que soluciona el requerimiento 7
    """
    


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
