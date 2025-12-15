# Gestión Judicial

Este proyecto es una aplicación Django simple para gestionar clientes, causas judiciales y movimientos asociados.

## Requisitos

- Python 3.11 o superior
- Django 6.0
- SQLite (configurado por defecto como `db.sqlite3`)

Opcional: es recomendable usar un entorno virtual (`venv`).

## Instalación y ejecución desde 0

1. Clonar el repositorio:

   git clone <url-del-repo>
   cd gestion_judicial

2. Crear y activar un entorno virtual:

   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

3. Instalar dependencias:

   pip install "django==6.0"

   (Si se provee `requirements.txt`):
   pip install -r requirements.txt

4. Aplicar migraciones y crear administrador:

   python manage.py migrate
   python manage.py createsuperuser

5. Ejecutar el servidor de desarrollo:

   python manage.py runserver

6. Abrir en el navegador:

- Página principal: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Causas: http://127.0.0.1:8000/causas/
- Clientes: http://127.0.0.1:8000/clientes/

Notas:
- La plantilla utiliza Bootstrap vía CDN, por lo que no es necesario compilar assets.
- La base de datos por defecto es `db.sqlite3` en la raíz del proyecto.

## Estructura y funciones de cada app

- `core`:
  - Vista principal (`HomeView`) y plantillas base (`base.html`, `partials/`) que sirven como layout común.

- `clientes`:
  - Modelo `Cliente` (nombres, apellidos, RUT, contacto, descripción, estado activo).
  - Vistas: listado, detalle y edición (`ClienteListView`, `ClienteDetailView`, `ClienteUpdateView`).
  - En la vista detalle se muestran las causas asociadas al cliente.

- `causas`:
  - Modelo `Causa` (competencia, corte, tribunal, tipo, rol, año, cliente FK, estado, descripción).
  - Permite listar, filtrar y buscar causas por cliente, tribunal, tipo, rol y año.
  - `CausaDetailView` muestra detalles de la causa y lista/permite agregar `movimientos`.
  - `CausaUpdateView` permite editar una causa existente.

- `movimientos`:
  - Modelo `Movimiento` (FK a `Causa`, fecha, descripción, observaciones).
  - Formulario `MovimientoForm` utilizado dentro de la vista detalle de la causa para agregar eventos a una causa.

Interacción entre apps:
- Un `Cliente` puede tener muchas `Causa` (relación `1:N`).
- Una `Causa` puede tener muchos `Movimiento` (relación `1:N`) — los movimientos representan eventos o actuaciones judiciales vinculadas a la causa.

## Administración

- Los modelos `Cliente`, `Causa` y `Movimiento` están registrados en el admin de Django.

## Desarrollo y pruebas

- No se incluyen pruebas específicas en este repositorio (ver directorios `tests.py` por app).
- Para añadir nuevas dependencias, actualice o cree `requirements.txt` con `pip freeze > requirements.txt`.

## Contribuir

- Abrir un issue o enviar un pull request con cambios claros y tests cuando aplique.

---
