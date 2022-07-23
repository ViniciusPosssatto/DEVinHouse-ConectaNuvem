SELECT * from university.matrizes_cursos;
SELECT * from university.alunos;
SELECT * from university.disciplinas;
SELECT * from university.cursos;
SELECT * from university.matriculas;
SELECT * from university.departamentos;


--Fazer a contagem de aluno por curso e ordenar do maior para menor
SELECT c.nom_curso as "Curso", count(1) as "Contagem"
from university.alunos a
inner join university.cursos c on a.cod_curso = c.cod_curso
group by c.nom_curso
order by "Contagem" desc;

--Fazer a soma de faltas e ordenar decrescente e colocar o nome das disciplinas
SELECT nome_disc as "DISCIPLINA", sum(m.faltas) as "TOTAL_FALTAS"
from university.matriculas m
inner join university.disciplinas d on m.cod_disc = d.cod_disc
group by nome_disc
order by "TOTAL_FALTAS" desc;