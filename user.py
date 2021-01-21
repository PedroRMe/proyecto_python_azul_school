#added to gitHub
import uuid
from bdusers import *
class User:
    def __init__(self,name,country,username):
        self.__name=name
        self.__country=country
        self.__username=username
        self.__id=str(uuid.uuid4())[0:4]


    def __str__(self):
        return "id: {} name: {} pais: {} Usuario: {} ".format(self.__id,self.__name,self.__country,self.__username)

    def get_id(self):
        return self.__id

    def set_name(self,name):
        self.__name=name
    
    def set_country(self,country):
        self.__country=country
        
    def set_username(self,username):
        self.__username=username


    id=property(get_id,set_name)
class UserMethod:

    """Clase para los metodos
        Methods:
        add_user: @ClassMethod
        show_user_ @ClassMethod

    """
    @classmethod
    def add_user(cls):
        name=input("Cual es tu nombre: ")
        country=input("De donde eres: ")
        username=input("Cual es tu username: ")
        user=User(name,country,username)
        return user

    @classmethod
    def show_users(cls,user_list):
        print("***********************************Usuarios*****************************")
        for user in user_list:
            print(user)
        print("************************************************************************")
    @classmethod
    def request_id(cls):
        id_user=input("Ingrese el identificador del usuario: ")
        return id_user

    @classmethod
    def c_name(cls):
        name=input("ingrese nuevo nombre")
        return name

    @classmethod
    def c_country(cls):
        country=input("ingrese nuevo pais")
        return country

    @classmethod
    def c_username(cls):
        username=input("ingrese nuevo username")
        return username
   







#def wrapper_get_id(function):
#    def hijo():
 #       print("*************************")
  #      id_user= input("Ingrese el id del usuario: ")
   #     function(id_user)
    #    print("**************************")
     #   return hijo

#@wrapper_get_id
#def delete_user(id_user):
 #   print("usuario eliminado") 


