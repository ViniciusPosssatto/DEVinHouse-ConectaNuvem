create if not exists schema escola_idiomas;

create table if not exists escola_idiomas.aluno(
	matricula SERIAL primary key,
	nome VARCHAR(200) not null,
	numero INT,
	bairro VARCHAR(30) not null,
	cidade VARCHAR(30) not null,
	estado VARCHAR(30) not null,
	cep VARCHAR(30) not null
);

create table if not exists escola_idiomas.turma(
	cod_turma SERIAL primary key,
	horario VARCHAR(5)
);

create table if not exists escola_idiomas.matricula(
	cod_matricula SERIAL primary key,
	qtd_faltas INT,
	nota1 FLOAT,
	nota2 FLOAT,
	nota3 FLOAT
);

create table if not exists escola_idiomas.titulacao(
	cod_titulacao SERIAL primary key,
	descricao_titulo VARCHAR(30) not null
);

create table if not exists escola_idiomas.professor(
	salario FLOAT not null,
	data_nascimento DATE not null,
	matricula SERIAL primary key,
	nome VARCHAR(200) not null
);

create table if not exists escola_idiomas.disciplina(
	cod_disciplina SERIAL primary key,
	nome_disciplina VARCHAR(30) not null
);

/*
Selecionar a tabela especifica 
select * from escola_idiomas.matricula;
*/

/*
ALTER STRUCTURE
*/

select * from escola_idiomas.matricula;

-- REMOVE UMA COLUNA
alter table escola_idiomas.matricula drop column nota3;

-- ADICIONA UMA COLUNA
alter table escola_idiomas.matricula
add column media float
generated always as ((nota1+nota2)/2) stored;

insert into escola_idiomas.matricula(qtd_faltas, nota1, nota2)
values(1, 4, 8)
insert into escola_idiomas.matricula(qtd_faltas, nota1, nota2)
values(3, 7, 3.7)
insert into escola_idiomas.matricula(qtd_faltas, nota1, nota2)
values(2, 8, 7.7)

-- ALTERA O TIPO DE DADO de uma coluna
alter table escola_idiomas.matricula alter column media type varchar(40);

-- RENOMEAR COLUNA
alter table escola_idiomas.matricula rename column media to nota_final;