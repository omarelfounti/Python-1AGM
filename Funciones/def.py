import random  # Importa la librería random para generar números aleatorios

# Lista de frases motivacionales o de fortuna
opciones = [
    'No persigas la felicidad, créala.',
    'Todas las cosas son difíciles antes de ser fáciles.',
    'El madrugador atrapa el gusano, pero el segundo ratón se lleva el queso.',
    'Si comes algo y nadie te ve comerlo, no tiene calorías.',
    'Alguien en tu vida necesita una carta tuya.',
    'No solo pienses. ¡Actúa!',
    'Tu corazón latirá más rápido.',
    'La fortuna que buscas está en otra galleta.',
    '¡Ayuda! Estoy siendo prisionero en una panadería china.'
]

# Definición de la función que selecciona una frase al azar
def fortuna():
    fortuna_aleatoria = random.randint(0, len(opciones) - 1)  # Genera un número aleatorio dentro del rango de la lista
    print(opciones[fortuna_aleatoria])  # Muestra la frase correspondiente al número generado

# Llamadas a la función para mostrar tres frases aleatorias
fortuna()
fortuna()
fortuna()

