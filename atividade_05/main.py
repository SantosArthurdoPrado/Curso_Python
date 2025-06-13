''' 
# TODO - atividade: Crie um programa que receba do usuário os seguintes
dados:
 - Nome
 - CPF
 - Data de Nascimento
 - E-mail
 - Gênero
 - Telefone
 - Endereço
 - Altura em metros
 - Peso em Kg
 - Tipo Sanguínio
 Ao final, o programa exibe esses dados.
 # NOTE - deve ser feito utilizando o conceito de dicionário.
'''
dados = {
    'Nome': '',
    'CPF' : '',
    'Data_de_Nascimento':'',
    'email':'',
    'Genero':'',
    'Telefone':'',
    'Endereco':'',
    'Altura_em_metros':'',
    'Peso_em_Kg':'',
    'Tipo_Sanguinio':'',
}
try: 
    dados['Nome'] = input("Informe o Nome: ")
    dados['CPF'] = input("Informe o CPF: ")
    dados['Data_de_Nascimento'] = input("Informe a Data de Nascimento: ")
    dados['email'] = input("Informe o E-mail: ")
    dados['Genero'] = input("Informe o Gênero: ")
    dados['Telefone'] = input("Informe o Telefone: ")
    dados['Endereco'] = input("Informe o Endereço: ")
    dados['Altura_em_metros'] = float(input("Informe a Altura em metros: ").replace(',','.'))
    dados['Peso_em_Kg'] = float(input("Informe o Peso em Kg: ").replace(',','.'))
    dados['Tipo_Sanguinio'] = input("Informe o Tipo Sanguínio ")
except Exception as e:
    print(f"Não foi possível inserir o novo valor. {e}.")
finally:
     print(f"Nome: {dados.get('Nome')}")
     print(f"CPF: {dados.get('CPF')}")
     print(f"Data de Nascimento: {dados.get('Data_de_Nascimento')}")
     print(f"E-mail: {dados.get('email')}")
     print(f"Gênero: {dados.get('Genero')}")
     print(f"Telefone: {dados.get('Telefone')}")
     print(f"Endereço: {dados.get('Endereco')}")
     print(f"Altura em metros: {dados.get('Altura_em_metros')}")
     print(f"Peso em Kg: {dados.get('Peso_em_Kg')}")
     print(f"Tipo Sanguinio: {dados.get('Tipo_Sanguinio')}")
