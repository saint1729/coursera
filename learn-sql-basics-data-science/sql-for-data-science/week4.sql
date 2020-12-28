select c.CustomerId, c.FirstName, c.LastName, c.Address, upper(concat(c.City, " ",  c.Country)) as cc from Customer c where c.CustomerId = 16;

select lower(concat(substr(emp.FirstName, 1, 4), substr(emp.lastname, 1, 2))) from Employee emp where emp.FirstName = 'Robert' and emp.LastName = 'King';

select emp.firstname fn, emp.lastname ln, datediff(now(), emp.hiredate) / 365 exp from employee emp group by fn, ln, exp having exp >= 15 order by ln;

select c.City, count(c.city) cc from Customer c group by c.City having cc = 2 order by cc desc;

select concat(c.firstname, c.lastname) as c1, concat(c.firstname, c.lastname, inv.invoiceid) c2 from Customer c, Invoice inv where c.CustomerId = inv.CustomerId group by c1, c2 having c1 = 'AstridGruber' order by c2;





