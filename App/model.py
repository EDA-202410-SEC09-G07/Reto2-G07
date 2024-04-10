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


from matplotlib import table
from numpy import average
from sympy import false
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
  
def add_skills(control, skill):
    """
    Función para agregar nuevas categorias
    """
    try:
        map_skills = control['skills']
        skill_id = skill['id']
        mp.put(map_skills, skill_id, skill)
    except:  # noqa: E722
        print(f"Error al agregar la habilidad {skill}")
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
            
            
#! =================================== REQUERIMIENTO 7  ===================================

def req_7(data_structs, amount_countries, year, month):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    amount_offers = 0 #! TOTAL OFERTAS EMPLEO
    countries_map = data_structs['jobs_country'] # Saco toda la informacion de este mapa 
    cities_map = mp.newMap(1000, maptype='PROBING', loadfactor=0.5) # Un mapa de ciudades vacio
    level_map = mp.newMap(3, maptype='PROBING', loadfactor=0.5) # Un mapa de nivel de experticia vacio
    countries_info = mp.valueSet(countries_map) #Saca un alista con los datos de los paises
    filter_countries = lt.newList('ARRAY_LIST')
    
    for country in lt.iterator(countries_info): # #? O(N) siendo N la cantidad de ofertas de empleo
        countries_list = lt.newList('ARRAY_LIST') # Crea una lista de paises
        for job in lt.iterator(country): # Itera sobre todos esos jobs
            job = examine_job_by_date(job, year, month) # Examine si cumple los requisitos de busqueda
            
            if job is not None: # Si cumple los requisitos
                add_job_to_cities_map(job, cities_map) # Agrega el trabajo el mapa de ciudades
                lt.addLast(countries_list, job) # Agrega el trabajo a la lista de trabajos
        if lt.size(countries_list) > 0: # Si la lista de trabajos no esta vacia
            lt.addLast(filter_countries, countries_list) 
            amount_offers += lt.size(countries_list)
    
    amount_cities = mp.size(cities_map) #! Saca la cantidad de ciudades que cumplen los cirterio s de busqueda
    
    #Obtener el pais con la mayor cantidad de ofertas
    best_country = obtain_best_country(filter_countries) #? O(HlogH) siendo H la cantidad de paises que cumplen con los criterios de busqueda
    #Obtener la ciudad con la mayor cantidad de ofertas
    best_city = obtain_best_city(cities_map) #? O(KlogK) siendo K la cantidad de ciudades que cumplen con los criterios de busqueda
    
    if amount_countries > lt.size(filter_countries): # SI se pieden mas paises de los que hay solo se usan los paises que haya
        amount_countries = lt.size(filter_countries)
        
    filter_countries = lt.subList(filter_countries, 1, amount_countries) # Una sublistas con los paises de consulta
    # Consulta sobre niveles de experticia
    for country in lt.iterator(filter_countries): #? O(R) siendo N la cantidad de paises que cumplen con los criterios de busqueda
        for job in lt.iterator(country): #? O(M) siendo M la cantidad de ofertas de empleo que cumplen con los criterios de busqueda
            add_job_to_level_map(data_structs, job, level_map)
    
    levels = obtain_table_levels(data_structs, level_map) #? O N * (MlogM) siendo N la cantidad de niveles de experticia y M la cantidad de datos relevantes 
    return amount_offers, amount_cities, best_country, best_city, levels

def obtain_table_levels(control, level_map):
    list_levels = mp.valueSet(level_map)
    levels = []
    for level in lt.iterator(list_levels):
        table_level = create_table_level(control, level)
        levels.append(table_level)    
    
    return levels
def create_table_level(control, level_map):
    
    level, amount_offers, amount_abilities, best_ability, worst_ability, average_level_skills, amount_companies, best_company, worst_company = obtain_data_by_level(control, level_map)

    table_level = [level, amount_offers, amount_abilities, best_ability, worst_ability, average_level_skills, amount_companies, best_company, worst_company]
    
    return table_level
