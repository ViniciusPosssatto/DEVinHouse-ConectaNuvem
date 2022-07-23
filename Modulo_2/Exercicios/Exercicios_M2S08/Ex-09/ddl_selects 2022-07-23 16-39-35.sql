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