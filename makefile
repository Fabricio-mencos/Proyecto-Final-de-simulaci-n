SHELL := cmd  # Para que sea compatible con Windows (cmd)

# Ruta al entorno virtual
VENV_DIR = .venv

# Comando para activar el entorno virtual en Windows
ACTIVATE = call .venv\Scripts\activate

# Comando para ejecutar el script de simulación
RUN_SIMULACION = python main.py  # Asumiendo que 'main.py' es el archivo principal

# Definir la regla para ejecutar todo el proceso
build: banner create install test typecheck run_simulacion

# Regla para mostrar el banner
banner:
	@echo "██████████   █████████  ███████████ ██████   ██████"
	@echo "░░███░░░░░█  ███░░░░░███░░███░░░░░░█░░██████ ██████ "
	@echo " ░███  █ ░  ███     ░░░  ░███   █ ░  ░███░█████░███ "
	@echo " ░██████   ░███          ░███████    ░███░░███ ░███ "
	@echo " ░███░░█   ░███          ░███░░░█    ░███ ░░░  ░███ "
	@echo " ░███ ░   █░░███     ███ ░███  ░     ░███      ░███ "
	@echo "██████████ ░░█████████  █████       █████     ██████"
	@echo "░░░░░░░░░░   ░░░░░░░░░  ░░░░░       ░░░░░     ░░░░░  "

# Crear el entorno virtual
create:
	python -m venv .venv

# Instalar dependencias
install:
	.venv\Scripts\pip install -r requirements.txt

# Ejecutar el script de simulación
run_simulacion:
	@echo "Ejecutando la simulación..."
	@$(ACTIVATE) && $(RUN_SIMULACION)

# Comprobaciones de tipo con mypy
typecheck:
	.venv\Scripts\mypy main.py
	.venv\Scripts\mypy processing/

# Realizar pruebas unitarias
test:
	.venv\Scripts\python -m unittest discover -s tests


build: banner create install test typecheck run
