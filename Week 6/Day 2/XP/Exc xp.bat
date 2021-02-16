Exc xp
Excercise 1:
1. select item,price from items order by price asc
2.select item,price from items where price >= 80 order by price asc
    item    | price
------------+-------
 Fan        |    80
 Small DESK |   100

 3.select fname,lname from customers

 4.select lname from customers order by lname desc 
   lname
---------
 Scott
 Jones
 Jones
 Johnson
 Green

No:2
1.CREATE TABLE purchases(
customer_id smallint,	
item_id	smallint,
FOREIGN KEY (customer_id) REFERENCES customers(id_),
FOREIGN  KEY (item_id)REFERENCES items (id)	

 2.   insert into purchases(customer_id,item_id)
    values (1,2),
    (2,2),
    (3,3),
    (4,2),
    (5,1)
    customer_id | item_id
    -------------+---------
            1 |       2
            2 |       2
            3 |       3
            4 |       2
            5 |       1

Exc 3
1.select * from purchases,not useful at all.

2.SELECT *
FROM purchases 
INNER JOIN customers
ON  purchases.customer_id= customers.id_

3.select item
from items
inner join purchases 
on  id = customer_id
where customer_id = 4

select item
from purchases
join customers
on purchases.customer_id = customers.id_
join items 
on purchases.item_id = items.id
where customer_id =3

4.
select item_id from purchases where item_id in (1,2)

Exc 4
1.
insert into items(item,price)
values('Hard drive',200);
insert into purchases(item_id,customer_id)
values (4,3)

Exc 5
select fname,lname,item
from purchases 
join customers
on customer_id=id_
join items


Excercise 2:
1.slect * from customer
2.select (first_name,last_name) as full_name  from customer 
       full_name
-------------------------
 (Jared,Ely)
 (Mary,Smith)
 (Patricia,Johnson)
 (Linda,Williams)
 (Barbara,Jones)
 (Elizabeth,Brown)
 (Jennifer,Davis)
 (Maria,Miller)
 (Susan,Wilson)
 (Margaret,Moore)
 (Dorothy,Taylor)
 etc....
 3.select distinct create_date from customer 

 4.select * from customer order by first_name desc
+-------------------------+--------
         479 |        1 | Zachary     | Hite         | zachary.hite@sakilacustomer.org          |        484 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         174 |        2 | Yvonne      | Watkins      | yvonne.watkins@sakilacustomer.org        |        178 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         190 |        2 | Yolanda     | Weaver       | yolanda.weaver@sakilacustomer.org        |        194 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 |      1
         212 |        2 | Wilma       | Richards     | wilma.richards@sakilacustomer.org        |        216 | t          | 2006-02-14  | 2013-05-26 14:49:45.738 \

  5.select film_id,title,description,release_year,rental_rate
from film
order by rental_rate

6.select address,district,phone 
from address
where district ='Texas'

             address             | district |    phone
---------------------------------+----------+--------------
 1795 Santiago de Compostela Way | Texas    | 860452626434
 333 Goinia Way                  | Texas    | 909029256431
 913 Coacalco de Berriozbal Loop | Texas    | 262088367001
 530 Lausanne Lane               | Texas    | 775235029633
 1894 Boa Vista Way              | Texas    | 239357986667
(5 rows)

7.select * from film where film_id in(15,150)

8.select film_id,title,description,length
from film
where title =''

9.select film_id,title,description,length
from film
where title like '%al%'

10.select title,rental_rate from film order by rental_rate limit 1 offset 9

11.select title,rental_rate from film order by rental_rate offset 10 fetch first 10  row only 

12.select  customer.customer_id,amount,payment_date 
from customer
join payment
on customer.customer_id=payment.customer_id

13.
select film.film_id
from film
join inventory
on film.film_id = inventory.film_id
where film.film_id not in (inventory.film_id)

14.
select city,country
from country
join city
on  country.country_id=city.country_id