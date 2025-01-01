from classes import documents, user, user_type

documento01 = documents.Documents(documents_id=1 ,cpf="145.382.206-20")
#documento02 = Documents(documents_id=1 ,cpf="145.821.793-91")
tipo01 = user_type.User_type(type_id=1, type_name="Administrador")
tipo02 = user_type.User_type(type_id=2, type_name="Comum")

usuario01 = user.User(name="James", email="james2015@gmail.com", user_id=1, saldo_inicial=300, user_type=tipo01)
usuario02 = user.User(name="Raquel", email="raquelsilva@hotmail.com", user_id=1, saldo_inicial=500, user_type=tipo02)
usuario03 = user.User(name="Henrique", email="henriquegames@gmail.com", user_id=1, saldo_inicial=150, user_type=tipo02)
usuario01.transferir(usuario02, 75)
#usuario02.transferir(usuario03, 200)

print(usuario01.show_informations())
print(usuario02.show_informations())
print(f"{usuario03.show_informations()}\n")

usuario01.investir()
print(usuario01.show_informations())
#usuario01.retirar_dinheiro(100,usuario02)
#print(usuario02.show_informations())