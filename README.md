# Instalar uv (solo una vez)
pip install uv

# Crear entorno virtual
uv init

# Instalar dependencias del proyecto
uv sync 

# Instalar depedencias
uv add dependencia

# Comando para poder usar el .env
$env:UV_ENV_FILE = ".env"