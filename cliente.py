from conexao import conectar
from mysql.connector import Error


def cadastrar_cliente(nome, cpf, telefone):

    conexao = conectar()
    cursor = conexao.cursor()

    try:

        cursor.callproc(
            "sp_cadastrar_cliente",
            (
                nome,
                cpf,
                telefone
            )
        )

        conexao.commit()

        print("Cliente cadastrado!")

    except Error as erro:

        print(f"Erro ao cadastrar cliente: {erro}")

    finally:

        cursor.close()
        conexao.close()


def listar_clientes():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Cliente")

    clientes = cursor.fetchall()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(cliente)

    cursor.close()
    conexao.close()


def atualizar_cliente(id_cliente, nome, telefone):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Cliente
    SET nome=%s, telefone=%s
    WHERE id_cliente=%s
    """

    cursor.execute(
        sql,
        (
            nome,
            telefone,
            id_cliente
        )
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Cliente atualizado!")
    else:
        print("Cliente não encontrado.")

    cursor.close()
    conexao.close()


def excluir_cliente(id_cliente):

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM Cliente WHERE id_cliente=%s",
            (id_cliente,)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado.")

    except Error:

        print(
            "Não é possível excluir este cliente "
            "porque ele possui veículos cadastrados."
        )

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()