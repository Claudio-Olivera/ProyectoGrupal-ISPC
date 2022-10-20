- Instalacion de entorno virtual con: pip install virtualenv
- Reviso version de virtual env con: virtualenv --version
- Creo entorno virtual con : virtualenv venv
- Activo entorno virtual con:  .\venv\Scripts\activate
- Reviso version de python y compruebo que ya sea de (venv) con: python --version
- Reviso version de pip y compruebo que ya sea de (venv) con: pip --version
- Configuro Vscode con F1 y escribo select interpreter, doy enter y selecciono la opción que corresponde a virtual env (esto se hace para que vscode use el interprete de virtual env)
- Abro nueva terminal y compruebo que ya aparece (venv) en la consola.

- Instalar Django con: pip install django
- Compruebo la instalación con : django-admin --version
- Inicio un nuevo proyecto de django con: django-admin startproject CuidaPets . (el punto final es para que se cree dentro de la carpeta que tengo creada)

### Manage.py sirve para ejecutar algunos comandos de administración como por ejemplo un servidor de desarrollo, copiar archivos de un lugar a otro, etc. 

- Puedo ejecutar el comando de ayuda: python manage.py --help (muestra lista de todos los comandos de manage.py)

- Ejecuto el proyecto con : python manage.py runserver (puedo indicar el puerto en el que quiero que se ejecute con: python manage.py runserver 3000 , ya que por defecto lo hace en el puerto 8000)
- Me dice que hay migraciones sin ser aplicadas, para aplicarlas : python manage.py makemigrations despues, python manage.py migrate
- Me crea un archivo db.sqlite3 que es la Database que usa django en desarrollo.
- Ctrl+click en http://127.0.0.1:8000/ y deria mostrarse la web de django inicial de nuestro proyecto.(Con Ctrl + c detengo el servidor.)
- Creación de un proyecto nuevo con el comando : python manage.py startapp myapp (En este caso myapp es nombre de ejemplo, puedo crear cuantos proyectos necesite, los mismos estarán acoplados al proyecto principal (se llama a los archivos desde el proyecto principal),que en este caso es CuidaPets) Muy parecido al concepto de componentes en Angular.







