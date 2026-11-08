<div align="center">

# Juego del Ahorcado

**Adiviná la frase oculta, letra por letra, antes de quedarte sin intentos.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Dependencias](https://img.shields.io/badge/dependencias-ninguna-success)
![Interfaz](https://img.shields.io/badge/interfaz-terminal-black)
![Estado](https://img.shields.io/badge/estado-en%20desarrollo-orange)

</div>

---

## Descripción

Ahorcado para la terminal escrito en Python. El juego elige al azar una frase (por ejemplo, el título de una película) desde `wordlist.txt` y el jugador tiene que descubrirla escribiendo **una letra por turno**, con un máximo de **6 errores**.

Proyecto de práctica para aplicar estructuras de control, funciones, estructuras de datos, programación orientada a objetos, módulos y manejo de archivos.

## Tabla de contenidos

- [Inicio rápido](#inicio-rápido)
- [Reglas](#reglas)
- [Ejemplo de partida](#ejemplo-de-partida)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Cómo funciona](#cómo-funciona)
- [Personalizar las frases](#personalizar-las-frases)
- [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
- [Autores](#autores)

---

## Inicio rápido

**Requisitos:** Python 3.8 o superior. No hace falta instalar nada, solo se usa la biblioteca estándar.

```bash
# 1. Clonar o descargar el proyecto
cd hangman_project

# 2. Ejecutar
python3 main.py      # Linux / macOS
python main.py       # Windows (si no funciona, probá: py main.py)
```

Para verificar tu versión de Python:

```bash
python --version
```

## Reglas

| Situación | Resultado |
|---|---|
| La letra está en la frase | Se revela en todas sus posiciones |
| La letra **no** está en la frase | Suma 1 error |
| Letra repetida | Se avisa, **no** cuenta como error |
| Número, símbolo o más de un carácter | Se rechaza, **sin** penalizar |
| Espacios y guiones | Se muestran automáticamente |
| Llegás a **6 errores** | Perdés |
| Descubrís toda la frase | Ganás |

Después de cada intento se muestran la frase actual, las letras adivinadas, las incorrectas y el contador de errores.

## Ejemplo de partida

```text
Frase: _ _   _ _ _
Letras adivinadas:
Letras incorrectas:
Errores: 0/6

Ingresá una letra: e

¡Bien! Esa letra está en la frase.
Frase: e _   _ e _
Letras adivinadas: e
Letras incorrectas:
Errores: 0/6

...

¡Felicidades, ganaste! La frase era: el rey
```

> El ejemplo es ilustrativo; el formato exacto de la salida puede variar.

## Estructura del proyecto

```text
hangman_project/
├── main.py         # Bucle principal del juego
├── game.py         # Clase HangmanGame (lógica)
├── utils.py        # Carga de frases desde el archivo
├── wordlist.txt    # Frases posibles, una por línea
└── README.md
```

## Cómo funciona

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Pide letras al jugador, valida la entrada (una sola letra, solo alfabética, no repetida), limpia la pantalla entre turnos y anuncia el resultado. |
| `game.py` | Clase `HangmanGame`: guarda la frase, las letras acertadas y falladas y los errores; procesa cada intento; arma la frase visible; determina si se ganó o se perdió. |
| `utils.py` | `get_random_word()`: lee `wordlist.txt`, ignora líneas vacías y devuelve una frase al azar en minúsculas. |
| `wordlist.txt` | Banco de frases. |

## Personalizar las frases

Editá `wordlist.txt` y agregá una frase por línea:

```text
el rey leon
toy story
volver al futuro
```

Recomendaciones:

- Usá minúsculas y, de ser posible, **sin tildes ni ñ**, para que el jugador no tenga que adivinar caracteres especiales.
- No dejes comentarios en el archivo (las líneas vacías se ignoran automáticamente).

## Objetivos de aprendizaje

- Estructuras de control: condicionales y bucles
- Funciones y modularización del código
- Estructuras de datos: cadenas y listas
- Programación orientada a objetos: clases y objetos
- Módulos e imports
- Lectura de archivos de texto y entrada del usuario
- Validación de entradas y manejo de excepciones
- Buenas prácticas de estilo (PEP 8)

## Autores

Gianella Meringolo · Joaquín Vila · Lucía Valverde

Proyecto realizado como parte del curso en **UTEC**.
