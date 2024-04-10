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
    # Filtrar las ofertas por mes y año
    filtered_jobs = [oferta for oferta in data_structs['jobs'] if oferta['published_at'][:7] == f"{year}-{month:02d}"]
 
    # Crear los mapas para almacenar la información
    map_country_codes = mp.newMap(numelements=1000, maptype='PROBING', cmpfunction=None)
    map_key_country_code_value_lst_cities = mp.newMap(1000, maptype='PROBING', cmpfunction=None)
    map_cities = mp.newMap(numelements=1000, maptype='PROBING', cmpfunction=None)
    map_company_names = mp.newMap(numelements=1000, maptype='PROBING', cmpfunction=None)
    map_skills = mp.newMap(numelements=1000, maptype='PROBING', cmpfunction=None)
    map_multilocations = mp.newMap(numelements=1000, maptype='PROBING', cmpfunction=None)
    map_junior = mp.newMap(numelements=8, maptype='PROBING')
    map_mid = mp.newMap(numelements=8, maptype='PROBING')
    map_senior = mp.newMap(numelements=8, maptype='PROBING')

    # Crear una lista para almacenar los niveles de experticia
    niveles_de_experticia = lt.newList('ARRAY_LIST')
    lt.addLast(niveles_de_experticia, 'junior')
    lt.addLast(niveles_de_experticia, 'mid')
    lt.addLast(niveles_de_experticia, 'senior')

    # Recorrer las ofertas filtradas
    for oferta in lt.iterator(filtered_jobs):
        # Actualizar el mapa de códigos de país
        if not mp.contains(map_country_codes, oferta['country_code']):
            mp.put(map_country_codes, oferta['country_code'], 1)
        else:
            mp.put(map_country_codes, oferta['country_code'], mp.get(map_country_codes, oferta['country_code']) + 1)
        
        # Actualizar el mapa de claves de códigos de país y valores de listas de ciudades
        if not mp.contains(map_key_country_code_value_lst_cities, oferta['country_code']):
            mp.put(map_key_country_code_value_lst_cities, oferta['country_code'], lt.newList('SINGLE_LINKED', oferta['city']))
        else:
            lt.addLast(mp.get(map_key_country_code_value_lst_cities, oferta['country_code']), oferta['city'])
        
        # Actualizar el mapa de ciudades
        if not mp.contains(map_cities, oferta['city']):
            mp.put(map_cities, oferta['city'], 1)
        else:
            mp.put(map_cities, oferta['city'], mp.get(map_cities, oferta['city']) + 1)
        
        # Actualizar los mapas según el nivel de experticia
        for nivel_de_experticia in lt.iterator(niveles_de_experticia):
            if nivel_de_experticia == oferta['experience_level']:
                # Actualizar el mapa de nombres de empresas
                if not mp.contains(map_company_names, oferta['company_name']):
                    mp.put(map_company_names, oferta['company_name'], 1)
                else:
                    mp.put(map_company_names, oferta['company_name'], mp.get(map_company_names, oferta['company_name']) + 1)
                
                # Actualizar el mapa de habilidades
                for skill in lt.iterator(data_structs['skills']):
                    if skill['id'] == oferta['id']:
                        if not mp.contains(map_skills, skill['id']):
                            mp.put(map_skills, skill['id'], 1)
                        else:
                            mp.put(map_skills, skill['id'], mp.get(map_skills, skill['id']) + 1)
                
                # Actualizar el mapa de multilocaciones
                for multilocation in lt.iterator(data_structs['multilocations']):
                    if multilocation['id'] == oferta['id']:
                        if not mp.contains(map_multilocations, multilocation['id']):
                            mp.put(map_multilocations, multilocation['id'], 1)
                        else:
                            mp.put(map_multilocations, multilocation['id'], mp.get(map_multilocations, multilocation['id']) + 1)
                
                # Obtener una sublista de claves de códigos de país
                sublst_n_country_codes = lt.subList(mp.keySet(map_country_codes), 1, n_paises)

    # Calcular el total de ofertas de empleo
    total_ofertas = sum(mp.valueSet(map_country_codes))
    
    # Calcular el número de ciudades donde se ofertó en los países resultantes de la consulta
    cantidad_cities = size(map_cities)
    
    # Calcular el promedio del nivel de habilidades solicitadas en las ofertas de trabajo
    promedio_nivel_skills = sum(mp.valueSet(map_skills)) / size(map_skills)

    # Encontrar el país con la mayor cantidad de ofertas
    max_country_count = float('-inf')
    max_country_code = None
    for country_code in mp.keySet(map_country_codes):
        count = mp.get(map_country_codes, country_code)
        if count > max_country_count:
            max_country_count = count
            max_country_code = country_code
    max_country_name = data_structs['country_codes'][max_country_code]

    # Encontrar la ciudad con la mayor cantidad de ofertas
    max_city_count = float('-inf')
    max_city_name = None
    for city_name in mp.keySet(map_cities):
        count = mp.get(map_cities, city_name)
        if count > max_city_count:
            max_city_count = count
            max_city_name = city_name

    # Inicializar el diccionario para almacenar la información de los niveles de experticia
    expertises_info = {}
    
    # Calcular información para cada nivel de experticia
    for expertise in lt.iterator(niveles_de_experticia):
        count_skills = size(map_skills)

        # Encontrar la habilidad más solicitada
        most_requested_skill_count = float('-inf')
        most_requested_skill = None
        for skill_id in mp.keySet(map_skills):
            count = mp.get(map_skills, skill_id)
            if count > most_requested_skill_count:
                most_requested_skill_count = count
                most_requested_skill = skill_id

        # Encontrar la habilidad menos solicitada
        least_requested_skill_count = float('inf')
        least_requested_skill = None
        for skill_id in mp.keySet(map_skills):
            count = mp.get(map_skills, skill_id)
            if count < least_requested_skill_count:
                least_requested_skill_count = count
                least_requested_skill = skill_id

        min_avg_skill_level = None  # A completar
        count_companies = size(map_company_names)

        # Encontrar la empresa con más ofertas
        max_offer_company_count = float('-inf')
        max_offer_company = None
        for company_name in mp.keySet(map_company_names):
            count = mp.get(map_company_names, company_name)
            if count > max_offer_company_count:
                max_offer_company_count = count
                max_offer_company = company_name

        # Encontrar la empresa con menos ofertas
        min_offer_company_count = float('inf')
        min_offer_company = None
        for company_name in mp.keySet(map_company_names):
            count = mp.get(map_company_names, company_name)
            if count < min_offer_company_count:
                min_offer_company_count = count
                min_offer_company = company_name

        multilocation_count = size(map_multilocations)

        # Agregar la información del nivel de experticia al diccionario
        expertises_info[expertise] = {
            "count_skills": count_skills,
            "most_requested_skill": most_requested_skill,
            "most_requested_skill_count": most_requested_skill_count,
            "least_requested_skill": least_requested_skill,
            "least_requested_skill_count": least_requested_skill_count,
            "min_avg_skill_level": min_avg_skill_level,
            "count_companies": count_companies,
            "max_offer_company": max_offer_company,
            "max_offer_company_count": max_offer_company_count,
            "min_offer_company": min_offer_company,
            "min_offer_company_count": min_offer_company_count,
            "multilocation_count": multilocation_count
        }

    # Retornar los resultados calculados
    return total_ofertas, cantidad_cities, max_country_name, max_country_count, max_city_name, max_city_count, expertises_info


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
