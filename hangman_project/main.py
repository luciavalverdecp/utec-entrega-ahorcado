import os
from utils import get_random_word
from game import HangmanGame


word = get_random_word()
game = HangmanGame(word)

while True:
    """Dependiendo del dispositivo se elimina el contenido de la terminal"""
    letter = input("Ingresá una letra: ").lower().strip()
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y macOS
        os.system('clear')

    try:
        if len(letter) != 1:
            raise ValueError ("La entrada debe tener una letra")
        
        if not letter.isalpha():
            raise ValueError( "La entrada debe ser una letra, no numeros ni caracteres especiales")
                
        if letter in game.guessed_letters or letter in game.wrong_letters:
            raise ValueError("Ya usaste esa letra.")

        if game.process_guess(letter):
            print("¡Bien! Esa letra está en la frase.")
        else:
            #fallos.append(letter)
            print("Esa letra no está en la frase.")

        if game.is_won():
            print(f"¡Felicidades, ganaste! La frase era: {game.word}")    
            break
        
        if game.is_lost():
            print(f"Errores: {game.errors}/{game.max_errors}")
            print(f"¡Fin del juego.! La frase era: {game.word}")    
            break

        game.display_progress()
        print("Letras adivinadas: ", game.display_guessed_letters())
        print("Letras incorrectas: ", game.display_wrong_letters())
        print(f"Errores: {game.errors}/{game.max_errors}")

    except ValueError as e:    
        print(e)
        print("Letras adivinadas: ", game.display_guessed_letters())
        print("Letras incorrectas: ", game.display_wrong_letters())
        print(f"Errores: {game.errors}/{game.max_errors}")