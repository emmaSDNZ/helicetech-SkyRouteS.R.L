# helicetech-SkyRouteS.R.L
Software ERP 


--DOC 

1: Clonar el repositorio
Cada integrante del equipo debe clonar el repositorio remoto a su máquina local. Este procedimiento se realiza una única vez, al iniciar la colaboración en el proyecto.

-->     git clone https://github.com/emmaSDNZ/helicetech-SkyRouteS.R.L/

Una vez clonado el repositorio, se debe acceder al directorio del mismo:

-->     cd helicetech-SkyRouteS.R.L

2. Cambio a la rama de desarrollo (dev)

La rama principal para el desarrollo activo es dev. Es fundamental trabajar sobre esta base y <NO> realizar desarrollos directamente en main, que está reservada para versiones estables.

-->     git checkout dev

Nota: Si la rama dev no se encuentra disponible localmente, primero debe traerse desde el repositorio remoto con:

-->     git fetch origin
-->     git checkout dev

//ESTE ITEM NO APLICA PARA EL ABP PRIMERA INSTANCIA PRESENTACION DEL PROYECTO
//SALTA DIRECTAMENTE AL 4
3. Creación de ramas de trabajo
Cada nueva funcionalidad o corrección debe desarrollarse en una rama independiente, derivada de dev. Esto facilita el control de cambios, revisión de código (Pull Requests), y evita conflictos con otros desarrolladores.

La convención de nombres sugerida es:

feature/nombre-de-la-funcionalidad para nuevas funcionalidades.


Ejemplos:
git checkout -b feature/formulario-registro

4. Confirmación de cambios (commits)
Una vez realizados los cambios en los archivos del proyecto, se deben seguir los siguientes pasos para confirmarlos:

4.1 Verificar los cambios realizados

-->     git status

4.2 Agregar los archivos modificados 

-->     git add .

4.3 Crear un commit con un mensaje descriptivo

-->     git commit -m "<debe ser descriptivo>"

5. Envío de cambios al repositorio remoto (push)

Una vez realizado el commit, se debe subir la rama al repositorio remoto:

-->     git push origin nombre-de-la-rama


6. Creación de Pull Request
Al finalizar el desarrollo, cada integrante debe generar un Pull Request (PR) desde GitHub. Esto permite revisar los cambios antes de integrarlos a la rama dev.

Pasos:

1)  Ingresar al repositorio en GitHub.

2)  Verificar que la rama activa sea la que se desea integrar.

3)  Hacer clic en “Compare & pull request”.

4)  Asegurar que:

        Base branch: dev

        Compare: feature/mi-funcionalidad

5)  Completar el título y descripción del PR.

6)  Enviar para revisión.



Resumen de comandos esenciales
    Tarea	                    Comando
Clonar repositorio	    git clone https://github.com/...
Cambiar a rama dev	    git checkout dev
Crear nueva rama	    git checkout -b feature/nombre
Verificar estado	    git status
Agregar cambios	        git add .
Confirmar cambios	    git commit -m "mensaje"
Subir rama	            git push origin nombre-de-la-rama
Traer cambios del 
repositorio remoto	    git pull origin dev (desde la rama dev)
