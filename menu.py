from user import UserMethod
from bdusers import *
  
ADD = 1
SEARCH = 2
DELETE = 3
SHOW = 4
CHANGE = 6

  
user_list = bd_user()
  
def selected_option(option):
   
   if option == ADD:
       user = UserMethod.add_user()
       add_user_db(user, user_list)
   
   elif option == SEARCH:
       id_user = UserMethod.request_id()
       search_user_db(id_user, user_list)
   
   elif option == DELETE:
       id_user = UserMethod.request_id()
       delete_user_db(id_user, user_list)
   
   elif option == SHOW:
       UserMethod.show_users(user_list)

   elif option == CHANGE:
       id_user=UserMethod.request_id()
       name_u=UserMethod.c_name()
       country=UserMethod.c_country()
       username=UserMethod.c_username()
       change_user(id_user,user_list,name_u,country,username)



  
  
message = """Control de usuarios
**Escoge una opción**
1.-Agregar Usuario
2.-Buscar Usuario
3.-Eliminar Usuario
4.-Mostrar Usuarios
5.-Salir
6.-Modificar Usuario
Opción: """

option=0
while option!=5:
    option=int(input(message))
    selected_option(option)

print("Hasta la proxima")    
    