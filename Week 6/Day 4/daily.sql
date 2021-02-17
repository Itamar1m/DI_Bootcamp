CREATE TABLE orders(
id serial primary key,
full_price integer			
);
insert into orders (id)
values
(1),
(2),
(3);
CREATE TABLE items(
id serial primary key,
item varchar(20)not null,
price integer not null 	
);

insert into items(item,price)
values
('Chicken',10),
('Steak',15),
('French Fries',5),
('Salad',12),
('Drink',5);

CREATE TABLE items_to_order(
items integer references items(id) on delete cascade,
orders integer references orders(id) on delete cascade	
);		
insert into items_to_order(orders,items)
values
(1,1),
(1,3),
(1,5),
(2,1),
(2,2),
(2,2),
(3,3),
(3,4),
(3,5)

select * from items_to_order
	
CREATE FUNCTION order_price(ord integer)
 RETURNS integer AS $full_price$
BEGIN
return(
select sum(price) from items
right join items_to_order
on items.id = items_to_order.items
where orders= ord);  
END;
$full_price$ LANGUAGE plpgsql;

select *from order_price(2)