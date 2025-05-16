import math
import config
from processing.objeto import Particula  

# Función para simular gravedad
def aplicar_gravedad(particulas):
    for i, a in enumerate(particulas):
        for j, b in enumerate(particulas):
            if i == j:
                continue
            dx = b.x - a.x
            dy = b.y - a.y
            distancia = math.hypot(dx, dy)
            if distancia == 0:
                continue
            fuerza = config.G * a.masa * b.masa / distancia**2
            ax = fuerza * dx / distancia / a.masa
            ay = fuerza * dy / distancia / a.masa
            a.vx += ax
            a.vy += ay

# Función para fusionar partículas cercanas
def fusionar(particulas):
    nuevas = []
    skip = set()
    for i in range(len(particulas)):
        if i in skip:
            continue
        a = particulas[i]
        for j in range(i + 1, len(particulas)):
            if j in skip:
                continue
            b = particulas[j]
            dx = b.x - a.x
            dy = b.y - a.y
            distancia = math.hypot(dx, dy)
            if distancia < config.FUSION_DIST:
                # Fusionar: la nueva masa es la suma de las masas de las dos partículas
                nueva_masa = a.masa + b.masa
                nueva_x = (a.x * a.masa + b.x * b.masa) / nueva_masa
                nueva_y = (a.y * a.masa + b.y * b.masa) / nueva_masa
                nueva_vx = (a.vx * a.masa + b.vx * b.masa) / nueva_masa
                nueva_vy = (a.vy * a.masa + b.vy * b.masa) / nueva_masa
                nuevas.append(Particula(nueva_x, nueva_y, nueva_masa, nueva_vx, nueva_vy))
                skip.add(i)
                skip.add(j)
                break
        else:
            nuevas.append(a)
    return nuevas

