
def bd_user():
    return []


def add_user_db(user,user_list):
    user_list.append(user)
    print("Usuario agregado")
    

def search_user_db(id_user,user_list):
    print("*****************************Busqueda de Usuario**********************")
    for index,user in enumerate (user_list):
        if id_user==user.id:
            print(user_list[index])
            
        else:
            print("*****************Usuario no encontrado***********************")    
            break
    print("*********************************************************************")

def delete_user_db(id_user,user_list):
    print("*****************************Busqueda de Usuario**********************")
    for index,user in enumerate (user_list):
        if id_user==user.id:
            user_list.pop(index)
            print("*Usuario eliminado*") 
            break           
        else:
            print("*****************Usuario no encontrado***********************")    
            
    print("*********************************************************************")

def change_user(id_user,user_list,name1,country,usr):
    for index,user in enumerate (user_list):
        if id_user==user.id:
                user_list[index].set_name(name1)
                user_list[index].set_country(country)
                user_list[index].set_username(usr)
                print("Usuario Actualizado")
                break
        else:
            print("No encontrado")




