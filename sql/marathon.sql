create database marathon;

use marathon;

create table deployment(
  app_id int(11) primary key auto_increment,
  app_name varchar(50),
  app_json text
);