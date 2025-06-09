# SkyRoute - Sistema de Gestión de Pasajes
---

## Descripción General

**SkyRoute** es un sistema de gestión de pasajes diseñado para **pequeñas agencias de viajes** que desean **digitalizar y optimizar** sus operaciones. Permite una administración integral de **clientes, destinos y ventas**, brindando funcionalidades clave como el registro, modificación y consulta de datos.

El sistema también incorpora un práctico **"botón de arrepentimiento"**, que facilita la cancelación eficiente y controlada de ventas.

---

## Integrantes del Grupo

* **Baigorria Sol Milagros** — GitHub: [@Solbaigorria3](https://github.com/Solbaigorria3)   
* **Luciano Castillo DNI:43062186** — GitHub: [@luciano1521](https://github.com/luciano1521)  
* **Isaias Emanuel Sudañez DNI: 39231001** — GitHub: [@emmaSDNZ](https://github.com/emmaSDNZ)  
* **Luciana Goldraij DNI: 49262403** — GitHub: [@lugoldraij](https://github.com/lugoldraij)  

---

## Instrucciones de Ejecución

Para poner en marcha el sistema **SkyRoute**, sigue los siguientes pasos:

### 1. Clonar el repositorio

```bash
git clone https://github.com/emmaSDNZ/helicetech-SkyRouteS.R.L
cd SkyRoute
````

### 2. Configurar la base de datos

* Asegúrate de tener un servidor **MySQL** instalado y en funcionamiento.
* Edita el archivo `src/conexion.py` (o `config.py` si corresponde) para configurar los parámetros de conexión a la base de datos:

  * `host`
  * `usuario`
  * `contraseña`
  * `nombre de la base de datos`
* Ejecuta el script SQL `data/helice_bn.sql` para crear la base de datos, las tablas necesarias e insertar los datos por defecto. Puedes hacerlo desde la línea de comandos de MySQL o mediante herramientas como **MySQL Workbench**:

```bash
mysql -u tu_usuario -p < data/helice_bn.sql
```

*(Reemplaza `tu_usuario` con tu usuario de MySQL; cuando se te solicite, ingresa tu contraseña.)*

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el programa principal

```bash
python src/main.py
```

Al ejecutarlo, verás el menú de opciones del sistema en la terminal.

---

### Principios y Buenas Prácticas de Diseño

El desarrollo de **SkyRoute** se ha guiado por principios y buenas prácticas que garantizan un código:

* **Mantenible**
* **Escalable**
* **Limpio y legible**

#### Principios aplicados

* **Principio de Responsabilidad Única (SRP):**
  Cada módulo tiene una responsabilidad bien definida, separando la lógica de acceso a datos (`conexion.py`, `sql_consultas.py`) de la lógica de negocio y presentación (`gestionar_*`, `main.py`).

* **Modularidad y Separación de Capas:**
  El sistema se organiza en capas bien diferenciadas:

  * **Capa de datos:** manejo de consultas SQL y conexión a la base de datos.
  * **Capa de negocio:** gestión de clientes, destinos, ventas y cancelaciones.
  * **Capa de presentación:** menús y control de flujo principal.

* **Centralización de Consultas SQL:**
  Todas las consultas SQL están centralizadas en `sql_consultas.py`, lo que facilita su mantenimiento, fomenta la reutilización y evita la duplicación.

* **Documentación Estandarizada:**
  El código incluye **docstrings estructurados** en las funciones, siguiendo el siguiente formato:

  * Descripción general
  * Parámetros de entrada
  * Valores retornados
  * Posibles excepciones
  * Ejemplos de uso

---

## Estructura del Repositorio

El repositorio de **SkyRoute** está organizado de manera clara y estandarizada para fomentar el desarrollo colaborativo, facilitar el mantenimiento y permitir una comprensión integral del proyecto.

### Estructura Principal

---


### `src/`

Esta carpeta alberga todo el **código fuente** del proyecto, incluyendo los módulos y funciones que componen la aplicación principal.

#### Estructura interna

```
src/
├── conexion.py                  # Módulo para la conexión a la base de datos
├── main.py                      # Archivo principal con menú y control de flujo
├── sql_consultas.py             # Consultas SQL reutilizables (SELECT, INSERT, UPDATE, DELETE)
├── gestionar_cliente.py         # Gestión de clientes (alta, baja, modificación, listado)
├── gestionar_destino.py         # Gestión de destinos (alta, baja, modificación, listado)
├── gestionar_ventas.py          # Registro y administración de ventas
├── gestionar_arrepentimiento.py # Funcionalidad para cancelar ventas
├── sql_ejecutar.py              # Ejecución de scripts SQL iniciales
└── sistema.py                   # Funciones auxiliares del sistema (acerca de, salir, etc.)
```

#### Descripción de los componentes:

* **conexion.py:**
  Módulo encargado de establecer y gestionar la conexión con la base de datos MySQL.

* **main.py:**
  Archivo principal que actúa como punto de entrada del sistema. Contiene el menú interactivo y el control de flujo general de la aplicación.

* **sql\_consultas.py:**
  Centraliza todas las consultas SQL utilizadas en el sistema. Incluye operaciones **SELECT, INSERT, UPDATE y DELETE**, reutilizables por los distintos módulos.

* **gestionar\_cliente.py:**
  Módulo de gestión de clientes. Permite realizar altas, bajas, modificaciones y listados de clientes registrados en el sistema.

* **gestionar\_destino.py:**
  Módulo de gestión de destinos turísticos. Ofrece funcionalidades para crear, editar, eliminar y consultar destinos disponibles.

* **gestionar\_ventas.py:**
  Módulo encargado de la gestión integral de ventas de pasajes. Permite registrar nuevas ventas y administrar el histórico de transacciones.

* **gestionar\_arrepentimiento.py:**
  Implementa la funcionalidad del **botón de arrepentimiento**, permitiendo cancelar ventas de manera segura, siguiendo los requisitos legales y funcionales previstos.

* **sql\_ejecutar.py:**
  Módulo de soporte que facilita la ejecución de scripts SQL iniciales para preparar el entorno (creación de tablas, datos por defecto, etc.).

* **sistema.py:**
  Incluye funciones auxiliares del sistema, como la opción **"Acerca de"**, funciones de cierre de aplicación y otras utilidades generales.



### `tests/`

Contiene las **pruebas automatizadas** (unitarias, de integración, funcionales, etc.) para verificar el correcto funcionamiento del código en `src/`.

Su uso es esencial para:

* la detección temprana de errores
* garantizar la calidad y estabilidad del software

---

### `docs/`

Carpeta destinada a la **documentación técnica**, guías de usuario, manuales y otros recursos útiles para comprender y utilizar el proyecto. Puede incluir:

* Diagramas
* Flujos de trabajo
* Especificaciones
* Notas importantes
* Guías de instalación y uso

---

### `data/`

Carpeta para **archivos de datos** esenciales para la ejecución o pruebas del proyecto:

* Datos de ejemplo
* Archivos de configuración
* Datasets

#### Estructura:

```
data/
└── helice_bn.sql                # Script para crear la base de datos, tablas e insertar valores por defecto
```

---

### `.gitignore`

Archivo de configuración para que **Git ignore** ciertos archivos y carpetas no necesarios en el control de versiones, como:

* Archivos temporales
* Dependencias descargadas
* Configuraciones locales

---

### `requirements.txt`

Contiene un listado de todas las **dependencias y librerías** necesarias para que el proyecto funcione correctamente. Facilita la instalación mediante `pip`.

---

### `README.md`

El archivo que estás leyendo. Proporciona una **descripción general** del proyecto, instrucciones básicas para comenzar y una explicación detallada de la estructura del repositorio.

---

Esta organización garantiza una **clara separación de recursos** y simplifica el trabajo colaborativo. Además, facilita la incorporación de nuevos colaboradores y contribuye al mantenimiento a largo plazo del proyecto.
