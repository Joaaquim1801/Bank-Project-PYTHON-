from CPF.verificador import*

class Documents:
    def __init__(self, documents_id, cpf):
        self.id = documents_id
        self.__cpf = cpf

        while True:
            if not validador_cpf(self.cpf):
                print("CPF Inválido")
                novo_cpf = ver_cpf(digitar_cpf())
                self.cpf = novo_cpf
                continue
            else:
                break
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def show_informations(self):
        return f"Id: {self.id} | CPF: {self.__cpf} "
