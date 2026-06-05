from conexao import conectar
from mysql.connector import Error


def registrar_entrada(id_veiculo, id_vaga):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.callproc(
            "sp_registrar_entrada",
            (
                id_veiculo,
                id_vaga
            )
        )

        conexao.commit()

        print("Entrada registrada com sucesso!")

    except Error as erro:

        print(f"Erro ao registrar entrada: {erro}")

    finally:

        cursor.close()
        conexao.close()


def registrar_saida(id_ticket, forma_pagamento):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.callproc(
            "sp_registrar_saida",
            (
                id_ticket,
                forma_pagamento
            )
        )

        conexao.commit()

        print("Saída registrada com sucesso!")

    except Error as erro:

        print(f"Erro ao registrar saída: {erro}")

    finally:

        cursor.close()
        conexao.close()


def listar_tickets():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM Ticket
    """)

    tickets = cursor.fetchall()
    if len(tickets) == 0:
            print("Não existem tickets abertos.")
    else:
            print("\n===== LISTA DE TICKETS =====")
    for ticket in tickets:
            print("\n--------------------------")
            print(f"ID Ticket: {ticket[0]}")
            print(f"Entrada: {ticket[1]}")
            print(f"Saída: {ticket[2]}")
            print(f"Valor Pago: R$ {ticket[3]}")
            print(f"Pagamento: {ticket[4]}")
            print(f"Status: {ticket[5]}")
            print(f"ID Veículo: {ticket[6]}")
            print(f"ID Vaga: {ticket[7]}")

    cursor.close()
    conexao.close()


def listar_tickets_abertos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM Ticket
    WHERE status_ticket = 'Aberto'
    """)

    tickets = cursor.fetchall()

    if len(tickets) == 0:
        print("Não existem tickets abertos.")
    else:
        print("\n===== LISTA DE TICKETS =====")
        for ticket in tickets:
           print("\n--------------------------")
           print(f"ID Ticket: {ticket[0]}")
           print(f"Data Entrada: {ticket[1]}")
           print(f"Status: {ticket[5]}")
           print(f"ID Veículo: {ticket[6]}")
           print(f"ID Vaga: {ticket[7]}")
    cursor.close()
    conexao.close()


def atualizar_ticket(id_ticket, forma_pagamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Ticket
    SET forma_pagamento=%s
    WHERE id_ticket=%s
    """

    cursor.execute(
        sql,
        (
            forma_pagamento,
            id_ticket
        )
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Ticket atualizado com sucesso!")
    else:
        print("Ticket não encontrado.")

    cursor.close()
    conexao.close()


def excluir_ticket(id_ticket):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM Ticket WHERE id_ticket=%s",
            (id_ticket,)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Ticket removido com sucesso!")
        else:
            print("Ticket não encontrado.")

    except Error as erro:

        print(f"Erro ao remover ticket: {erro}")

    finally:

        cursor.close()
        conexao.close()


def listar_faturamento():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM vw_faturamento
    """)

    faturamentos = cursor.fetchall()

    if len(faturamentos) == 0:
        print("Nenhum faturamento encontrado.")
    else:

        print("\n===== RELATÓRIO DE FATURAMENTO =====")

        for data, total_tickets, valor in faturamentos:

            print("\n-------------------------")
            print(f"Data: {data}")
            print(f"Tickets Finalizados: {total_tickets}")
            print(f"Valor Registrado: R$ {valor}")

    cursor.close()
    conexao.close()