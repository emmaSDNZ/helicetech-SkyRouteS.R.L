---
# SkyRoute - Sistema de Gestión de Pasajes
---

## Descripción General

SkyRoute es un sistema de gestión de pasajes diseñado para **pequeñas agencias de viajes** que buscan digitalizar y optimizar sus operaciones. Facilita la administración integral de **clientes, destinos y ventas**, ofreciendo funcionalidades clave como el registro, modificación y consulta de datos. Además, incorpora un práctico **"botón de arrepentimiento"** para la cancelación eficiente de ventas.

---

## Integrantes del Grupo

* **[Baigorria Sol Milagros]** - GitHub: [@usuario1_github](https://github.com/usuario1_github)
* **[Luciano Castillo ]** - GitHub: [@(https://github.com/usuario2_github](https://github.com/usuario2_github)
* **[Isaias Emanuel Sudañez]** - GitHub: [@(https://github.com/emmaSDNZ](https://github.com/emmaSDNZ))
* **[Luciana Goldraij]** - GitHub: [@usuario3_github](https://github.com/usuario3_github)


---

## Instrucciones de Ejecución

Para poner en marcha el sistema SkyRoute, sigue los siguientes pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/emmaSDNZ/helicetech-SkyRouteS.R.L]
    cd SkyRoute
    ```

2.  **Configura la base de datos:**
    * Asegúrate de tener un servidor MySQL instalado y funcionando.
    * Edita el archivo `src/conexion.py` (o `config.py` si decides usar ese) para configurar los parámetros de conexión a tu base de datos (host, usuario, contraseña, nombre de la base de datos).
    * Ejecuta el script SQL `data/helice_bn.sql` para crear la base de datos y las tablas necesarias, e insertar los datos por defecto. Puedes hacerlo desde la línea de comandos de MySQL o con una herramienta como MySQL Workbench:
        ```bash
        mysql -u tu_usuario -p < data/helice_bn.sql
        ```
        *(Reemplaza `tu_usuario` con tu usuario de MySQL y, cuando te lo pida, introduce tu contraseña).*

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta el programa principal:**
    ```bash
    python src/main.py
    ```
    Una vez ejecutado, verás el menú de opciones del sistema en la terminal.

---

## Estructura del Repositorio

El repositorio de SkyRoute está organizado de manera clara y estandarizada, promoviendo el desarrollo colaborativo, la facilidad de mantenimiento y una comprensión integral del proyecto.

A continuación, se detalla la estructura principal:

### `src/`
Esta carpeta alberga todo el **código fuente** del proyecto, incluyendo los módulos, clases y funciones que componen la aplicación principal.

**Ejemplo de estructura interna:**
```
src/
├── conexion.py                 # Módulo para la conexión a la base de datos
├── main.py                     # Archivo principal con menú y control de flujo
├── sql_consultas.py            # Consultas SQL reutilizables (SELECT, INSERT, UPDATE, DELETE)
├── gestionar_cliente.py        # Gestión de clientes (alta, baja, modificación, listado)
├── gestionar_destino.py        # Gestión de destinos (alta, baja, modificación, listado)
├── gestionar_ventas.py         # Registro y administración de ventas
├── gestionar_arrepentimiento.py # Funcionalidad para cancelar ventas
├── sql_ejecutar.py             # Ejecución de scripts SQL iniciales
└── sistema.py                  # Funciones auxiliares del sistema (acerca de, salir, etc.)
```

---

### Principios y Buenas Prácticas de Diseño

Para asegurar un código **mantenible, escalable y limpio**, SkyRoute se construyó bajo los siguientes principios y patrones de diseño:

* **Principio de Responsabilidad Única (SRP):** Cada módulo posee una responsabilidad bien definida, separando la lógica de acceso a datos (ej. `conexion.py`, `sql_consultas.py`) de la lógica de negocio y presentación (ej. `gestionar_*` y `main.py`).
* **Modularidad y Separación de Capas:** La arquitectura se divide en capas claras:
    * **Capa de datos:** Maneja las consultas SQL y la conexión a la base de datos.
    * **Capa de negocio:** Contiene la lógica para gestionar clientes, destinos, ventas y cancelaciones.
    * **Capa de presentación:** Comprende los menús y el control de flujo principal.
* **Centralización de Consultas SQL:** Todas las sentencias SQL están consolidadas en `sql_consultas.py`, lo que optimiza su mantenimiento, reutilización y previene la duplicación.
* **Documentación de Código Estandarizada:** Se utilizan **docstrings estructurados** en las funciones, siguiendo un patrón claro que incluye:
    * Descripción general
    * Parámetros de entrada
    * Valores retornados
    * Posibles excepciones
    * Ejemplos de uso

---

### `tests/`
Contiene las **pruebas automatizadas** (unitarias, de integración, funcionales, etc.) para verificar el correcto funcionamiento del código en `src/`. Es fundamental para la detección temprana de errores y para asegurar la calidad del software.

---

### `docs/`
Destinada a la **documentación técnica**, guías de usuario, manuales y cualquier otro recurso que facilite la comprensión del proyecto, incluyendo diagramas, flujos de trabajo, especificaciones y notas importantes. También puede contener guías de instalación y uso.

---

### `data/`
Almacena los **archivos de datos** esenciales para la ejecución o pruebas del proyecto, como datos de ejemplo, archivos de configuración o datasets. Su propósito es separar el código de los datos que consume.
data/
├── helice_bn.sql              # Script para crear la base de datos, tablas e insertar valores por defecto.
---

### `.gitignore`
Este archivo configura Git para **ignorar** ciertos archivos o carpetas (ej. temporales, dependencias descargadas, configuraciones locales) y evitar que sean versionados.

---

### `requirements.txt`
Enumera las **dependencias y librerías** necesarias para que el proyecto opere correctamente, facilitando su instalación a través de herramientas como `pip`.

---

### `README.md`
El archivo que estás leyendo. Ofrece una **descripción general** del proyecto, instrucciones básicas para comenzar y una explicación detallada de la estructura del repositorio.

---

Esta organización garantiza una **clara separación de recursos**, simplificando el trabajo en equipo y permitiendo que cada miembro se enfoque en su área sin confusiones. Además, agiliza la incorporación de nuevos colaboradores y el mantenimiento a largo plazo del proyecto.

---

Para cualquier consulta sobre la estructura o el contenido de estas carpetas, por favor, contacta con el responsable del proyecto o el equipo de DevOps.
