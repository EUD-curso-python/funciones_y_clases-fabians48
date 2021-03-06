global1 = 34

def cambiar_global(var1):
    '''Cambiar una variable global
    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1 = var1
#    print(var1)
    return global1
    pass
#cambiar_global(5)

def anio_bisiesto(anio):
    '''Responder si el entero pasado como argumento es un año bisiesto

    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    if anio%4 == 0:
      if anio%100 == 0:
        if anio%400 == 0:
          return True
        else:
          return False
      else:
        return True
    else:
      return False

    pass

def contar_valles(lista):
    '''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    cont = 0
    temp = False
    cont2 = 0
    cont3 = 0
    longitud = len(lista)
    for i in lista:
      cont3 += 1
      if i == -1:
        cont2=cont3
        temp = False
        while temp == False:
          if cont2 < longitud:
            if lista[cont2]==1:
              cont += 1
              temp = True
            elif lista[cont2]==0:  
              cont2 += 1
              temp = False
            else:
              temp = True
          else:
            temp = True
    print(cont)
    return cont
    
    pass

#contar_valles([-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1])

def saltando_rocas(listarocas):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    
    #saltando_rocas = []
    #ll = [1,1,0,0]
    saltos =0
    cont = 0; #=c
    cont1 = 0 #i = 0; 
    longitud = len(listarocas) #l = len(ll)
    while cont1 < longitud-1:
      
      if cont1+2 < longitud and listarocas[cont1+2] == 0:
        cont += 1
        cont1 += 2 
      else: 
        cont += 1
        cont1 += 1
      saltos = cont
#      print(saltos)
    return(saltos)
saltando_rocas([1,1,0,0])


def pares_medias(listapares):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''

    pares= {}
    for i in listapares:
      if int(listapares.count(i)/2)!=0:
        pares[i]= int(listapares.count(i)/2)
    print(pares)
    return pares
    pass

#pares_medias([1,1,2,2,3,1])

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'

class ListaComa:
  
  
  def __init__(self, lista=[]):
    self.lista = lista
  def __str__(self):
    cadena=""
    for i in self.lista:
      if cadena == "":
        cadena = str(i)
      else:
        cadena = cadena + "," + str(i)
    return cadena
  

lis = ListaComa([1,2,3])
#print(lis)



# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'

class Persona:
  def __init__(self, nombres=[], apellidos=[]):
    self.nombres = nombres
    self.apellidos = apellidos

  def nombre_completo(self):
    cadena1=""
    cadena2=""
    cadena3=""
    for i in self.nombres:
      if cadena1 == "":
        cadena1 = str(i).capitalize()
      else:
        cadena1 = cadena1 + " " + str(i).capitalize()

    for j in self.apellidos:
      if cadena2 == "":
        cadena2 = str(j).capitalize()
      else:
        cadena2 = cadena2 + " " + str(j).capitalize()
    
    cadena3 = cadena1 + " " + cadena2
    return cadena3

nom = Persona(["fabian", "emilio"], ["solano", "aragon"])
#print(nom.nombre_completo())

# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.

import datetime
class Persona1(Persona):
  def __init__(self, nombres, apellidos, fecha_nacimiento):
    super().__init__(nombres,apellidos)
    self.fecha_nacimiento = fecha_nacimiento
  def edad(self):
    #fechaactual = datetime.datetime.now()
    #fecha_nacimiento = datetime.datetime.strptime("1985-10-21", "%Y-%m-%d")
    edad1 = datetime.datetime.now().year - self.fecha_nacimiento.year
    edad1 -= ((datetime.datetime.now().month, datetime.datetime.now().day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
    return(edad1)


fecha = datetime.datetime.strptime("1985-10-21", "%Y-%m-%d")
edd = Persona1(["fabian", "emilio"], ["solano", "aragon"], fecha)
#print(edd.edad())