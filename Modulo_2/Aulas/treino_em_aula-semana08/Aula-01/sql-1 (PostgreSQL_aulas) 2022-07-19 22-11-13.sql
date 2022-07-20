create schema auto_generated_field;

create table auto_generated_field.pessoa(
  id_pessoa serial primary key,
  primeiro_nome varchar(40) not null,
  ultimo_nome varchar(40) not null,
  nome_completo varchar(80) generated always as (primeiro_nome || ' ' || ultimo_nome) stored
);

select * from auto_generated_field.pessoa;

insert into auto_generated_field.pessoa(primeiro_nome, ultimo_nome)
values ('Natan', 'Nascimento');