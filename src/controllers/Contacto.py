from Insert_Contacto import insert_contacto
from Delete_Contacto import delete_contacto
from Select_contacto import select_contacto
#no borrar este import , se utiliza al descomentar la linea 27
import Select_all_contactos

class Contacto:
    def __init__(self, name, email, message,Id_Contacto):
        self.name = name
        self.email = email
        self.message = message
        self.Id_Contacto = Id_Contacto

#crea nuevo registro de datos en la tabla contacto
    def crear_contacto(self):
        insert_contacto(self)

#obtiene el registro seleccionado por id desde la tabla user_card
    def obtener_contacto_por_id(self):
        select_contacto([self.Id_Contacto])

#borra el registro de la tabla user_card
    def borrar_contacto(self):
        delete_contacto([self.Id_Contacto])

#obtiene todos los datos de la tabla contacto
#Select_all_contactos.get_all_contacto()

#Contacto no necesita tener un metodo para actualizar los mensajes.


#-----------------INVOCACION DE METODOS Y CREACION DE OBJETOS----------------------#
#contacto1= Contacto('Patricio','patricio@gmail.com','Como recomendación, me gustaria poder comprar cosas para mis mascotas en la web',1)

#contacto1.crear_contacto()
#contacto1.obtener_contacto_por_id()

#contacto2=Contacto('German', 'german@gmail.com', 'Queria informarles que encontre una brecha de seguridad en su web, comuniquense a mi correo cuanto antes.', 2)

#contacto2.crear_contacto()
#contacto2.obtener_contacto_por_id()


#contacto2.obtener_contacto_por_id()

#contacto1.borrar_contacto()

