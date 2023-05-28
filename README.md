# Sistema de Respuesta de Voz Interactivo (IVR) - Guía de Instalación y Ejecución Local

Este repositorio contiene un sistema de respuesta de voz interactivo (IVR) desarrollado con Django, SQLite y TailwindCSS. Para correrlo localmente en tu computadora, podés seguir los siguientes pasos:

## Requisitos previos
- Python (versión 3.6 o superior)
- Pip (sistema de gestión de paquetes de Python)

## Pasos para ejecutar localmente

1. Clonar el repositorio:

```bash
git clone https://github.com/TomiMalamud/django-dsi-utn.git
```

2. Te va a preguntar el nombre del directorio donde querés clonar el repositorio. Ingresá el nombre que quieras y después ingresá así:

```bash
cd nombre-del-repo
```

3. Iniciá el entorno virtual: (también se puede por GUI en VSCode con Ctrl+Shift+P y escribiendo Python: Create Virtual Environment)

```bash
python3 -m venv .venv
```

4. Activá el entorno virtual: (por GUI se activa automáticamente)

En Windows:
```bash
env\Scripts\activate
```

En Linux o macOS:
```bash
source env/bin/activate
```

5. Instalá las dependencias: (también se instalan solas por GUI)

```bash
pip install -r requirements.txt
```

6. Para que la base de datos funcione, tenés que hacer las migraciones:

```bash
python manage.py migrate
```

7. Instalá las dependencias de Tailwind:

```bash
python manage.py tailwind install
```

```bash
python manage.py tailwind start
```

8. Iniciá el servidor:

```bash
python manage.py runserver
```

9. Dentro de la respuesta de la terminal, deberías ver el link del servidor:


```
http://localhost:8000 o http://127.0.0.1:8000/
```

Haciendo click en el link deberías ver esta pantalla: 