"""
Ejercicio Ciclo
i = 0

n = int(input())

Ciclo while que itera de 0 a la entrada
while i < n:

    numeros que sean menor a la entrada
    se exponenciará al cuadrado
    if i < n:
        print(i ** 2)
    i += 1
"""

""" 
# Evaluar si un año es bisiesto o no

def is_leap(year):
    if ((year % 4 == 0) 
        and (year % 100 != 0 or year % 400 == 0)):
        leap = True
        return leap
    else:
        leap = False
        return leap

year = int(input())
print(is_leap(year)) """

""" 
# Mostrar una lista de numeros enteros del 1 hasta n, juntarlos sin metodos de cadenas

i = 0
n = 5

while i < n:
    str(print(i + 1, end = '')) # end = '' para que no salte de linea
    i += 1 """

# Ejercicio HackerRank

"""
Dada la hoja de puntuaciones de los participantes en el Día del Deporte de su Universidad, 
se le pide que encuentre la puntuación del subcampeón. Se te dan n puntuaciones. 

Guárdalas en una lista y averigua la puntuación del subcampeón.

n = total de elementos de la lista a guardar

2 <= n <= 10
-100 <= lista <= 100

"""

def second_highest(secuence: list, n):
    i = 0
    secuence.sort()
    secuence_set = set(secuence)
    secuence = list(secuence_set)
    
    if (n >= 2 and n <= 10) and (secuence[i] >= -100 and secuence[i] <= 100):
        highest_score = max(secuence)
        secuence.remove(highest_score)

    return max(secuence)

n = 5
some_list = list(map(int, input().split(" ")))
print(second_highest(some_list, n))
