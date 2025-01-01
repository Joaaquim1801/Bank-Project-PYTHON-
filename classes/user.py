from time import sleep
from os import system

def requer_permissao(permissao):
    def decorator(func):
        def wrapper(obj, *args, **kwargs):
            if obj.type.type_name == permissao:
                return func(obj, *args, **kwargs)
            else:
                raise PermissionError(f"O usuário {obj.name} não tem permissão para utilizar essa função")
        return wrapper
    return decorator


class User:
    lista_usuarios = []
    def __init__(self, name, email, user_id, user_type, saldo_inicial = 0.0):
        self._name = name
        self._email = email
        self.id = user_id
        self.saldo_inicial = saldo_inicial
        self.type = user_type
        User.lista_usuarios.append(name)


    def show_informations(self):
        type_info = self.type.get_type_info()
        return f"Id: {self.id} | Name: {self.name} | Email: {self.email} | Saldo Inicial: R${self.saldo_inicial:.2f} | Cargo: {type_info}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo_inicial += valor
            return f"Valor depositado: {valor} | Saldo: {self.saldo_inicial}"
        return "O valor depositado deve ser positivo"

    def transferir(self, destinatario, valor):# A fazer
        if valor > 0 and self.saldo_inicial >= valor:
            self.saldo_inicial -= valor
            destinatario.receber(valor)
            return f"Transferência Realiada! Enviado R${valor} para {destinatario}"
        elif valor <= 0:
            return "O valor da transferência deve ser positivo"
        return "Saldo Insuficiente"
    
    def receber(self, valor):
        if valor > 0:
            self.saldo_inicial += valor
            return f"Recebimento realido com sucesso!"
        return "O valor deve ser positivo"
    
    def retirar(self,valor):
        self.saldo_inicial -= valor

    @requer_permissao("Administrador")
    def retirar_dinheiro(self, valor, destinatario):
        if destinatario.name in User.lista_usuarios:
            if valor > 0:
                destinatario.retirar(valor)
                return f"R${valor} retirado de {destinatario}"
            elif valor <= 0:
                return "O valor mínimo para retirar o dinheiro de um usuário deve ser maior que zero"
        return "O usuário não existe"
    
    def investir(self):
        while True:
            print(f"Saldo Atual: R${self.saldo_inicial}")
            for c in range(30, 0, -1):
                print(f"Tempo Restante: {c} segundos")
                sleep(1)
                system('cls')
            self.saldo_inicial *= 1.1
            print(f"Saldo Atual: R${self.saldo_inicial:.2f}")
            resposta = str(input("Deseja continuar?[S/N] ")).upper()
            if resposta in ("NÃO", "N"):
                break
            else:
                continue

    def sacar(self,valor):
        if valor > 0 and valor >= self.saldo_inicial:
            self.saldo_inicial -= valor
            return f"R$ {valor} sacado "
        elif valor <= 0:
            return "O valor da transferência deve ser positivo"

    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
