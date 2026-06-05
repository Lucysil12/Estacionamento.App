from conexao import conectar
from mysql.connector import Error


def cadastrar_veiculo(
    placa,
    modelo,
    cor,
    id_cliente,
    id_categoria
):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO Veiculo
        (placa, modelo, cor, id_cliente, id_categoria)
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (
                placa,
                modelo,
                cor,
                id_cliente,
                id_categoria
            )
        )

        conexao.commit()

        print("Veículo cadastrado com sucesso!")

    except Error as erro:

        print(f"Erro ao cadastrar veículo: {erro}")

    finally:

        cursor.close()
        conexao.close()


def listar_veiculos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM vw_veiculos_clientes
    """)

    veiculos = cursor.fetchall()

    if len(veiculos) == 0:
        print("Nenhum veículo cadastrado.")
    else:
        for veiculo in veiculos:
            print(veiculo)

    cursor.close()
    conexao.close()


def atualizar_veiculo(id_veiculo, cor):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Veiculo
    SET cor=%s
    WHERE id_veiculo=%s
    """

    cursor.execute(
        sql,
        (
            cor,
            id_veiculo
        )
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Veículo atualizado com sucesso!")
    else:
        print("Veículo não encontrado.")

    cursor.close()
    conexao.close()


def excluir_veiculo(id_veiculo):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM Veiculo WHERE id_veiculo=%s",
            (id_veiculo,)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Veículo removido com sucesso!")
        else:
            print("Veículo não encontrado.")

    except Error:

        print(
            "Não é possível excluir este veículo "
            "porque ele possui tickets vinculados."
        )

    finally:

        cursor.close()
        conexao.close()