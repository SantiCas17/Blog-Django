# MiBlog - Proyecto Final Coderhouse

Este es el proyecto final del curso de Python en Coderhouse. Consiste en un blog web completamente funcional con sistema de usuarios, creación de contenido, y panel de administración, utilizando el patrón MVT. Lo pueden ver en este link https://santiagocastillo.pythonanywhere.com/

##  Características principales
* **Autenticación:** Registro de nuevos usuarios, Login y Logout.
* **Perfiles:** Vista protegida para edición de datos personales (Nombre, Apellido, Email).
* **CRUD Completo:** Creación, Lectura, Actualización y Eliminación de posteos.
* **Seguridad y Permisos:** Únicamente el autor original de un posteo tiene permisos para editarlo o borrarlo.
* **Manejo de Archivos:** Soporte para carga de imágenes mediante `ImageField` y renderizado en plantillas.
* **Interfaz de Usuario:** Diseño responsivo, moderno y armónico utilizando Bootstrap  y Template Inheritance.

##  Tecnologías utilizadas
* Python 
* Django
* SQLite (Base de datos local)
* Pillow (Para el procesamiento de imágenes)
* Bootstrap (Vía CDN)
* HTML / CSS

## Instalación y Uso Local

Para correr este proyecto en tu computadora, sigue estos pasos:

1. Clona o descarga este repositorio.
2. Abre una terminal en la carpeta del proyecto y crea un entorno virtual:
   `python -m venv .venv`
3. Activa el entorno virtual:
   * Windows: `.venv\Scripts\activate`
   * Mac/Linux: `source .venv/bin/activate`
4. Instala las dependencias necesarias:
   `pip install -r requirements.txt`
5. Ejecuta las migraciones de la base de datos:
   `python manage.py migrate`
6. Inicia el servidor de desarrollo:
   `python manage.py runserver`
7. Ingresa a `http://127.0.0.1:8000/` en tu navegador web.

---
*Desarrollado por Santiago Ezequiel Castillo.*
