#Archivo Game

class HangmanGame:
    
    def __init__(self, word):
        """ Inicializa el juego """
        self.word = word
        self.guessed_letters = []
        self.wrong_letters = []
        self.max_errors = 6 
        self.errors = 0

    def display_progress(self):
        """Devuelve la frase con las letras adivinadas y '_' en las que faltan."""

        texto = ""
        for letra in self.word:
            if letra in self.guessed_letters:
                texto = texto+letra + " "
            else:
                texto = texto + "_"
        print(texto)


    def process_guess(self, letter):
        """ procesa la letra que le ingresas """
        letter = letter.lower()

        if letter in self.guessed_letters:
            return None

        self.guessed_letters.append(letter)
        
        if letter in self.word:
            return True
        
        self.errors += 1
        self.wrong_letters.append(letter)
        return False


    def display_wrong_letters(self):
        """Devuelve las letras erradas de las ingresadas."""

        texto = ""
        for letra in self.wrong_letters:
            texto = texto + letra + " "
        return texto.strip()