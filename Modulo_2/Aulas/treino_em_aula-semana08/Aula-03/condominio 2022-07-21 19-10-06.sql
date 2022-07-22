CREATE SCHEMA if not exists gestora_condominio;

CREATE TABLE if not exists gestora_condominio.edificio(
  id_edificio int primary key,
  endereco varchar(50) not null,
  data_construcao date,
  data_ultima_vistoria date
);

CREATE TABLE if not exists gestora_condominio.apartamento(
  area float not null,
  apt_numero int primary key
);

CREATE TABLE if not exists gestora_condominio.proprietario(
  fk_apartamento_apt_numero int foreign key,
  fk_pessoa_cpf int foreign key
);

CREATE TABLE if not exists gestora_condominio.pessoa(
  data_nascimento date not null,
  cpf int primary key,
  sexo varchar(1),
  nome varchar(200) not null
);

-- VISUALIZAÇÃO das colunas
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'gestora_condominio';

-- VISUALIZAÇÃO das tabelas
SELECT table_schema, table_name from information_schema.tables
WHERE table_schema = 'condominio';