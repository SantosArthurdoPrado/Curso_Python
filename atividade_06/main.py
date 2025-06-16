"""
# TODO - Atividade: Crie um Programa com um dicionário chamado 'usuário',
com o seguinte menu:
- Cadastrar nova chave
- Exibir  dados do usuário
- Alterar valor da chave
- Excluir chave 
- Sair do Programa
"""
import os
usuario = {
    'nome': "",
    'idade': "",
    'telefone': "",
    'nome_do_pai': "",
    'nome_da_mae': "",
    'nome_do_cachorro': "",
    'comida_favorita': "",
    'tempo_de_sono': "",
    'nome_do_melhor_amigo': ""

}
while True:
    print(f"{'-'*30} MENU {'-'*30}")
    print("1 - Cadastrar nova chave")
    print("2 - Exibir  dados do usuário")
    print("3 - Alterar valor da chave")
    print("4 - Excluir chave")
    print("5 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    os.system("cls")
    match opcao:
        case "1":
            chave = input("Informe o nome da chave: ").lower().strip()
            try:
                if chave in usuario:
                    usuario[chave] = input("Informe o novo valor: ").strip()
                    os.system("cls")
                    print(f"Chave alterada com sucesso!")
                else:
                    os.system("cls")
                    print("Não foi possível encontrar a chave requisitada.")
            except Exception as e:
                print(f"Não foi possível alterar. {e}.")
                continue
            finally:
                continue
        case "2":
            for chave in usuario:
             print(f"{chave.capitalize()}: {usuario.get(chave)}.")
             continue
        case "3":
            chave = input("Informe o nome da chave: ").lower().strip()
            try:
                if chave in usuario:
                    usuario[chave] = input("Informe o novo valor: ").strip()
                    print(f"Chave alterada com sucesso!")
                else:
                    print("Não foi possível encontrar a chave requisitada.")
            except Exception as e:
                print(f"Não foi possível alterar. {e}.")
                continue
            finally:
                continue
        case "4":
            chave = input("Informe o nome da chave que deseja deletar: ").lower().strip()
            try:
                if chave in usuario:
                    del usuario[chave]
                    print("Chave excluída com sucesso!")
                else:
                    print("Não foi possível achar a chave.")
            except Exception as e:
                    print(f"Não foi possível deletar a chave. {e}.")
            finally:
                continue
        case "5":
            print("Tchau! Tchau! :o ")
            break
        case _:
            continue
