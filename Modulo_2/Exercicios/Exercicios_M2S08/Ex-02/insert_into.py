from re import T
import psycopg2


lista_aluno = ['mat_aluno', 'nome', 'data_entrada', 'cod_curso', 'cotista']


def insert_aluno():
    try:
        connection = psycopg2.connect(user="admin", password="12345678", host="172.22.240.1", port="5432", database="admin")
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO universidade.aluno(mat_aluno, nome, data_entrada, cod_curso, cotista) VALUES (%s,%s,%s,%s,%s)"""

        record_to_insert = [(111, 'Packt jonson', '1950-04-14', 1, False), (112, 'Springer boot', '1950-09-20', 1, False),
                            (113, 'Jonh Springer', '1950-05-05', 2, True), (114, 'Beto Oxford', '1950-09-18', 1, False),
                            (115, 'Marcio IT', '1950-03-12', 3, True)]
        for i in record_to_insert:
            cursor.execute(postgres_insert_query, i)

            connection.commit()
            count = cursor.rowcount
        print(count, "Record inserted successfully into universidade table alunos")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into universidade table alunos", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insert_dpto():
    try:
        connection = psycopg2.connect(user="admin", password="12345678", host="172.22.240.1", port="5432", database="admin")
        cursor = connection.cursor()

        postgres_insert_query = "INSERT INTO universidade.departamentos(cod_dpto, nome_dpto) VALUES (%s)"

        record_to_insert = [(1, 'Consulado'), (2, 'serviços gerais'), (3, 'PROEX'), (4, 'PRAE'), (5, 'Professores')]
        for i in record_to_insert:
            cursor.execute(postgres_insert_query, i)

            connection.commit()
            count = cursor.rowcount
        print(count, "Record inserted successfully into universidade table dpto")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into universidade table dpto", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

insert_dpto()
# insert_aluno()