-- SCHEMA: universidade

-- DROP SCHEMA IF EXISTS universidade ;

CREATE SCHEMA IF NOT EXISTS universidade
	
CREATE TABLE IF NOT EXISTS universidade.departamentos(
	cod_dpto int PRIMARY KEY,
	nome_dpto varchar(50) not null
);

CREATE TABLE IF NOT EXISTS universidade.cursos(
	cod_curso int PRIMARY KEY,
	nome_curso varchar(100),
	cod_dpto int not null,
	CONSTRAINT FK_DEPARTAMENTOS_cod_dpto FOREIGN KEY (cod_dpto) REFERENCES universidade.departamentos (cod_dpto)
);

CREATE TABLE IF NOT EXISTS universidade.alunos(
	mat_aluno int PRIMARY KEY,
	nome varchar(100) not null,
	data_entrada date not null,
	cod_curso int not null,
	cotista boolean not null,
	CONSTRAINT FK_CURSOS_cod_curso FOREIGN KEY (cod_curso) REFERENCES universidade.cursos (cod_curso)
);

CREATE TABLE IF NOT EXISTS universidade.disciplinas(
	cod_disc int PRIMARY KEY,
	nome_disc varchar(50) not null,
	carga_horaria int not null
);

CREATE TABLE IF NOT EXISTS universidade.matriculas(
	semestre int PRIMARY KEY,
	mat_aluno int not null,
	cod_disc int not null,
	nota decimal(5,2),
	faltas int,
	status varchar(1) not null,
	CONSTRAINT FK_ALUNOS_mat_aluno FOREIGN KEY (mat_aluno) REFERENCES universidade.alunos (mat_aluno),
	CONSTRAINT FK_DISCIPLINA_cod_disc FOREIGN KEY (cod_disc) REFERENCES universidade.disciplinas (cod_disc)
);

CREATE TABLE IF NOT EXISTS universidade.matrizes_cursos(
	cod_curso int not null,
	cod_disc int not null,
	periodo int not null,
	CONSTRAINT FK_CURSOS_cod_curso FOREIGN KEY (cod_curso) REFERENCES universidade.cursos (cod_curso),
	CONSTRAINT FK_DISCIPLINAS_cod_disc FOREIGN KEY (cod_disc) REFERENCES universidade.disciplinas (cod_disc)
);