from conexao import conectar
from mysql.connector import Error


def cadastrar_setor(nome_setor, tipo_setor):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO Setor
        (nome_setor, tipo_setor)
        VALUES (%s,%s)
        """

        cursor.execute(
            sql,
            (
                nome_setor,
                tipo_setor
            )
        )

        conexao.commit()

        print("Setor cadastrado com sucesso!")

    except Error as erro:

        print(f"Erro ao cadastrar setor: {erro}")

    finally:

        cursor.close()
        conexao.close()


def listar_setores():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Setor")

    setores = cursor.fetchall()

    if len(setores) == 0:
        print("Nenhum setor cadastrado.")
    else:
        for setor in setores:
            print(setor)

    cursor.close()
    conexao.close()


def atualizar_setor(id_setor, nome_setor, tipo_setor):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Setor
    SET nome_setor=%s,
        tipo_setor=%s
    WHERE id_setor=%s
    """

    cursor.execute(
        sql,
        (
            nome_setor,
            tipo_setor,
            id_setor
        )
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Setor atualizado com sucesso!")
    else:
        print("Setor não encontrado.")

    cursor.close()
    conexao.close()


def excluir_setor(id_setor):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM Setor WHERE id_setor=%s",
            (id_setor,)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Setor removido com sucesso!")
        else:
            print("Setor não encontrado.")

    except Error:

        print(
            "Não é possível excluir este setor "
            "porque existem vagas vinculadas."
        )

    finally:

        cursor.close()
        conexao.close()