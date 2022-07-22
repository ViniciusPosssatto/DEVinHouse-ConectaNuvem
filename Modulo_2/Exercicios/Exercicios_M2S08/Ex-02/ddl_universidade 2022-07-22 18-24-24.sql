-- departamentos
INSERT INTO universidade.departamentos(cod_dpto, nome_dpto) 
VALUES (1, 'Consulado')
INSERT INTO universidade.departamentos(cod_dpto, nome_dpto) 
VALUES (2, 'serviços gerais')
INSERT INTO universidade.departamentos(cod_dpto, nome_dpto) 
VALUES (3, 'PROEX')
INSERT INTO universidade.departamentos(cod_dpto, nome_dpto) 
VALUES (4, 'PRAE')
INSERT INTO universidade.departamentos(cod_dpto, nome_dpto) 
VALUES (5, 'Professores')

SELECT * from universidade.departamentos;

-- CURSOS
INSERT INTO universidade.cursos(cod_curso, nome_curso, cod_dpto)
VALUES (1, 'Ciencias', 5)
INSERT INTO universidade.cursos(cod_curso, nome_curso, cod_dpto)
VALUES (2, 'Alguma coisa', 5)
INSERT INTO universidade.cursos(cod_curso, nome_curso, cod_dpto)
VALUES (3, 'Outra coisa', 5)
INSERT INTO universidade.cursos(cod_curso, nome_curso, cod_dpto)
VALUES (3, 'Infraestrutura', 5)
INSERT INTO universidade.cursos(cod_curso, nome_curso, cod_dpto)
VALUES (4, 'Administração', 5)

SELECT * from universidade.cursos;

--ALUNOS
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (111, 'Packt jonson', '1950-04-14', 2, False)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (112, 'Springer boot', '1950-09-20', 1, False)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (114, 'Beto Oxford', '1950-09-18', 4, False)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (113, 'Jonh Springer', '1950-05-05', 2, True)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (115, 'Marcio IT', '1950-03-12', 3, True)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (116, 'March zion', '1950-04-14', 2, False)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (117, 'Grey boot', '1950-09-20', 1, False)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (118, 'Beto Richard', '1950-09-18', 4, False)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (119, 'Jonh Snow', '1950-05-05', 2, True)
INSERT INTO universidade.alunos(mat_aluno, nome, data_entrada, cod_curso, cotista) 
VALUES (120, 'Marcs DDD', '1950-03-12', 3, True)

SELECT * from universidade.alunos;

-- DISCIPLINAS
INSERT INTO universidade.disciplinas(cod_disc, nome_disc, carga_horaria)
VALUES (1, 'Matematica', 60)
INSERT INTO universidade.disciplinas(cod_disc, nome_disc, carga_horaria)
VALUES (2, 'português', 30)
INSERT INTO universidade.disciplinas(cod_disc, nome_disc, carga_horaria)
VALUES (3, 'quimica', 25)
INSERT INTO universidade.disciplinas(cod_disc, nome_disc, carga_horaria)
VALUES (4, 'filosofia', 44)
INSERT INTO universidade.disciplinas(cod_disc, nome_disc, carga_horaria)
VALUES (5, 'biologia', 12)

-- MATRICULAS
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, status)
VALUES (1, 112, 2, 6, 'A')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, status)
VALUES (2, 113, 2, 6.8, 'A')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, faltas, status)
VALUES (3, 113, 3, 9.76, 3, 'A')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, status)
VALUES (4, 115, 4, 5.5, 'R')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, status)
VALUES (5, 111, 4, 3.75, 'R')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, faltas, status)
VALUES (6, 113, 3, 9.1, 2, 'A')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, faltas, status)
VALUES (7, 113, 3, 8.76, 5, 'A')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, faltas, status)
VALUES (8, 113, 3, 2.76, 4, 'R')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, faltas, status)
VALUES (9, 113, 3, 5.76, 8,'R')
INSERT INTO universidade.matriculas(semestre, mat_aluno, cod_disc, nota, faltas, status)
VALUES (10, 113, 3, 6.1, 11, 'A')


SELECT * from universidade.matriculas;

-- CURSOS
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (1, 1, 2)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (2, 3, 2)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (3, 3, 2)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (4, 2, 2)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (2, 1, 3)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (1, 1, 2)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (2, 3, 4)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (3, 3, 2)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (2, 2, 5)
INSERT INTO universidade.matrizes_cursos(cod_curso, cod_disc, periodo)
VALUES (2, 1, 3)

SELECT * from universidade.matrizes_cursos;