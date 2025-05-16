import pygame
import random
import math
import config

class Particula:
    def __init__(self, x, y, masa, vx, vy, color=None, forma=None):
        self.x = x
        self.y = y
        self.masa = masa
        self.vx = vx
        self.vy = vy
        self.color = color if color else generar_color_aleatorio()
        self.forma = forma if forma else random.choice(["circulo", "cuadrado", "triangulo"])
        self.radio = int(max(2, self.masa * config.RADIO_ESCALA))

    def actualizar_pos(self):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radio < 0:
            self.x = self.radio
            self.vx *= -1
        elif self.x + self.radio > config.WIDTH:
            self.x = config.WIDTH - self.radio
            self.vx *= -1

        if self.y - self.radio < 0:
            self.y = self.radio
            self.vy *= -1
        elif self.y + self.radio > config.HEIGHT:
            self.y = config.HEIGHT - self.radio
            self.vy *= -1

    def dibujar(self, pantalla):
        if self.forma == "circulo":
            pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), self.radio)
        elif self.forma == "cuadrado":
            lado = self.radio * 2
            pygame.draw.rect(pantalla, self.color, pygame.Rect(self.x - self.radio, self.y - self.radio, lado, lado))
        elif self.forma == "triangulo":
            h = math.sqrt(3) * self.radio
            puntos = [
                (self.x, self.y - h / 2),
                (self.x - self.radio, self.y + h / 2),
                (self.x + self.radio, self.y + h / 2)
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)

def generar_color_aleatorio():
    return (
        random.randint(config.COLOR_MIN[0], config.COLOR_MAX[0]),
        random.randint(config.COLOR_MIN[1], config.COLOR_MAX[1]),
        random.randint(config.COLOR_MIN[2], config.COLOR_MAX[2])
    )
