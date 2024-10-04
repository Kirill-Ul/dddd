-- 1. Выбрать все записи заказов в которых наименование страны
-- отгрузки начинается с 'U'

select*
from orders
where ship_country like 'U%'

-- 2. Выбрать записи заказов (включить колонки идентификатора заказа,
-- идентификатора заказчика, веса и страны отгузки), 
-- которые должны быть отгружены в страны имя которых начинается с 'N',
-- отсортировать по весу (по убыванию) и вывести только первые 10 записей.

select order_id, customer_id, freight, ship_country
from orders
where ship_country like 'N%'
order by freight desc
limit 10

-- 3. Выбрать записи работников (включить колонки имени, фамилии, телефона,
-- региона) в которых регион неизвестен

select last_name, first_name, home_phone, region
from employees
where region is null

-- 4. Подсчитать кол-во заказчиков регион которых известен
select count (*)
from customers
where region is not null


-- 5. Подсчитать кол-во поставщиков в каждой из стран и отсортировать 
-- результаты группировки по убыванию кол-ва

select country, count(*)
from suppliers
group by country
order by count (*) desc 

-- 6. Подсчитать суммарный вес заказов (в которых известен регион) по странам,
-- затем отфильтровать по суммарному весу (вывести только те записи где суммарный вес больше 2750)
-- и отсортировать по убыванию суммарного веса.

select ship_country, sum(freight) sum_freight
from orders
where ship_region is not null
group by ship_country
having sum(freight) > 2750
order by sum_freight desc

-- 7. Выбрать все уникальные страны заказчиков и поставщиков и отсортировать страны по возрастанию

select country
from customers
union
select country
from suppliers
order by country

-- 8. Выбрать такие страны в которых "зарегистированы" одновременно и заказчики и поставщики и работники.

select country
from customers
intersect
select country
from suppliers
intersect
select country
from employees

-- 9. Выбрать такие страны в которых "зарегистированы" одновременно заказчики и поставщики,
-- но при этом в них не "зарегистрированы" работники.

select country
from customers
intersect
select country
from suppliers
except
select country
from employees
order by country

-- 10. Найти заказчиков и обслуживающих их заказы сотрудников таких, что и заказчики
-- и сотрудники из города London, а доставка идёт компанией Speedy Express.
-- Вывести компанию заказчика и ФИО сотрудника.

select customers.company_name,employees.first_name, employees.last_name 
from orders
join customers on orders.customer_id = customers.customer_id
join employees on orders.employee_id = employees.employee_id
join shippers on orders.ship_via = shippers.shipper_id
where customers.city = 'London' 
 and employees.city = 'London' 
 and shippers.company_name = 'Speedy Express';

 -- 11.Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, 
 -- которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже,
 -- имя контакта поставщика и его телефонный номер.

select product_name, units_in_stock, quantity_per_unit, phone
from products
join categories on products.category_id = categories.category_id
join suppliers on products.supplier_id = suppliers.supplier_id
where category_name in ('Beverages', 'Seafood') and discontinued <> 1 and units_in_stock < 20

-- 12. Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.

select contact_name, order_id
from customers
left join orders on customers.customer_id = orders.customer_id
where order_id is null
order by contact_name

13. Переписать предыдущий запрос, использовав симметричный вид джойна (подсказка: речь о LEFT и RIGHT).


select contact_name, order_id
from orders
right join customers on customers.customer_id = orders.customer_id
where order_id is null
order by contact_name


