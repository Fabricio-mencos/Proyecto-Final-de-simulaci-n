import unittest
from processing.simulacion import aplicar_gravedad, fusionar
from processing.objeto import Particula
from processing.distribuciones import Generador
import config
import pygame

class TestGenerador(unittest.TestCase):

    def test_generar_masa_aleatoria(self):
        # Ejecutamos la función varias veces para comprobar que el valor cae en un rango razonable
        for _ in range(100):  # Probar varias veces para obtener una muestra
            masa = Generador.generar_masa_aleatoria()

            # Verificamos que la masa está en un rango razonable alrededor de la media (MASA_MEDIA)
            self.assertGreater(masa, 0)  # Masa no puede ser negativa
            self.assertTrue(masa <= config.MASA_MEDIA + 3 * config.MASA_DESVIACION)

    def test_generar_posicion_uniforme(self):
        # Probamos que las posiciones generadas están dentro de los límites del área
        for _ in range(100):  # Probar varias veces para obtener una muestra
            x, y = Generador.generar_posicion_uniforme(500, 500)

            # Verificamos que la posición esté dentro del rango esperado (con margen)
            self.assertGreaterEqual(x, 100)
            self.assertLessEqual(x, 500 - 100)
            self.assertGreaterEqual(y, 100)
            self.assertLessEqual(y, 500 - 100)



class TestParticula(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.pantalla = pygame.Surface((config.WIDTH, config.HEIGHT))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_rebote_bordes(self):
        p = Particula(1, 1, 10, -5, -5)
        p.actualizar_pos()
        self.assertGreaterEqual(p.x, p.radio)
        self.assertGreaterEqual(p.y, p.radio)
        self.assertGreaterEqual(p.vx, 0)
        self.assertGreaterEqual(p.vy, 0)

if __name__ == '__main__':
    unittest.main()