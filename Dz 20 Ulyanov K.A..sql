select * from public.customers


select contact_name, city 
from customers

select * from public.orders

select order_id, shipped_date - order_date
from orders

select distinct ship_city
from orders

select distinct ship_city, ship_country
from orders

select count (*) ship_name
from orders

select distinct ship_country
from orders

select order_id, ship_country 
from orders
where ship_country in ('France', 'Austria', 'Spain')

select * from public.orders
select customer_id, required_date
from orders 
order by required_date desc

select customer_id, shipped_date
from orders
order by shipped_date asc

select min(units_in_stock)
from products
where units_in_stock > 30

select max(units_in_stock)
from products
where units_in_stock > 30

select avg(shipped_date - order_date)
from orders
where ship_country = 'USA'

select sum(units_in_stock * unit_price)
from products
where c <> 0




