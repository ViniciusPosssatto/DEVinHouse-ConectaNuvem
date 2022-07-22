CREATE SCHEMA if not exists locadora;

CREATE TABLE if not exists locadora.ator(
  id_ator SERIAl PRIMARY KEY,
  nome varchar(200) NOT NULL,
  nome_artistico varchar(200) NOT NULL
);

CREATE TABLE if not exists locadora.historico(
  FK_id_filme int not null,
  FK_id_ator int not null
);

CREATE TABLE if not exists locadora.filme(
  nome varchar(200) NOT NULL,
  id_filme SERIAL PRIMARY KEY
  fk_id_ator int not null
  foreign key (fk_id_ator) references locadora.ator (id_ator)
);

CREATE TABLE if not exists locadora.categoria(
  id_categoria SERIAL PRIMARY KEY,
  nome varchar(200) NOT NULL
);