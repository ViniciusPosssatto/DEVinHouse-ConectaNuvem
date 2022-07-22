/*
CRUD

I = INSERT
S = SELECT
U = UPDATE
D = DELETE

*/

--INSERT -- inserir
INSERT INTO gestora_condominio.apartamento(area, apt_numero)
VALUES (141, 13)

INSERT INTO gestora_condominio.edificio(id_edificio, endereco, data_construcao, data_ultima_vistoria)
VALUES (15, 'Rua Palmeiras, nº234', '2010-04-03', '2022-03-09')

INSERT INTO gestora_condominio.pessoa(data_nascimento, cpf, sexo, nome)
VALUES ('2001-02-14', 333333333, 'f', 'Arroba')

--UPDATE - atualizar
UPDATE gestora_condominio.edificio
SET endereco='rua bla, nº 334', data_construcao='2020-03-20'
where id_edificio=13

UPDATE gestora_condominio.edificio
SET endereco='Rua Huehue, nº 123', data_ultima_vistoria='2022-05-15'
where id_edificio=14

UPDATE gestora_condominio.apartamento
SET area=155
where apt_numero=12

UPDATE gestora_condominio.pessoa
SET cpf=1235123
where cpf=333333333

-- DELETE
delete from gestora_condominio.proprietario;
--vai deletar todos os dados que tiver dentro da tabela. utilizar o where.

delete from gestora_condominio.pessoa
where cpf = 1235123

--SELECT -- leitura
select * from gestora_condominio.pessoa p
order by cpf;