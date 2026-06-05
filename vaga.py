from conexao import conectar
from mysql.connector import Error


def cadastrar_vaga(numero, id_setor):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO Vaga
        (numero, status_vaga, id_setor)
        VALUES (%s,'Livre',%s)
        """

        cursor.execute(sql, (numero, id_setor))

        conexao.commit()

        print("Vaga cadastrada com sucesso!")

    except Error as erro:

        print(f"Erro ao cadastrar vaga: {erro}")

    finally:

        cursor.close()
        conexao.close()


def listar_vagas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Vaga")

    vagas = cursor.fetchall()

    if len(vagas) == 0:
        print("Nenhuma vaga cadastrada.")
    else:
        for vaga in vagas:
            print(vaga)

    cursor.close()
    conexao.close()


def listar_vagas_livres():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM vw_vagas_livres
    """)

    vagas = cursor.fetchall()

    if len(vagas) == 0:
        print("Não existem vagas livres.")
    else:
        for vaga in vagas:
            print(vaga)

    cursor.close()
    conexao.close()


def atualizar_vaga(id_vaga, status):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Vaga
    SET status_vaga=%s
    WHERE id_vaga=%s
    """

    cursor.execute(
        sql,
        (
            status,
            id_vaga
        )
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Vaga atualizada com sucesso!")
    else:
        print("Vaga não encontrada.")

    cursor.close()
    conexao.close()


def excluir_vaga(id_vaga):

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM Vaga WHERE id_vaga=%s",
            (id_vaga,)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Vaga removida com sucesso!")
        else:
            print("Vaga não encontrada.")

    except Error:

        print(
            "Não é possível excluir esta vaga "
            "porque ela possui tickets vinculados."
        )

    finally:

        cursor.close()
        conexao.close()


def verificar_disponibilidade(id_vaga):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT status_vaga
    FROM Vaga
    WHERE id_vaga=%s
    """, (id_vaga,))

    resultado = cursor.fetchone()

    if resultado:
        print(f"Status da vaga: {resultado[0]}")
    else:
        print("Vaga não encontrada.")

    cursor.close()
    conexao.close()