def obtain_data_by_level(control, level_map):
    level = mp.get(level_map, 'level')['value']
    amount_offers = lt.size(mp.get(level_map, 'jobs')['value'])
    map_abilities = mp.get(level_map, 'map_skills')['value']
    amount_abilities, best_ability, worst_ability = obtain_best_and_worst_ability(map_abilities) #? O(JlogJ) siendo K la cantidad de habilidades 
    average_level_skills = mp.get(level_map, 'average_level_skills')['value']
    amount_skills = mp.get(level_map, 'amount_skills')['value']
    counter_skills = mp.get(level_map, 'counter_skills')['value']
    average_level_skills = round((counter_skills / amount_skills), 2)
    mp.put(level_map, 'average_level_skills', average_level_skills)
    map_companies = mp.get(level_map, 'map_companies')['value']
    amount_companies, best_company, worst_company = obtain_best_and_worst_companies(map_companies) #? O(UlogU) siendo U la cantidad de compañias
    
    return level, amount_offers, amount_abilities, best_ability, worst_ability, average_level_skills, amount_companies, best_company, worst_company
def obtain_best_and_worst_ability(map_abilities):
    list_abilities = mp.valueSet(map_abilities)
    merg.sort(list_abilities, sort_abilities_by_amount_jobs)
    best_ability = lt.firstElement(list_abilities)
    best_ability = {'Habilidad': lt.firstElement(best_ability)['skills'], 'Cantidad de ofertas': lt.size(best_ability)}
    worst_ability = lt.lastElement(list_abilities)
    worst_ability = {'Habilidad': lt.firstElement(worst_ability)['skills'], 'Cantidad de ofertas': lt.size(worst_ability)}
    return lt.size(list_abilities), best_ability, worst_ability
def obtain_best_and_worst_companies(map_companies):
    list_companies = mp.valueSet(map_companies)
    merg.sort(list_companies, sort_companies_by_amount_jobs)
    best_company = lt.firstElement(list_companies)
    best_company = {'Compañia': lt.firstElement(best_company)['company_name'], 'Cantidad de ofertas': lt.size(best_company)}
    worst_company = lt.lastElement(list_companies)
    worst_company = {'Compañia': lt.firstElement(worst_company)['company_name'], 'Cantidad de ofertas': lt.size(worst_company)}
    return lt.size(list_companies), best_company, worst_company
def obtain_best_country(filter_countries):
    merg.sort(filter_countries, sort_countries_by_amount_jobs) # Ordena los paises por la cantidad de ofertas
    best_country = lt.firstElement(filter_countries) # Saca el pais con la mayor cantidad de ofertas
    best_country = {'Pais': lt.firstElement(best_country)['country_code'], 'Cantidad de ofertas': lt.size(best_country)} # Crea un diccionario con la informacion del pais
    return best_country
def obtain_best_city(cities_map):
    list_cities = mp.valueSet(cities_map)
    merg.sort(list_cities, sort_cities_by_amount_jobs) # Ordena las ciudades por la cantidad de ofertas
    best_city = lt.firstElement(list_cities) # Saca la ciudad con la mayor cantidad de ofertas
    best_city = {'Ciudad': lt.firstElement(best_city)['city'], 'Cantidad de ofertas': lt.size(best_city)} # Crea un diccionario con la informacion de la ciudad
    return best_city
def add_job_to_cities_map(job, cities_map):
    """
    Función que agrega un trabajo a un mapa de ciudades
    """
    city = job['city'] # Extrae la ciudad del trabajo
    if mp.contains(cities_map, city): # Si la ciudad ya esta en el mapa
        city_info = mp.get(cities_map, city) # Saca la informacion de la ciudad
        city_jobs = city_info['value'] # Saca los trabajos de la ciudad
        lt.addLast(city_jobs, job) # Agrega el trabajo a la lista de trabajos
    else: # Si la ciudad no esta en el mapa
        city_jobs = lt.newList('ARRAY_LIST') # Crea una nueva lista de trabajos
        lt.addLast(city_jobs, job) # Agrega el trabajo a la lista de trabajos
        mp.put(cities_map, city, city_jobs) # Agrega la lista de trabajos al mapa de ciudades
def add_job_to_level_map(control, job, level_map):
    
    job_level = job['experience_level'] # Cual es el nivel de experiencia del trabajo
    if mp.contains(level_map, job_level): # SI ese nivel de experiencia ya esta en el mapa
        level_info = mp.get(level_map, job_level)
        level_info = level_info['value']
        update_info_level(control, level_info, job)
    else:
        level_entry = create_level_entry(job_level)
        mp.put(level_map, job_level, level_entry)
        update_info_level(control, level_entry, job)
def update_info_level(control, level_map, job):
    #Agrego el trabajo a la lista de trabajos
    list_jobs = mp.get(level_map, 'jobs')['value']
    lt.addLast(list_jobs, job)
    
    
    #Agrego el trabajo a el mapa de skills
    skill_info = search_skill(control, job)
    add_job_to_skills_map(control, skill_info, job, level_map)

    #Agrego el trabajo al mapa de compañias
    add_job_to_companies_map(control, job, level_map)   
