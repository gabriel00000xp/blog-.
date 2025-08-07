# Django Blog Project

Este proyecto es una aplicación de blog básica construida con Django 5.2.4. Permite crear, listar y ver detalles de publicaciones. Es ideal como base para aprender Django y expandir funcionalidades.

## Estructura del Proyecto

```
django_base/
│
├── blog/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│
├── django_base/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/
│   ├── _base.html
│   ├── post_list.html
│   ├── post_detail.html
│   ├── post_new.html
│
├── static/
│   └── (archivos estáticos opcionales)
│
├── db.sqlite3
├── manage.py
```

## Instalación y Configuración

1. **Clona el repositorio y entra al directorio:**
   ```sh
   git clone <url-del-repo>
   cd django_base
   ```

2. **Crea y activa un entorno virtual:**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instala Django:**
   ```sh
   pip install django
   ```

4. **Aplica migraciones:**
   ```sh
   python manage.py migrate
   ```

5. **Crea un superusuario (opcional, para admin):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor:**
   ```sh
   python manage.py runserver
   ```

7. **Accede a la app:**
   - Blog: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Funcionalidades

- **Listado de posts:** Página principal con todas las publicaciones.
- **Detalle de post:** Haz clic en un título para ver el contenido completo.
- **Crear post:** Enlace para crear una nueva publicación.
- **Plantillas:** Uso de herencia de templates para un diseño consistente.

## Archivos principales

- `blog/views.py`: Vistas basadas en clase para listar, ver y crear posts.
- `blog/urls.py`: Rutas de la aplicación blog.
- `templates/_base.html`: Template base para heredar.
- `templates/post_list.html`: Lista de publicaciones.
- `templates/post_detail.html`: Detalle de una publicación.
- `templates/post_new.html`: Formulario para crear publicaciones.
- `django_base/settings.py`: Configuración del proyecto.

## Personalización

- Puedes agregar campos al modelo `Post` en `blog/models.py`.
- Para estilos, agrega archivos CSS en la carpeta `static/` y enlázalos en `_base.html`.
- Cambia el idioma o zona horaria en `settings.py` (`LANGUAGE_CODE`, `TIME_ZONE`).

## Notas

- El proyecto está en modo desarrollo (`DEBUG=True`).
- Los archivos estáticos se sirven desde la carpeta `static/`.
- Las plantillas se buscan en la carpeta `templates/` a nivel de proyecto.

## Requisitos

- Python 3.10+
- Django 5.2.4

---

¡Listo! Puedes usar este proyecto como base para tus propios blogs o como práctica