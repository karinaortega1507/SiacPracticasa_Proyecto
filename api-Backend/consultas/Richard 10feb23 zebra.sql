--1 poner usuario                                           --pusuario                     --pempresa            Jessenia Gomez Practicasa
-- fsoft.Practi                   jgomez@Practi   --encryp(jgomez)               Practi  Jairo Gomez Mercatti
select * from siacfsbs.dbo.fsbsmcliusu where cliciausu = '­v}xg' and cliciagrupo = 'Practi'
--usuario no existe

--2 muestro las compañias
select a.cliciaciacodigo, a.cliciacianombre, a.cliciarutaBD, a.clicianonBD from siacfsbs.dbo.fsbsmclicia a 
	inner join siacfsbs.dbo.fsbsmcliusu b on a.cliciaidenti = b.cliciaidenti and b.cliciagrupo = b.cliciagrupo
where b.cliciausu = '­v}xg' --pusuario
and b.cliciagrupo = 'Practi' --pempresa


---Selecciona compañia "01"

--3 ingresado a la compañia

              --${p_prefijo}.dbo.siacusar where usrcodigo = ${p_usuario} / falta la contrasenia
select * from SiacPracticasa.dbo.siaccusr where usrcodigo = '­v}xg'

--4 localidad
select b.locdescri,b.loccodigo from SiacPracticasa.dbo.siactloc a inner join cgblocal b on a.ciacodigo = b.ciacodigo and a.loccodigo = b.loccodigo
	where a.ciacodigo = '02' and usrcodigo = '­v}xg' and b.locstatus = 'A'
	                                     --${p_usuario}

---seleccione localidad 

--5 armar menu
select a.* from siacopc a inner join siactusrweb b on a.opctag = b.opctag and a.modcodigo = b.modcodigo
	where b.ciacodigo = '01' and b.usrcodigo = '­v}xg' and b.modcodigo = 'WEB'
order by a.opctag



SELECT COLUMN_NAME
FROM SiacPracticasa.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'siaccusr';

-- --1 poner usuario
-- -- fsoft.Practi
-- select * from siacfsbs.dbo.fsbsmcliusu where cliciausu = '­¡ƒsv' and cliciagrupo = 'Mercatti'
-- --usuario no existe

-- --2 muestro las compa�ias
-- select a.cliciaciacodigo, a.cliciacianombre, a.cliciarutaBD, a.clicianonBD from siacfsbs.dbo.fsbsmclicia a 
-- 	inner join siacfsbs.dbo.fsbsmcliusu b on a.cliciaidenti = b.cliciaidenti and b.cliciagrupo = b.cliciagrupo
-- where b.cliciausu = '_‹xAƒ‚P_NO' and b.cliciagrupo = 'Mercatti'
-- ---Selecciona compa�ia "01"

-- --3 ingresado a la compa�ia, para el usuario '_‹xAƒ‚P_NO' tiene clicianonBD = SiacMercatti, entonces
-- -- select * from SiacPracticasa.dbo.SiacMercatti where usrcodigo = '_‹xAƒ‚P_NO'
-- select * from SiacMercatti.dbo.siactusr where usrcodigo = '­¡ƒsv'

-- --- TODO: hasta aqui entiendo lo que hay que hacer vamos a ver luego

-- --4 localidad
-- select b.locdescri from SiacPracticasa.dbo.siactloc a inner join cgblocal b on a.ciacodigo = b.ciacodigo and a.loccodigo = b.loccodigo
-- 	where a.ciacodigo = '01' and usrcodigo = '�v}xg' and b.locstatus = 'A'

-- ---seleccione localidad 

-- --5 armar menu
-- select a.* from siacopc a inner join siactusrweb b on a.opctag = b.opctag and a.modcodigo = b.modcodigo
-- 	where b.ciacodigo = '01' and b.usrcodigo = '�v}xg' and b.modcodigo = 'WEB'
-- order by a.opctag


-- select * from siacopc where modcodigo = 'WEB'