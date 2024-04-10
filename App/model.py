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
import datetime

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


def req_1(data_structs, N, country, level):
    filter_data = lt.newList('ARRAY_LIST') # O(1)
    map_by_country = data_structs['jobs_country'] # O(1)
    country_jobs = (mp.get(map_by_country, country))['value'] # O(1)
    
    amount_jobs_country = lt.size(country_jobs)
    
    for job in lt.iterator(country_jobs): # O (h) siendo h la cantidad de ofertas que haya en la ciudad
        if job['experience_level'] == level: # O(1)
            lt.addLast(filter_data, job)

    merg.sort(filter_data, sort_job_by_date) # O(klog(k)) siendo k la cantidad de ofertas que cumplan con el nivel de experiencia y el país
    
    amount_jobs_experience = lt.size(filter_data) # O(1)
    
    
    if N > lt.size(filter_data): # O(1)
        N = lt.size(filter_data)
    
    answer = lt.subList(filter_data, 1, N) # O(N) SIendo n la cantidad de datos que nos piden
    
    return answer, amount_jobs_country, amount_jobs_experience


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

def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


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
    valores = mp.valueSet(control['jobs_ciudad'])
    llaves = mp.keySet(control["jobs_ciudad"])
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
    valores2 = mp.valueSet(mapa)
    llaves2 = mp.keySet(mapa)
    n_empresas = mp.size(mapa)
    n_ciudades = lt.size(llaves)
    i = 0
    while i < int(numero_ciudad):
        inicial_size = 0 
        job3 = ""
        llave3= ""
        for job in lt.iterator(valores2):
            for llave in lt.iterator(llaves2):
                size = len(job["elements"])
                if size > inicial_size:
                    inicial_size = size 
                    job3 = job["elements"]
                    llave3 = llave
        
            
                pos2 = lt.isPresent(llaves2, llave3)
                lt.deleteElement(llaves2, pos2)
                mp.put(mapa_retorno, llave3, job3) 
                
                i += 1
    return mapa_retorno, n_ciudades, n_empresas 
            
            


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(control, level, divisa, initial_date, final_date):
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

def sort_job_by_date(job1, job2):
    
    # job1['published_at'] = datetime.datetime.strptime(job1['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    # job2['published_at'] = datetime.datetime.strptime(job2['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    
    return job1['published_at'] > job2['published_at']

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
