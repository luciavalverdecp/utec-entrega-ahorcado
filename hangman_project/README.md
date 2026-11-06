🎮 Juego del Ahorcado (Hangman) en consola

Juego del ahorcado hecho en Python que se juega completamente desde la terminal. El jugador debe adivinar una frase oculta (por ejemplo, el título de una película) escribiendo una letra por turno, con un máximo de 6 intentos incorrectos. Las frases se cargan de forma aleatoria desde un archivo de texto, por lo que cada partida es diferente.

Proyecto de práctica para aplicar estructuras de control, funciones, estructuras de datos, programación orientada a objetos, módulos y manejo de archivos.

📋 Tabla de contenidos
Reglas del juego
Estructura del proyecto
Requisitos
Cómo ejecutar
Cómo jugar
Formato de wordlist.txt
Descripción de los archivos
Objetivos de aprendizaje
Autor

🎯 Reglas del juego
El jugador adivina la frase oculta letra por letra.
Solo se aceptan letras como entrada válida (los números y símbolos se rechazan sin penalizar).
Cada intento incorrecto aumenta el contador de errores.
El jugador pierde al llegar a 6 errores.
El jugador gana si descubre todas las letras antes de llegar al límite.
Después de cada intento se muestran las letras ya usadas y el estado actual de la frase.
Los caracteres que no son letras (espacios, signos de puntuación) se revelan automáticamente.
Repetir una letra ya usada no cuenta como error.
📁 Estructura del proyecto
hangman_project/
│
├── main.py        # Bucle principal del juego
├── game.py        # Clase HangmanGame (lógica del juego)
├── utils.py       # Funciones auxiliares (validar entrada, mostrar estado, cargar frases)
├── wordlist.txt   # Lista de frases (una por línea)
└── README.md      # Instrucciones y descripción del juego
⚙️ Requisitos
Python 3.8 o superior.
No necesita instalar librerías externas: usa solo la biblioteca estándar de Python.

Para verificar tu versión de Python:

bash
python --version
▶️ Cómo ejecutar
Clona el repositorio o descarga la carpeta del proyecto.
Entra a la carpeta:
bash
   cd hangman_project
Ejecuta el juego: Windows (PowerShell o CMD):
powershell
   python main.py

Linux / macOS:

bash
   python3 main.py

Si python no se reconoce en Windows, prueba con py main.py.

🕹️ Cómo jugar
Al iniciar, el juego elige una frase al azar de wordlist.txt y la muestra oculta con guiones bajos.
En cada turno, escribe una letra y presiona Enter.
Si la letra está en la frase, se revela en todas sus posiciones.
Si no está, suma un error. Tienes hasta 6 errores.
La partida termina cuando completas la frase (ganas) o llegas a 6 errores (pierdes).
Ejemplo de partida
=== JUEGO DEL AHORCADO ===

Frase:  _ _   _ _ _
Letras usadas: (ninguna)
Errores: 0/6

Ingresa una letra: o

Frase:  _ _   _ _ _
Letras usadas: o
Errores: 1/6

Ingresa una letra: e

Frase:  e _   _ e _
Letras usadas: e, o
Errores: 1/6

...

¡Felicidades, ganaste! La frase era: el rey

El ejemplo es ilustrativo; el formato exacto de salida puede variar según tu implementación.

📝 Formato de wordlist.txt
Una frase por línea.
En minúsculas y, preferentemente, sin tildes ni ñ para que el jugador no tenga que adivinar caracteres especiales.
Sin líneas vacías ni comentarios.
El programa limpia los espacios sobrantes con strip() al leer cada línea.

Ejemplo:

el rey leon
toy story
volver al futuro
el padrino
buscando a nemo
titanic
matrix
jurassic park
la bella y la bestia
el hobbit

Puedes agregar tus propias frases abriendo el archivo y escribiendo una nueva por línea. Para editarlo en Windows:

powershell
notepad wordlist.txt
🧩 Descripción de los archivos
main.py

Punto de entrada del programa. Contiene el bucle principal del juego: carga las frases, crea la partida, pide letras al jugador, muestra el estado después de cada intento y anuncia el resultado final. También permite jugar otra partida al terminar.

game.py

Contiene la clase HangmanGame, que encapsula toda la lógica del juego:

Guarda la frase secreta, las letras adivinadas, las letras falladas y el contador de errores.
Procesa cada intento del jugador (acierto, error o letra repetida).
Construye el estado visible de la frase (letras reveladas y guiones bajos).
Determina si el jugador ganó o perdió.
utils.py

Funciones auxiliares que mantienen main.py y game.py limpios:

Cargar frases desde wordlist.txt (ignorando líneas vacías).
Validar la entrada del usuario (una sola letra, solo caracteres alfabéticos).
Mostrar el estado actual de la partida en pantalla.
wordlist.txt

Archivo de texto con las frases posibles, una por línea.

📚 Objetivos de aprendizaje

Con este proyecto se practica:

Estructuras de control: condicionales y bucles para manejar el flujo del juego.
Funciones: encapsular y estructurar la lógica.
Estructuras de datos: cadenas, listas, conjuntos y diccionarios.
Programación orientada a objetos: clases, objetos y herencia.
Módulos e imports: separar el código en varios archivos.
Entrada/salida: lectura de datos del usuario y de archivos de texto.
Validación de entrada desde la línea de comandos.
Depuración básica y resolución de problemas.
Buenas prácticas de estilo siguiendo la guía PEP 8.
👤 Autor

Gianella Meringolo, Joaquin Vila y Lucia Valverde — Proyecto realizado como parte del curso en UTEC.