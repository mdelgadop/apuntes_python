#instalar un entorno virtual para que, lo que instalemos, se quede aquí y no afecte a otros proyectos
# python -m venv fastapi-venv

#activamos el entorno virtual
# fastapi-venv\Scripts\activate

"""Para corregir la restricción que trae por defecto PowerShell para ejecutar Script en Windows, realiza lo siguientes pasos:
Abre la consola PowerShell como administrador y comprueba el error escribiendo «Get-ExecutionPolicy». Si al hacer clic en Enter la consola te devuelve : 
«Unrestricted», entonces tendrás que modificar la configuración
 
Escribe en la consola «Set-ExecutionPolicy Unrestricted» y a continuación contesta con un "S" o "Y", para indicar que quieres modificarla."""

#instalamos fastApi en el entorno virtual:
#pip install fastapi

#instalamos uvicorn, el servidor web donde ejecutar la api
#pip install uvicorn

#Creo main.py y lo ejecuto (con --reload para que el servidor no se pare al hacer un cambio):
#uvicorn main:app --reload
