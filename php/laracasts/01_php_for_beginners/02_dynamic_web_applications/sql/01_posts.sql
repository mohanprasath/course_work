drop table posts;

create table posts (
                       id int auto_increment primary key ,
                       title varchar(250) not null ,
                       comment varchar(1000)
);