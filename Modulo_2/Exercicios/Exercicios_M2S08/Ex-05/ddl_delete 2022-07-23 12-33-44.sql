-- DROP GERAL
DROP schema universidade cascade;

-- CURSOS
 universidade.cursos;

--ALUNOS
DELETE from universidade.alunos a
where cotista=false and EXTRACT(month from a.data_entrada)=03

-- DISCIPLINAS
DELETE from universidade.disciplinas
WHERE carga_horaria <= 20

-- MATRICULAS
DELETE from universidade.matriculas m
where m.status='R'