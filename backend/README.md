1.-
Para poder probar el codigo, utilizar pyCharm para abrirlo ya que VsCode no detecta las importaciones entre carpetas (probamos todos los tipos de importaciones posibles, 
horas de intentos y modificaciones pero por algun motivo pylance utilizado en vscode no detecta bien las importaciones entre carpetas)
Cabe destacar, que el codigo no sufrió modificaciones cuando se pasó al ide de intellij pyCharm y funcionaba correctamente, es decir, el problema no estaba en 
las importaciones realizadas.

2.-
La carpeta .idea y el archivo main.py, se crean automáticamente cuando se hace un nuevo proyecto en pyCharm

3.-
En la carpeta models, al final de cada clase, estan comentadas las pruebas que se realizaron desde python manejando los datos en la db, por medio de la 
invocacion de los métodos de los objetos creados en la instanciación. Descomentar para poder hacer pruebas.

4.-
En la carpeta models, fue agregado como extra el codigo necesario en python para la creacion de las tablas. Además se pueden modificar los archivos para conectar 
con la database que se desee, por defecto , la configuracion es:
                                        host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234'

5.-
En la carpeta controllers, se pueden modificar los archivos para conectar con la database que se desee, por defecto , la configuracion es:
                                        host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234'
                                        
