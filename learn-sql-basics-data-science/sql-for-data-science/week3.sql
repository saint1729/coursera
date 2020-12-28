select count(*) from Artist ar, Album al where ar.ArtistId = al.ArtistId and ar.name = 'Led Zeppelin';

select count(*) from Artist ar, Album al, Track tr where ar.ArtistId = al.ArtistId and al.AlbumId = tr.AlbumId and ar.name = 'Audioslave';

select count(*) from Invoice inv left join Customer cu on cu.CustomerId where cu.CustomerId = inv.CustomerId;

select sum(tr.unitprice) from Track tr, Album al where tr.AlbumId = al.AlbumId and al.title = 'Big Ones';

select count(*) from Invoice, InvoiceLine;

select tr.name from Track tr, Album al where tr.AlbumId = al.AlbumId and al.Title = 'Californication' limit 8;

select count(cu.CustomerId) as c, cu.FirstName, cu.LastName, cu.City, cu.Email from Customer cu, Invoice inv where cu.CustomerId = inv.CustomerId group by cu.FirstName, cu.LastName, cu.City, cu.Email limit 5;

select tr.name, al.title, ar.ArtistId, tr.TrackId from Track tr, Album al, Artist ar where tr.AlbumId = al.AlbumId and ar.ArtistId = al.ArtistId and tr.TrackId = 12;

select emp2.LastName, emp1.LastName from Employee emp1, Employee emp2 where emp1.ReportsTo = emp2.EmployeeId;

select ar.Name, ar.ArtistId from Artist ar left join Album al on ar.ArtistId = al.ArtistId where al.AlbumId is null;

select emp.FirstName, emp.LastName as ln from Employee emp
union
select cu.FirstName, cu.LastName as ln from Customer cu
order by ln desc limit 6;

select distinct cu.CustomerId, cu.City, inv.BillingCity from Customer cu, Invoice inv 
where cu.CustomerId = inv.CustomerId;






