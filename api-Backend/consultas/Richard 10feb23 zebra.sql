--1 poner usuario                                           --pusuario                     --pempresa            Jessenia Gomez Practicasa
-- fsoft.Practi                   jgomez@Practi   --encryp(jgomez)               Practi  Jairo Gomez Mercatti
select * from siacfsbs.dbo.fsbsmcliusu where cliciausu = '­v}xg' and cliciagrupo = 'Practi'
--usuario no existe

--2 muestro las compañias
select a.cliciaciacodigo,
 a.cliciacianombre,
 a.cliciarutaBD,
 a.clicianonBD from siacfsbs.dbo.fsbsmclicia a 
	inner join siacfsbs.dbo.fsbsmcliusu b on a.cliciaidenti = b.cliciaidenti and b.cliciagrupo = b.cliciagrupo
where b.cliciausu = '­v}xg' --pusuario
and b.cliciagrupo = 'Practi' --pempresa


---Selecciona compañia "01"

--3 ingresado a la compañia

              --${p_prefijo}.dbo.siacusar where usrcodigo = ${p_usuario} / falta la contrasenia
select * from SiacPracticasa.dbo.siaccusr where usrcodigo = '­v}xg' and usrclave = 'I4bªszuj'

--4 localidad
-- select b.locdescri,
b.loccodigo from SiacPracticasa.dbo.siactloc a inner join cgblocal b on a.ciacodigo = b.ciacodigo and a.loccodigo = b.loccodigo
-- 	where a.ciacodigo = '02' and usrcodigo = '­v}xg' and b.locstatus = 'A'
-- 	                                     --${p_usuario}

select b.locdescri,
b.loccodigo from SiacPracticasa.dbo.siactloc a inner join SiacPracticasa.dbo.cgblocal b on a.ciacodigo = b.ciacodigo and a.loccodigo = b.loccodigo
	where a.ciacodigo = '01' and usrcodigo = '­v}xg' and b.locstatus = 'A'
	                                     --${p_usuario}

---seleccione localidad 

--5 armar menu
select a.* from siacpracticasa.dbo.siacopc a inner join siacpracticasa.dbo.siactusrweb b on a.opctag = b.opctag and a.modcodigo = b.modcodigo
	where b.ciacodigo = '01' and b.usrcodigo = '­v}xg' and b.modcodigo = 'WEB'
order by a.opctag





SELECT COLUMN_NAME, DATA_TYPE
FROM SiacPracticasa.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'fapvendedor';


SELECT TOP 100 *
FROM SiacPracticasa.dbo.facped




-- insert into SiacPracticasa.dbo.facped 
-- (pednumped,
--  pedtivapor,
--  pedsubtot,
--  pediva,
--  pedtotal,
--  pedusuisys,
--  pedusumodi,
--  pedfeccrea,
--  pedfecmodi)
-- values ( @pednumped,

-- @pedtivapor,

-- @pedsubtot,

-- @pediva,

-- @pedtotal,

-- @pedusuisys,
--  User,
--  SYSDATETIME(),
--  SYSDATETIME() );

insert into SiacPracticasa.dbo.facped 
values(
	'01',
	@pednumped,
	'01',
	NULL,
	'PR',
	'EFE',
	'D',
	'000001',
	'000001',
	'GUAYAQUIL',
	0.00,
	SYSDATETIME(),
	SYSDATETIME(),
	0.00,
	@pedtivapor,
	@pedsubtot,
	@pediva,
	@pedtotal,
	'P',
	'prueba app mobile',
	SYSDATETIME(),
	SYSDATETIME(),
	@pedusuisys,
	User,
	SYSDATETIME(),
	SYSDATETIME(),
	@pedusuisys,
	User,
	null,
	(select vencodigo from SiacPracticasa.dbo.fapvendedor where 1=1 and usrcodigo=@pedusuisys and ciacodigo =@ciacodigo and loccodigo=@loccodigo),
	(select zoncodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
	0.00,
	0.00,
	0.00,
	0.00,
	(select tipcodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
	0.00,
	12.00,
	0.00,
	0.00,
	0.00,
	0,
	'CC',
	1,
	0,
	0.00,
	0,
	0.00,
	0.00,
	0,
	0,
	0,
	null,
	null,
	null,
	0,
	0.00,
	-1,
	0,
	NULL,
	0,
	NULL,
	'000',
	'000',
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0.00,
	(select regcodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
	(select ciucodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
	(select procodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
	0,
	1,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	0.00,
	NULL,
	'000',
	'B',
	NULL,
	NULL,
	NULL,
	' ',
	(select top 1 sysservicio from SiacPracticasa.dbo.SiacSys),
	@pedvalser,
	@mesacodigo
);


-- --1 poner usuario
-- -- fsoft.Practi
-- select * from siacfsbs.dbo.fsbsmcliusu where cliciausu = '­¡ƒsv' and cliciagrupo = 'Mercatti'
-- --usuario no existe

-- --2 muestro las compa�ias
-- select a.cliciaciacodigo,
 a.cliciacianombre,
 a.cliciarutaBD,
 a.clicianonBD from siacfsbs.dbo.fsbsmclicia a 
-- 	inner join siacfsbs.dbo.fsbsmcliusu b on a.cliciaidenti = b.cliciaidenti and b.cliciagrupo = b.cliciagrupo
-- where b.cliciausu = '_‹xAƒ‚P_NO' and b.cliciagrupo = 'Mercatti'
-- ---Selecciona compa�ia "01"

-- --3 ingresado a la compa�ia,
 para el usuario '_‹xAƒ‚P_NO' tiene clicianonBD = SiacMercatti,
 entonces
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