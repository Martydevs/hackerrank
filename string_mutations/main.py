# Ejercicio Hackerrank | Mutar un caracter especifico mediante el indice de la cadena
def mutate_string(string: str, pos: int, char: str):
    secuence = string
    final_pos = pos + 1
    result = secuence[:pos] + char + secuence[final_pos:]

    return result

if __name__ == '__main__':
    string = "abracadabra"
    pos = 5
    char = "k"
    print(mutate_string(string, pos, char))
 