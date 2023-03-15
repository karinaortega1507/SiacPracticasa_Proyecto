(select * from SiacPracticasa.dbo.inmart where artcodigo='000010'),
(select * from SiacPracticasa.dbo.fatped),
(select (artprecventa1*0.12) * 1 from SiacPracticasa.dbo.inmart where artcodigo='000010'),
select * from SiacPracticasa.dbo.inmart