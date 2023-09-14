# Sistema de Respuesta de Voz Interactivo (IVR) - Guía de Instalación y Ejecución Local

Este repositorio contiene un sistema de respuesta de voz interactivo (IVR) desarrollado con Python. Para correrlo localmente hay que seguir los siguientes pasos.

## Requisitos previos
- Python
- pip (sistema de gestión de paquetes de Python)
- VSCode y GIT.

## Pasos para ejecutar localmente

Estos pasos funcionan usando VSCode. También se puede hacer por comandos. 

1. Con VSCode abierto, abrir Source Control (Ctrl+Shift+G) y clonar el repositorio

2. Iniciar el entorno virtual con (Ctrl+Shift+P) escribiendo "Python: Create Virtual Environment" o "Python: Crear ambiente virtual".

3. Instalar las dependencias seleccionando requirements.txt en el proceso de creación del entorno virtual. Si ya se creó el entorno y no se hizo, hay que correr el siguiente comando:
 
```bash
pip install -r requirements.txt
```

4. Con (Ctrl+R) se corre el programa, desde `logica_negocio.py`.