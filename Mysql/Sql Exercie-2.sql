#Exercise 2

#Question 1
select distinct City from customers;
select count(distinct City)  from customers;

#Question 2
select max(Quantity) from order_details;
select min(Quantity) from order_details;

#Question 3
Select avg(Quantity) from order_details;
select sum(Quantity) from order_details;

#Question 4
select ProductName from products
limit 11 offset 4;

#Question 5
select *  from suppliers
where SupplierName like "_a%" ;

#Question 6
select * from customers
where Not (Country = "USA"or Country = "Canada");

#Question 7 dates in the question are different.
select * from orders
join order_details On orders.OrderID = order_details.OrderID 
where OrderDate between "1996-07-08" and "1997-01-07"
order by order_details.OrderID desc;

#question 8
select distinct City from customers;
select count(distinct City)  from customers;

#Question 9
select * from employees
where not(LastName="Sanjay" or LastName = "Soniya") ;

#Question 10
create table SupplierDetail As select * from suppliers;

#Question 11
delete  from customers 
where Country = "Venezuela";
select * from customers;