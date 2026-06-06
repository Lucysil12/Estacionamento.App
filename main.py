from cliente import *
from veiculo import *
from vaga import *
from ticket import * 
from setor import *
from conexao import conectar 


def menu_clientes():

    while True:

        print("\n===== CLIENTES =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":

            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")

            cadastrar_cliente(nome, cpf, telefone)

        elif op == "2":

            listar_clientes()

        elif op == "3":

            id_cliente = int(input("ID Cliente: "))
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")

            atualizar_cliente(
                id_cliente,
                nome,
                telefone
            )

        elif op == "4":

            id_cliente = int(input("ID Cliente: "))

            excluir_cliente(id_cliente)

        elif op == "0":

            break

        else:

            print("Opção inválida!")


def menu_veiculos():

    while True:

        print("\n===== VEÍCULOS =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":

            placa = input("Placa: ")
            modelo = input("Modelo: ")
            cor = input("Cor: ")
            id_cliente = int(input("ID Cliente: "))
            id_categoria = int(input("ID Categoria: "))

            cadastrar_veiculo(
                placa,
                modelo,
                cor,
                id_cliente,
                id_categoria
            )

        elif op == "2":

            listar_veiculos()

        elif op == "3":

            id_veiculo = int(input("ID Veículo: "))
            cor = input("Nova cor: ")

            atualizar_veiculo(
                id_veiculo,
                cor
            )

        elif op == "4":

            id_veiculo = int(input("ID Veículo: "))

            excluir_veiculo(id_veiculo)

        elif op == "0":

            break

        else:

            print("Opção inválida!")


def menu_vagas():

    while True:

        print("\n===== VAGAS =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Listar Livres")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Verificar Disponibilidade")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":

            numero = input("Número da vaga: ")

            conexao = conectar()
            cursor = conexao.cursor()
            
            cursor.execute("""
            SELECT *
            FROM Setor
            """)
            
            print("\nSETORES DISPONÍVEIS:")
            
            for setor in cursor.fetchall():
                print(setor)
            
            cursor.close()
            conexao.close()
            
            id_setor = int(input("\nID Setor: "))
            
            cadastrar_vaga(
                numero,
                id_setor
            )

        elif op == "2":

            listar_vagas()

        elif op == "3":

            listar_vagas_livres()

        elif op == "4":

            id_vaga = int(input("ID Vaga: "))
            status = input("Status (Livre/Ocupada/Manutenção): ")

            atualizar_vaga(
                id_vaga,
                status
            )

        elif op == "5":

            id_vaga = int(input("ID Vaga: "))

            excluir_vaga(id_vaga)

        elif op == "6":

            id_vaga = int(input("ID Vaga: "))

            verificar_disponibilidade(id_vaga)

        elif op == "0":

            break

        else:

            print("Opção inválida!")


def menu_tickets():

    while True:

        print("\n===== TICKETS =====")
        print("1 - Registrar Entrada")
        print("2 - Registrar Saída")
        print("3 - Listar Todos")
        print("4 - Tickets Abertos")
        print("5 - Atualizar")
        print("6 - Excluir")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":

            id_veiculo = int(input("ID Veículo: "))
            id_vaga = int(input("ID Vaga: "))

            registrar_entrada(
                id_veiculo,
                id_vaga
            )

        elif op == "2":

            id_ticket = int(input("ID Ticket: "))
            forma = input(
                "Forma Pagamento (Pix, Cartão ou Dinheiro): "
            )

            registrar_saida(
                id_ticket,
                forma
            )

        elif op == "3":

            listar_tickets()

        elif op == "4":

            listar_tickets_abertos()

        elif op == "5":

            id_ticket = int(input("ID Ticket: "))
            forma = input("Nova forma de pagamento: ")

            atualizar_ticket(
                id_ticket,
                forma
            )

        elif op == "6":

            id_ticket = int(input("ID Ticket: "))

            excluir_ticket(id_ticket)

        elif op == "0":

            break

        else:

            print("Opção inválida!")
def menu_setores():
    while True:
        print("\n===== SETORES =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")

        op = input("Escolha: ")
        if op == "1":

            nome_setor = input("Nome do setor: ")
            tipo_setor = input("Tipo do setor: ")
            cadastrar_setor(
                nome_setor,
                tipo_setor
            )
        elif op == "2":

            listar_setores()

        elif op == "3":
             id_setor = int(input("ID Setor: "))
             nome_setor = input("Novo nome do setor: ")
             tipo_setor = input("Novo tipo do setor: ")

             atualizar_setor(
                id_setor,
                nome_setor,
                tipo_setor
            )
        elif op == "4":

            id_setor = int(input("ID Setor: "))

            excluir_setor(id_setor)

        elif op == "0":
            break

        else:

            print("Opção inválida!")

def menu_relatorios():

    while True:

        print("\n===== RELATÓRIOS =====")
        print("1 - Vagas Livres")
        print("2 - Tickets Abertos")
        print("3 - Faturamento")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":

            listar_vagas_livres()

        elif op == "2":

            listar_tickets_abertos()

        elif op == "3":

            listar_faturamento()

        elif op == "0":

            break

        else:

            print("Opção inválida!")


while True:

    print("\n===================================")
    print("     SISTEMA DE ESTACIONAMENTO")
    print("===================================")
    print("1 - Clientes")
    print("2 - Veículos")
    print("3 - Vagas")
    print("4 - Tickets")
    print("5 - Setores")
    print("6 - Relatórios")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        menu_clientes()

    elif opcao == "2":

        menu_veiculos()

    elif opcao == "3":

        menu_vagas()

    elif opcao == "4":

        menu_tickets()
    elif opcao == "5":

       menu_setores()

    elif opcao == "6":

       menu_relatorios()

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida!")


