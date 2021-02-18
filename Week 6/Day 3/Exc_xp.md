Exc 1
1.
select name from language

2.
select title ,description,language.name
from language 
join film
on film.language_id=language.language_id
2.1
select title ,description,language.name
from language 
right join film
on film.language_id=language.language_id
2.2
select title ,description,language.name
from language 
left join film
on film.language_id=language.language_id
-Italian,french ,German,Mandarin

3.
insert into new_film(name)
values('A movie'),
('B movie'),
('C movie'),
('D movie')

4.
CREATE TABLE customer_review(
review_id serial primary key,
film_id smallint,
language_id smallint,
title varchar(50),
score smallint,
review_text text,
last_update time,
FOREIGN KEY (film_id) REFERENCES  new_film(film_id)	on delete cascade, 
FOREIGN KEY (language_id) REFERENCES  language(language_id)		
)

5.
insert into customer_review(film_id,language_id,title,score,review_text,last_update)
values
(1,1,'Best',10,'Best movie ever',now()::time),
(1,3,'Bad',2,'Worst movie ever',now()::time)

6. 
 delete from new_film where id =3

 Exc 2
 1.
select language_id,title,film_id from film order by film_id
update film set language_id =3  where film_id in (1,2)
2.

3.drop table customer_review
select count(rental_date)-count(return_date)
from rental 183

4.select rental_date from rental
where return_date is null
5.
Select rental_rate, title, inventory.inventory_id, rental_date from rental 
INNER JOIN inventory
ON inventory.inventory_id = rental.inventory_id
INNER JOIN film 
ON film.film_id = inventory.film_id
WHERE return_date IS NULL
ORDER BY rental_rate DESC LIMIT 30

6.1
select title,first_name,last_name,description from film_actor
join film 
on film.film_id =film_actor.film_id
join actor
on actor.actor_id=film_actor.actor_id
where description like '%Sumo%' and first_name='Penelope' and last_name='Monroe'

6.2
join film_category
on film_category.film_id=film.film_id
join category 
on category.category_id =film_category.category_id
where rating ='R' and name like '%Documentary%' and length<60

6.3
select title,first_name ,rental_rate,last_name,return_date
from film 
join inventory on
film.film_id =inventory.film_id
join rental on
rental.inventory_id = inventory.inventory_id
join customer on
customer.customer_id =rental.customer_id
where rental_rate>4 and first_name ='Matthew' and last_name='Mahan'
and return_date between '2005-07-28' and '2005-08-01'
6.4
select title,first_name ,rental_rate,last_name,return_date,replacement_cost
from film 
join inventory on
film.film_id =inventory.film_id
join rental on
rental.inventory_id = inventory.inventory_id
join customer on
customer.customer_id =rental.customer_id
where first_name ='Matthew' and last_name='Mahan'
and description like '%Boat%'