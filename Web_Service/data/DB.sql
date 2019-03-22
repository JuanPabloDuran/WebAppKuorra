Create database Ferreteria_Dur;
 use Ferreteria_Dur;
 Create table Clientes(
     id_cliente int  auto_increment primary key,
     Nombre varchar(50) not null,
     Ape_Pat varchar(40) not null,
     Ape_Mat varchar(40) not null,
     Telefono varchar(10) not null,
     email varchar(30) not null);


CREATE USER 'Pablo'@'localhost' IDENTIFIED BY 'Duran';
GRANT ALL privileges ON `Ferreteria_Dur`.* TO 'Pablo'@'localhost';
FLUSH PRIVILEGES;
