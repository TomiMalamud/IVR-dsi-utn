# Sistema de Respuesta de Voz Interactivo (IVR) - Guía de Instalación y Ejecución Local

Este repositorio contiene un sistema de respuesta de voz interactivo (IVR) desarrollado con Django, SQLite y TailwindCSS. Para correrlo localmente en tu computadora, podés seguir los siguientes pasos:

## Requisitos previos
- Python
- pip (sistema de gestión de paquetes de Python)
- VSCode y GIT.

## Pasos para ejecutar localmente

Estos pasos funcionan usando VSCode. También se puede hacer por comandos. 

1. Con VSCode abierto, abrí Source Control (Ctrl+Shift+G) y cloná el repositorio

2. Iniciá el entorno virtual con Ctrl+Shift+P y escribiendo "Python: Create Virtual Environment"

3. Instalá las dependencias seleccionando requirements.txt en el proceso de creación del entorno virtual. Si ya creaste el entorno y no lo hiciste, podés correr el siguiente comando:
 
```bash
pip install -r requirements.txt
```

4. Con este comando inicializás la base de datos:

```bash
python manage.py migrate
```

5. Iniciá el servidor:

```bash
python manage.py runserver
```

6. Dentro de la respuesta de la terminal, deberías ver el link del servidor:
```bash
http://localhost:8000 o http://127.0.0.1:8000/
```