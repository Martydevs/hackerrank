# Ejercicio El Segundo Mayor | HackerRank

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

if __name__ == '__main__':
    n = 5
    some_list = list(map(int, input().split(" ")))
    print(second_highest(some_list, n))