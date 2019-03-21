Create database Ferreteria_Dur;
 use Ferreteria_Dur;
 Create table Clientes(
     id_cliente int (2) not null primary key,
     Nombre varchar(50) not null,
     Ape_Pat varchar(40) not null,
     Ape_Mat varchar(40) not null,
     Telefono varchar(10) not null,
     email varchar(30) not null);

insert into Clientes (id_cliente,Nombre,Ape_Pat,Ape_Mat,Telefono,email) values
(1,'Juan','Perez','Marquez','7751097865','Juan@mail'),
(2,'Pedro','Lopez','Lopez','7756453245','Pe@mail'),
(3,'Andrea','Andrade','Alarcon','7757568900','AAA@mail.com');

CREATE USER 'Pablo'@'localhost' IDENTIFIED BY 'Duran';
GRANT ALL privileges ON `Ferreteria_Dur`.* TO 'Pablo'@'localhost';
FLUSH PRIVILEGES;