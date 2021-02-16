Xp gold
Exc 1
1.
select distinct rating from film
select count(rating) from film where rating = 'PG -13'
select count(rating) from film where rating = 'PG'
select count(rating) from film where rating = 'R'
select count(rating) from film where rating = 'NC-17'
+---------+
| count   |
|---------|
| 210     |
+---------+

2.
select title,rating from film where rating in('G','PG-13')
2.1.
select title,rating,rental_rate from film where rating in('G','PG-13') and length <=200 and rental_rate <3.00  order by title

3.update customer set first_name='Itama',last_name='Menachemi'  where customer_id =1

4.select address,first_name,address.address_id
from customer
join address
on customer.address_id = address.address_id
where first_name ='Itama';
update address set address='1000 hhhh' where address.address_id =5
| address   | first_name   | address_id   |
|-----------+--------------+--------------|
| 1000 hhhh | Itama        | 5            |
+-----------+--------------+--------------+

Exc 2
1.
update students set birth_date='02-11-1998' where lname ='Benichou'
2.
update students set lname ='Guez' where lname ='Grez'

DELETE
1.
select count(*) from students

COUNT
1.select count(*) from students
2.select count(*) from students where birth_date > '01-01-2000'

INSERT/AFTER
1.alter table students
add column math_grade smallint 
2.update students set math_grade =80 where id=1
3.update students set math_grade =90 where id in(2,4)
4.update students set math_grade =40 where id =6
5.select count(*) from students where math_grade >83
6.insert into students (fname,lname,math_grade,birth_date)
values('Omer','Simpson',70,'01-02-1992'),
('Omer','Simpson',null,'01-02-1992')
7.BONUS
select fname, count(math_grade) from students group by fname

SUM
select sum(math_grade)from students