
# Guía de  para integrande que constribuyen al Proyecto

Este documento describe el flujo de trabajo recomendado para colaborar eficientemente en el repositorio de **helicetech-SkyRouteS.R.L**. Seguir estos pasos asegura una integración de código fluida, facilita la revisión y minimiza conflictos entre los miembros del equipo.

---

## 1. Clonar el Repositorio

Para empezar a trabajar en el proyecto, cada integrante debe **clonar el repositorio remoto** a su máquina local. Este paso se realiza **una única vez**.

```bash
git clone https://github.com/emmaSDNZ/helicetech-SkyRouteS.R.L/
```

Una vez clonado, accede al directorio del proyecto:

```bash
cd helicetech-SkyRouteS.R.L
```

---

## 2. Cambio a la Rama de Desarrollo (`dev`)

La rama principal para el desarrollo activo es `dev`. Es **fundamental** trabajar sobre esta rama y **no** realizar desarrollos directamente en `main`, que está reservada para versiones estables del proyecto.

```bash
git checkout dev
```

**Nota:** Si la rama `dev` no está disponible localmente, primero debes traerla desde el repositorio remoto:

```bash
git fetch origin
git checkout dev
```

---

## 3. Creación de Ramas de Trabajo (Features)

Cada nueva funcionalidad, mejora o corrección de error debe desarrollarse en una **rama independiente**, derivada de `dev`. Esto facilita el control de cambios, las revisiones de código (a través de **Pull Requests**) y ayuda a evitar conflictos con el trabajo de otros desarrolladores.

La convención de nombres sugerida es:

* `feature/nombre-de-la-funcionalidad` para nuevas funcionalidades.
* `fix/nombre-del-bug` para correcciones de errores.

**Ejemplo:**

```bash
git checkout -b feature/formulario-registro
```

---

## 4. Confirmación de Cambios (`commits`)

Una vez que hayas realizado los cambios en los archivos de tu proyecto, sigue estos pasos para confirmarlos:

### 4.1 Verificar los cambios realizados

Antes de agregar, es buena práctica revisar qué archivos han sido modificados:

```bash
git status
```

### 4.2 Agregar los archivos modificados

Esto prepara tus cambios para el `commit`:

```bash
git add .
```

### 4.3 Crear un commit con un mensaje descriptivo

El mensaje del `commit` debe ser claro y conciso, describiendo los cambios realizados:

```bash
git commit -m "feat: implementar formulario de registro de usuarios"
```

---

## 5. Envío de Cambios al Repositorio Remoto (`push`)

Después de realizar el `commit`, debes subir tu rama al repositorio remoto para que tus cambios sean visibles:

```bash
git push origin nombre-de-la-rama
```

**Ejemplo:** `git push origin feature/formulario-registro`

---

## 6. Creación de Pull Request (PR)

Una vez que hayas finalizado el desarrollo de tu funcionalidad o corrección, debes generar un **Pull Request (PR)** desde GitHub. Esto permite que otros miembros del equipo revisen tus cambios antes de que se integren a la rama `dev`.

**Pasos:**

1.  **Ingresar al repositorio en GitHub.**
2.  **Verificar** que la rama activa sea la que deseas integrar (tu rama de `feature` o `fix`).
3.  Hacer clic en el botón **"Compare & pull request"**.
4.  Asegurarte de que la configuración sea la siguiente:
    * **Base branch:** `dev` (rama a la que quieres fusionar)
    * **Compare:** `feature/mi-funcionalidad` (tu rama de trabajo)
5.  **Completar el título y la descripción del PR** de forma clara.
6.  **Enviar para revisión.**

---

## Resumen de Comandos Esenciales

Aquí tienes una tabla rápida con los comandos más utilizados:

| Tarea                             | Comando                                        |
| :-------------------------------- | :--------------------------------------------- |
| Clonar repositorio                | `git clone [URL_REPOSITORIO]`                  |
| Cambiar a rama `dev`              | `git checkout dev`                             |
| Crear nueva rama (ej. `feature`) | `git checkout -b feature/nombre-de-la-rama`    |
| Verificar estado de archivos      | `git status`                                   |
| Agregar todos los cambios         | `git add .`                                    |
| Confirmar cambios                 | `git commit -m "mensaje descriptivo"`          |
| Subir rama al remoto              | `git push origin nombre-de-la-rama`            |
| Traer cambios del remoto          | `git pull origin dev` (desde la rama `dev`)    |

---
