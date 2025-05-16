import random
import config

class Generador:

    @staticmethod
    def generar_masa_aleatoria():
        return random.gauss(config.MASA_MEDIA, config.MASA_DESVIACION)

    @staticmethod
    def generar_posicion_uniforme(ancho, alto, margen=100):
        x = random.uniform(margen, ancho - margen)
        y = random.uniform(margen, alto - margen)
        return x, y

