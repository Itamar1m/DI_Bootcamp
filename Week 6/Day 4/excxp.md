Exc 1
1.
select first_name as "First Name",last_name as "Last Name"  from employees 

2.
select employees.department_id
from employees
group by employees.department_id
having count(employees.department_id) = 1

3.
select * from employees order by first_name desc

4.
select first_name ,last_name ,salary ,salary*0.15 as pf from employees

5.
select employee_id,first_name,last_name,salary from employees order by salary 

6.
select sum(salary)from employees

7.
select min(salary) ,max(salary)from employees

8.
select avg(salary)from employees

9.
select count(*) from employees

10.
select upper(first_name) from employees

11.
select substring(first_name,0,4) from employees

12.
select concat ( first_name,' ',last_name) as "Full Name"  from employees

13.
select first_name,last_name ,(length(first_name)+length(last_name)) as length from employees 
select first_name, last_name, length(CONCAT(first_name, last_name)) 
as "Full Name"
from employees
14.
select pg_typeof(first_name)
from employees
15.
select * from employees limit 10

Exc 2
1.
select concat( first_name,' ',last_name) as "Full Name"  from employees where salary between 10000 and 15000
2.
select concat(first_name,' ',last_name) as "Full Name",hire_date from employees where hire_date between '01-01-1987' and '01-01-1988'
3.
select first_name from employees where first_name like'%e%' and first_name like'%c%'
4.
select last_name,job_title,salary from employees 
join jobs
on employees.job_id=jobs.job_id
where job_title not in('Programmer','Shipping Clerk')
and salary not in (4500,10000,15000)
5.
select last_name from employees where length(last_name)=6
6.
select last_name from employees where position('e'in last_name) =3
7.
select distinct job_title from employees 
join jobs
on employees.job_id=jobs.job_id
8.select * from employees where last_name in('Jones','Blake','Scott','King','Ford')

Exc 3
1.
update employees set email='available' from departments where
employees.department_id = departments.department_id and Department_name ='Accounting'

2.

3.update employees set email='available' from departments where
employees.department_id = departments.department_id

4.pdate employees set salary = 8000 where employee_id =105 and salary <5000
