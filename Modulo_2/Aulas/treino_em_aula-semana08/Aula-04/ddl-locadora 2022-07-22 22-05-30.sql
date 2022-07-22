-- insert ator
INSERT INTO locadora.ator(nome, nome_artistico)
VALUES('Uesley', 'Safadão')

INSERT INTO locadora.ator(nome, nome_artistico)
VALUES('Jhonny Depp', 'Jack Sparrow')

--insert categoria
INSERT INTO locadora.categoria(nome)
VALUES('Clipes de música')

INSERT INTO locadora.categoria(nome)
VALUES('Aventura')

--insert filme
INSERT INTO locadora.filme(nome)
VALUES('Terror')

INSERT INTO locadora.filme(nome)
VALUES('Piratas do caribe')

--insert historico
INSERT INTO locadora.historico()

--DROP TABLE
drop table locadora.historico

--ADD FK na tabela
ALTER TABLE locadora.historico add constraint
FK_ATOR_id_ator foreign key (FK_id_ator) references locadora.ator (id_ator)

ALTER TABLE locadora.historico add constraint
FK_FILME_id_filme foreign key (FK_id_filme) 
references locadora.filme (id_filme)

SELECT * FROM locadora.ator a
SELECT * FROM locadora.categoria c
SELECT * FROM locadora.filme f
SELECT * FROM locadora.historico h

--select para ver as constraints
SELECT * FROM locadora.