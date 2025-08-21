# Django Blog Project

Este proyecto es una aplicación web de blog desarrollada con Django 5.2.4. Permite a los usuarios autenticados crear, listar, editar y eliminar publicaciones, además de gestionar su cuenta mediante registro, inicio y cierre de sesión. El diseño utiliza herencia de plantillas para mantener una estructura consistente y profesional.

---

## Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Configuración](#instalación-y-configuración)
- [Uso](#uso)
- [Funcionalidades Detalladas](#funcionalidades-detalladas)
- [Personalización](#personalización)
- [Notas Técnicas](#notas-técnicas)
- [Requisitos](#requisitos)
- [Créditos](#créditos)

---

## Características

- **CRUD de publicaciones:** Crear, leer, actualizar y eliminar posts.
- **Autenticación de usuarios:** Registro, login y logout.
- **Protección de vistas:** Solo usuarios autenticados pueden crear, editar o eliminar posts.
- **Herencia de plantillas:** Diseño consistente en todas las páginas.
- **Panel de administración:** Gestión avanzada de usuarios y posts.
- **Mensajes de bienvenida y navegación dinámica según estado de sesión.**
- **Soporte para archivos estáticos (CSS, JS, imágenes).**
- **Configuración de zona horaria e idioma.**

---

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
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
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
│   ├── post_edit.html
│
├── static/
│   └── (archivos estáticos opcionales)
│
├── db.sqlite3
├── manage.py
```

---

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

3. **Instala dependencias:**
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

---

## Uso

- **Página principal:** Muestra el listado de publicaciones.
- **Detalle de post:** Haz clic en el título para ver el contenido completo.
- **Crear post:** Enlace para crear una nueva publicación (solo usuarios autenticados).
- **Editar y eliminar post:** Solo el autor puede editar o eliminar sus publicaciones.
- **Registro y login:** Acceso mediante la app `accounts`.

---

## Funcionalidades Detalladas

### Blog

- **ListView:** Muestra todos los posts ordenados por fecha.
- **DetailView:** Muestra el contenido completo de un post.
- **CreateView:** Permite crear un nuevo post (requiere login).
- **UpdateView:** Permite editar un post (solo el autor).
- **DeleteView:** Permite eliminar un post (solo el autor).

### Usuarios

- **Registro:** Formulario para crear una cuenta nueva.
- **Login:** Autenticación de usuarios.
- **Logout:** Cierre de sesión.

### Plantillas

- **_base.html:** Plantilla base con navegación y bloques para contenido.
- **Herencia:** Todas las páginas extienden la base para mantener el diseño.

### Seguridad

- **Protección de vistas:** Solo usuarios autenticados pueden crear, editar o eliminar posts.
- **CSRF:** Protección en formularios.

### Administración

- **Panel admin:** Gestión avanzada de usuarios y posts desde `/admin`.

---

## Personalización

- **Modelo Post:** Puedes agregar campos en `blog/models.py` (ejemplo: imagen, etiquetas).
- **Estilos:** Agrega CSS en la carpeta `static/` y enlázalos en `_base.html`.
- **Idioma y zona horaria:** Modifica `LANGUAGE_CODE` y `TIME_ZONE` en `settings.py`.
- **Templates:** Personaliza los archivos en `templates/` para adaptar el diseño.

---

## Notas Técnicas

- El proyecto está en modo desarrollo (`DEBUG=True`).
- Los archivos estáticos se sirven desde la carpeta `static/`.
- Las plantillas se buscan en la carpeta `templates/` a nivel de proyecto.
- El sistema de autenticación usa la app `accounts` para registro y login.
- El archivo `settings.py` incluye rutas y configuración para templates, estáticos y redirecciones tras login/logout.

---

## Requisitos

- Python 3.10+
- Django 5.2.4

---

## Créditos

Desarrollado por [g].  
Basado en la estructura oficial de Django.

---

¡Listo! Puedes usar este proyecto como base para tus propios blogs, como práctica para aprender Django, o expandirlo con nuevas