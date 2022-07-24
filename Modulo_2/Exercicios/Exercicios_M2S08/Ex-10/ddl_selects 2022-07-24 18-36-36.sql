SELECT * from university.matrizes_cursos;
SELECT * from university.alunos;
SELECT * from university.disciplinas;
SELECT * from university.cursos;
SELECT * from university.matriculas;
SELECT * from university.departamentos;


--Fazer a contagem de alunos cotistas reprovados em disciplinas
SELECT d.nome_disc as "Disciplina", count(1) as "Contagem"
from university.matriculas m
inner join university.alunos a on m.mat_alu = a.mat_alu
inner join university.disciplinas d on m.cod_disc = d.cod_disc
where m.status='R' and a.cotistas='S'
group by d.nome_disc
order by "Contagem" desc;

--Listar o número total de matrículas de alunos cotistas em disciplinas
SELECT d.nome_disc as "Disciplina", count(1) as "Contagem"
from university.matriculas m
inner join university.alunos a on m.mat_alu = a.mat_alu
inner join university.disciplinas d on m.cod_disc = d.cod_disc
where a.cotistas='S'
group by d.nome_disc
order by "Contagem" desc;

-- usando limit
SELECT * from university.matriculas
limit 10;

-- usando AVG
SELECT avg(nota)
from university.matriculas
where status='R'

SELECT mat.alu, roud(avg(nota)) as "MEDIA_FINAL"
from university.matriculas
group by mat_alu
order by "MEDIA_FINAL" desc
limit 3;

-- usando DISCTINCT
SELECT DISTINCT mat_alu from university.matriculas;

-- usando LIKE
SELECT * from university.cursos
where nom_curso LIKE '%Manhã';

-- usando inner join e GROUP e ORDER
SELECT c.nom_curso as "Nome_Curso", count(1) as "CONTAGEM"
from university.alunos a
inner join university.cursos c on a.cod_curso = c.cod_curso
group by c.nom_curso
order by "CONTAGEM" desc;

-- usando soma SUM
SELECT d.nome_disc as "DISCIPLINA", sum(m.faltas) as "TOTAL_FALTAS"
from university.matriculas m
inner join university.disciplinas d on m.cod_disc = d.cod_disc
group by d.nome_disc
order by "TOTAL_FALTAS" desc;

-- select com 3 condições
SELECT * from university.alunos a
inner join university.matriculas m on a.mat_alu = m.mat_alu
where a.cotista='S' and m.faltas < 5 and EXTRACT(YEAR from a.dat_entrada) = 2005
order by m.faltas desc;