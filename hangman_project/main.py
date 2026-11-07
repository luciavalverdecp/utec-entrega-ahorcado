from utils import get_random_word
from game import HangmanGame


word = get_random_word()
game = HangmanGame(word)

while True:
    #fallos = []
    letter = input("Ingresá una letra: ").lower().strip()

    try:
        if len(letter) != 1:
            raise ValueError ("La entrada debe tener una letra")
        
        if not letter.isalpha():
            raise ValueError( "La entrada debe ser una letra, no numeros ni caracteres especiales")
                
        if letter in game.guessed_letters:
            raise ValueError("Ya usaste esa letra.")

        if game.process_guess(letter):
            print("¡Bien! Esa letra está en la frase.")
        else:
            #fallos.append(letter)
            print("Esa letra no está en la frase.")

        game.display_progress()
        print("Letras incorrectas: ", game.display_wrong_letters())
        break

    except ValueError as e:    
        print(e)

    






    