def create_level_entry(level):
    """
    Función que crea una entrada de nivel
    """
    level_info = mp.newMap(7, maptype='PROBING', loadfactor=0.5)
    
    mp.put(level_info, 'level', level) # Nivel de Experiencia
    mp.put(level_info, 'jobs', lt.newList('ARRAY_LIST')) #Una lista con los trabajos
    mp.put(level_info, 'map_skills', mp.newMap(1000, maptype='PROBING', loadfactor=0.5)) # Un mapa con las habilidades
    mp.put(level_info, 'amount_skills', 0) # Cantidad de habilidades
    mp.put(level_info, 'counter_skills', 0) # Contador de habilidades
    mp.put(level_info, 'average_level_skills', 0) # Promedio de habilidades
    mp.put(level_info, 'map_companies', mp.newMap(1000, maptype='PROBING', loadfactor=0.5)) # Un mapa con las compañias
    
    return level_info   
def examine_job_by_date(job, year, month):
    """
    Función que examina un trabajo
    """
    year = datetime.datetime.strptime(year, '%Y')
    month = datetime.datetime.strptime(month, '%m')
    date_job = job['published_at']
    date_job = datetime.datetime.strptime(date_job, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    if date_job.year == year.year and date_job.month == month.month:
        return job
    else:
        return None  
def search_skill(control, job):
    skills_map = control['skills']
    id = job['id']
    
    if mp.contains(skills_map, id):
        job_skills = mp.get(skills_map, id)
        job['skills'] = job_skills['value']['name']
        return job_skills['value']
    else:
        return false   
def add_job_to_skills_map(control, skill_info ,job, level_map):
    
    skills_map = mp.get(level_map, 'map_skills')['value']
    skill_name = skill_info['name']
    skill_level = skill_info['level']
    
    if mp.contains(skills_map, skill_name):
        skill_entry = mp.get(skills_map, skill_name)
        skill_jobs = skill_entry['value']
        lt.addLast(skill_jobs, job)
    else:
        skill_jobs = lt.newList('ARRAY_LIST')
        lt.addLast(skill_jobs, job)
        mp.put(skills_map, skill_name, skill_jobs)
    
    amount_skills = mp.get(level_map, 'amount_skills')['value']
    amount_skills += 1
    mp.put(level_map, 'amount_skills', amount_skills)
    counter_skills = mp.get(level_map, 'counter_skills')['value']
    counter_skills += int(skill_level)
    mp.put(level_map, 'counter_skills', counter_skills)
    
    return control   
def add_job_to_companies_map(control, job, level_map):
        
    companies_map = mp.get(level_map, 'map_companies')['value']
    company_name = job['company_name']
    
    if mp.contains(companies_map, company_name):
        company_entry = mp.get(companies_map, company_name)
        company_jobs = company_entry['value']
        lt.addLast(company_jobs, job)
    else:
        company_jobs = lt.newList('ARRAY_LIST')
        lt.addLast(company_jobs, job)
        mp.put(companies_map, company_name, company_jobs)
    
    return control
def sort_countries_by_amount_jobs(country1, country2):
    
    country1_jobs = lt.size(country1)
    country2_jobs = lt.size(country2)
    country1_name = lt.firstElement(country1)['country_code']
    country2_name = lt.firstElement(country2)['country_code']
    
    
    if country1_jobs == country2_jobs:
        return  country1_name < country2_name
    else:
        return country1_jobs > country2_jobs   
def sort_cities_by_amount_jobs(city1, city2):
    
    city1_jobs = lt.size(city1)
    city2_jobs = lt.size(city2)
    city1_name = lt.firstElement(city1)['city']
    city2_name = lt.firstElement(city2)['city']
    
    if city1_jobs == city2_jobs:
        return  city1_name < city2_name
    else:
        return city1_jobs > city2_jobs 
def sort_abilities_by_amount_jobs(ability1, ability2):
    ability1_jobs = lt.size(ability1)
    ability2_jobs = lt.size(ability2)
    return ability1_jobs > ability2_jobs
def sort_companies_by_amount_jobs(company1, company2):
    company1_jobs = lt.size(company1)
    company2_jobs = lt.size(company2)
    company1_name = lt.firstElement(company1)['company_name']
    company2_name = lt.firstElement(company2)['company_name']
    if company1_jobs == company2_jobs:
        return  company1_name < company2_name
    else:
        return company1_jobs > company2_jobs
#! =======================================================================================
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
