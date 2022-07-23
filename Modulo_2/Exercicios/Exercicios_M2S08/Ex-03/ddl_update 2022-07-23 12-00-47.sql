-- departamentos
UPDATE universidade.departamentos
SET nome_dpto='Dpt das cove'
where cod_dpto=1
UPDATE universidade.departamentos
SET nome_dpto='Alunos'
where cod_dpto=4

SELECT * from universidade.departamentos;

-- CURSOS
UPDATE universidade.cursos
SET nome_curso='Ciencias agrarias'
where cod_curso=2
UPDATE universidade.cursos
SET nome_curso='Engenharia'
where cod_curso=3

SELECT * from universidade.cursos;

--ALUNOS
UPDATE universidade.alunos
SET nome='Jack springer'
where mat_aluno=112
UPDATE universidade.alunos
SET nome='Marcio Santos', data_entrada='1951-08-09'
where mat_aluno=115

SELECT * from universidade.alunos;

-- DISCIPLINAS
UPDATE universidade.disciplinas
SET nome_disc='Filosofia'
where cod_disc=4
UPDATE universidade.disciplinas
SET nome_disc='Química'
where cod_disc=3

SELECT * from universidade.disciplinas;

-- MATRICULAS
UPDATE universidade.matriculas
SET nota='7.77'
WHERE semestre=5
UPDATE universidade.matriculas
SET status='A'
WHERE semestre=5

SELECT * from universidade.matriculas;