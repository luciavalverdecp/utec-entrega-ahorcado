import random

def get_random_word():
    """Lee el archivo y devuelve una palabra válida random."""
    with open("wordlist.txt", "r", encoding="utf-8") as archivo:
        palabras = []
        for linea in archivo:
            """se encarga de eliminar especios a la izquierda y derecha, para luego convertir su contenido en minuscula."""
            linea = linea.strip().lower()
            """Agrega la línea solo si no está vacía y, ignorando los espacios, contiene únicamente letras (descarta números, símbolos, etc.)"""
            if linea and linea.replace(" ", "").isalpha():
                palabras.append(linea)

    return random.choice(palabras)