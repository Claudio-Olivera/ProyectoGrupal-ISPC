from controller.Sql_Insert import insert_user_card
from controller.Sql_Update import update_user_card
from controller.Sql_Delete import delete_user_card
from controller.Sql_Select import get_only_user_card

class Card:
    def __init__(self, Mascotas, Presentacion, Imagen,Id_more_Data, Id_user_Card ):
        self.Mascotas = Mascotas
        self.Presentacion = Presentacion
        self.Imagen = Imagen
        self.Id_more_Data = Id_more_Data
        self.Id_user_Card = Id_user_Card

#crea nuevo registro de datos en la tabla user_card
    def crear_card(self):
        insert_user_card(self)

#obtiene el registro seleccionado por id desde la tabla user_card
    def obtener_card(self):
        get_only_user_card([self.Id_user_Card])

#actualiza el registro de la tabla user_card
    def actualizar_card(self):
            update_user_card(self)

#borra el registro de la tabla user_card
    def borrar_card(self):
        delete_user_card([self.Id_user_Card])


#-----------------INVOCACION DE METODOS Y CREACION DE OBJETOS----------------------#

#card1 = Card('Perros, Gatos, Hamsters', 'Se administrar medicacion a perros y gatos, hago paseos, tengo experiencia con reptiles ', '/images/laura.jpg',2,2)
#card1.crear_card()

#card1.borrar_card()

#card1.obtener_card()

#card1=Card('Reptiles', 'Tengo experiencia en el cuidado de reptiles', '/images/reptil.jpg',2,2)
#card1.actualizar_card()

