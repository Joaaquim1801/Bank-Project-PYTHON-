import re

#123.456.789-12
def validador_cpf(CPF):
    numeros = []
    numeros_multiplicados = []

    #Remover pontos e traços, retorna uma lista com os conjuntos de números
    cpf_limpo = re.split(r"[.-]", CPF)

    #Adiciona cada número na lista numeros
    for conjunto in cpf_limpo:
        for numero in conjunto:
            numeros.append(numero)

    #Verificador do primeiro dígito verificador
    peso = 10
    for num in numeros[:9]:
        numeros_multiplicados.append(int(num)*peso)
        peso -= 1
    digito_01 =  11- (sum(numeros_multiplicados) % 11 )
    if digito_01 >= 10:
        digito_01 = 0

    #Verificador do segundo dígito verificador
    numeros_multiplicados.clear()
    peso = 11
    for num in numeros[:10]:
        numeros_multiplicados.append(int(num)*peso)
        peso -= 1
    digito_02 = 11 - (sum(numeros_multiplicados) % 11)
    if digito_02 >= 10:
        digito_02 = 0
    
    #Verificação dos ultimos
    ultimos_numeros = [str(digito_01),str(digito_02)]
    if ultimos_numeros == numeros[9:12]:
        return True
    else:
        return False

def ver_cpf(cpf):
    variavel = ""
    for i,digito in enumerate(cpf):
        if type(digito) == list:
            for numero in digito:
                variavel += str(numero)
        elif i == 5:
            variavel += "-"
        else:
            variavel += "."
    return variavel
                
def digitar_cpf():
    cpf = [["_","_","_"], "." , ["_","_","_"], "." , ["_","_","_"], "-" , ["_","_"]]

    for i,digito in enumerate(cpf):
        if type(digito) == list:
            c = 0
            contador = 3
            if i == 6:
                contador = 2
            for numero in range(contador):
                while True:
                    try:
                        print(f"Pré-Visualização: {ver_cpf(cpf)}")
                        cadastro_numero = int(input("Digite um número para cadastrar: "))
                    except ValueError:
                        print("ERRO! Digite apenas números")
                        continue
                    else:
                        lista = [num for num in str(cadastro_numero)]
                        if len(lista) > 1:
                            print("ERRO! Digite apenas números válidos")
                            continue
                        else:
                            break
                cpf[i].remove("_")
                cpf[i].insert(c,cadastro_numero) #AQUI
                c += 1
    return cpf