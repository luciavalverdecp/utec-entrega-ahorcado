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

        texto = "Frase: "
        for letra in self.word:
            if letra in self.guessed_letters:
                texto = texto+letra + " "
            else:
                texto = texto + "_"
        print(texto)


    def process_guess(self, letter):
        """ Procesa la letra ingresada y devuelve si fue correcta """
        letter = letter.lower()

        if letter in self.guessed_letters or letter in self.wrong_letters:
            return None

        #self.guessed_letters.append(letter) acá esta guardando todas las letras no solo las letras correctas.
        
        if letter in self.word:
            self.guessed_letters.append(letter)
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

    def display_guessed_letters(self):
            """Devuelve las letras adivinadas de las ingresadas."""
    
            texto = ""
            for letra in self.guessed_letters:
                texto = texto + letra + " "
            return texto.strip()

    def is_won(self):
        
        for letra in self.word:
            if letra not in self.guessed_letters:
             return False

        return True

    def is_lost(self):
        """Devuelve True si se alcanzó la cantidad máxima de errores."""
        if self.errors >= self.max_errors:
            return True
        else:
            return False
        

