drop database if exists jsgame;
create database jsgame;

use jsgame;

drop table if exists account;
create table account(
	id varchar(40) not null,
	passwd varchar(40) null,
	nickname varchar(40) null,
	level int DEFAULT 1,
	exp int DEFAULT 1,
	speed float DEFAULT 1.2,
	wbLimitQuantity int DEFAULT 1,
	wbLen int DEFAULT 1,
	money int DEFAULT 0,
	primary key(id)
);

#insert into account values ("admin", "1234", "admin", 20, 1, 2.0, 3, 3, 5000);