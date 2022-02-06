SELECT * FROM northwind.customers;
#1.	Write a query to get Product name and quantity/unit.
Select northwind.products.product_name, northwind.products.quantity_per_unit 
FROM Northwind.products;
#2. Write a query to get current Product list (Product ID and name).  
Select northwind.products.id, northwind.products.product_name 
FROM northwind.products;
#3. Write a query to get discontinued Product list (Product ID and name). 
Select northwind.products.id,northwind.products.product_name 
FROM northwind.products 
WHERE northwind.products.discontinued="1" ;
#4. Write a query to get most expense and least expensive Product list (name and unit price).  
Select max(northwind.products.product_name),max(northwind.products.list_price),
min(northwind.products.product_name),min(northwind.products.list_price) 
from northwind.products;
#5. Write a query to get Product list (id, name, unit price) where current products cost less than $20. 
Select northwind.products.id, northwind.products.product_name, northwind.products.list_price 
from northwind.products 
where northwind.products.list_price<"20";
#6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25. 
Select northwind.products.id, northwind.products.product_name, northwind.products.list_price 
from northwind.products 
where northwind.products.list_price between 15 and 20;
#7. Write a query to get Product list (name, unit price) of above average price.  
Select avg(northwind.products.list_price) from northwind.products;
Select northwind.products.product_name, northwind.products.list_price 
from northwind.products where northwind.products.list_price>15.84577778;
#8. Write a query to get Product list (name, unit price) of ten most expensive products.  
Select northwind.products.product_name, northwind.products.list_price 
from northwind.products ORDER BY list_price DESC limit 10;
#9. Write a query to count current and discontinued products. 
Select count(northwind.products.discontinued) from northwind.products where discontinued="0";
Select count(northwind.products.discontinued) from northwind.products where discontinued="1";
#10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  
Select northwind.products.product_name, northwind.products.reorder_level, northwind.products.quantity_per_unit 
From northwind.products 
where northwind.products.quantity_per_unit<northwind.products.reorder_level


