# creating and using a database
create database mohan;
use mohan;

# creating the tables
create table department (dept_id integer not null, dept_name varchar(20), building varchar(15), budget numeric(12,2), primary key(dept_name)); 
create table course (course_id varchar(7), title varchar(50), dept_name varchar(20), credits numeric(2,0), primary key(course_id), foreign key(dept_name) references department(dept_name));

# natural join
select course.dept_name, title, department.building from course natural join department;

# cartesian product
select course.dept_name, title, department.building from course join department;

# proof - multiply the count results of the following two statements then compare it with the no of rows from the above result
select count(*) from course;
select count(*) from department;

# selecting all the rows from a table
select * from department; 
select * from course;
select * from department, course;

# counting all the rows from a table
select count(*) from department; 

# Inserting some rwos in the above reated tables
insert into course values ('IT001', 'Introduction to Computers', 'IT', 5.0);
insert into course values ('CSE001', 'C Programming', 'CSE', 5.0);
insert into course values ('CSE002', 'Java Programming', 'CSE', 5.0);
insert into department values (1, "IT", "i-block", 10000000.00);
insert into department values (2, "CSE", "cse-block", 30000000.00);

# removing or dropping a column from a table
alter table department drop dept_name; 
alter table course drop credits;

# removing a table in its entirity
drop table department, course;

# renaming while selecting
select dept_name as department from course; 

# distinct values from the table
select distinct dept_name from course;

# where clause

# set operations
# union
# intersection
# except
# set operations with all keyword

# and, or not, null

# aggregate functions
# avg
# min
# max
# sum
# count

# above aggregations with grouping
# having clause

# aggregation with null and boolean values


