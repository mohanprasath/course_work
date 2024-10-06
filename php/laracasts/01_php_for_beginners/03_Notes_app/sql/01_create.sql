drop table posts if exists;

create table posts (
                       id int auto_increment primary key ,
                       title varchar(250) not null ,
                       comment varchar(1000)
);

select id, title from posts where id=2;


drop table users if exists;
create table users (
                       id int auto_increment primary key,
                       name varchar(250) not null,
                       email varchar(250) not null unique
);


drop table notes if exists;
create table notes (
                       id int primary key auto_increment,
                       body text char set utf8 not null,
                       user_id int not null,
                       foreign key (user_id) references users(id)
);
