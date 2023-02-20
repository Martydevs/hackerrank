# Ejercicio Hackkerank: Evaluar valores de cadena si son menores o iguales a 10 caracteres
# y unirlos en una cadena de salida.
def print_full_name(first: str, last: str):
    if len(first) <= 10 and len(last) <= 10:
        return f'Hello {first} {last}! You just delved into python.'
    else:
        raise ValueError("Both values are higher than 10 characters.")

first = input()
last = input()
print(print_full_name(first, last))