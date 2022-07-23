-- SELECT GERAL
SELECT * from universidade.departamentos;
SELECT * from universidade.cursos;
SELECT * from universidade.alunos;
SELECT * from universidade.disciplinas;
SELECT * from universidade.matriculas;

-- CURSOS
SELECT * from universidade.cursos;

--ALUNOS
SELECT nome, data_entrada from universidade.alunos a
where EXTRACT(YEAR from a.data_entrada)=1950
SELECT nome, data_entrada from universidade.alunos a
where EXTRACT(month from a.data_entrada)=04

-- DISCIPLINAS
SELECT * from universidade.disciplinas
WHERE carga_horaria >= 30

SELECT nome_disc as "Disciplina", carga_horaria as "Carga horaria" from universidade.disciplinas
WHERE carga_horaria > 30

-- MATRICULAS
SELECT mat_aluno, status from universidade.matriculas m
where m.status='R'

SELECT * from universidade.matriculas m
inner join universidade.alunos a on m.mat_aluno = a.mat_aluno
where m.status='R'
order by nota