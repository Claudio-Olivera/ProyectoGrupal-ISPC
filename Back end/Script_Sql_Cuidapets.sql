CREATE SCHEMA IF NOT EXISTS `new_schema` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `new_schema` ;

-- -----------------------------------------------------
-- Table `new_schema`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema`.`admin` (
  `Id_Admin` INT NOT NULL,
  `Username` VARCHAR(20) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Password` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`Id_Admin`),
  UNIQUE INDEX `Id_Admin` (`Id_Admin` ASC),
  UNIQUE INDEX `Username` (`Username` ASC),
  UNIQUE INDEX `Email` (`Email` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `new_schema`.`contacto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema`.`contacto` (
  `Id_Contacto` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Message` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`Id_Contacto`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `new_schema`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema`.`user` (
  `Id_User` INT NOT NULL AUTO_INCREMENT,
  `User` VARCHAR(20) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Password` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`Id_User`),
  UNIQUE INDEX `User` (`User` ASC),
  UNIQUE INDEX `Email` (`Email` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `new_schema`.`more_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema`.`more_data` (
  `Id_more_Data` INT NOT NULL,
  `Name` VARCHAR(20) NOT NULL,
  `LastName` VARCHAR(50) NOT NULL,
  `Calle` VARCHAR(30) NOT NULL,
  `Direccion` VARCHAR(30) NOT NULL,
  `Piso_Depto` VARCHAR(30) NULL DEFAULT NULL,
  `Ciudad` VARCHAR(30) NOT NULL,
  `Provincia` VARCHAR(30) NOT NULL,
  `Telefono` VARCHAR(20) NOT NULL,
  `Id_user` INT NOT NULL,
  PRIMARY KEY (`Id_more_Data`),
  INDEX `FK_moreData_TO_User` (`Id_user` ASC) ,
  CONSTRAINT `FK_moreData_TO_User`
    FOREIGN KEY (`Id_user`)
    REFERENCES `new_schema`.`user` (`Id_User`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `new_schema`.`user_card`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_schema`.`user_card` (
  `Id_user_Card` INT NOT NULL,
  `Mascotas` VARCHAR(50) NOT NULL,
  `Presentacion` VARCHAR(250) NOT NULL,
  `Imagen` VARCHAR(100) NOT NULL,
  `Id_more_Data` INT NOT NULL,
  PRIMARY KEY (`Id_user_Card`),
  INDEX `FK_Card_TO_more_Data` (`Id_more_Data` ASC) ,
  CONSTRAINT `FK_Card_TO_more_Data`
    FOREIGN KEY (`Id_more_Data`)
    REFERENCES `new_schema`.`more_data` (`Id_more_Data`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;



-- -----------------------------------------------------
-- Consultas Admin
-- -----------------------------------------------------
-- Insert new Admin
INSERT INTO admin (id_admin, Username, Email, Password) VALUES (1,"Admin1","admin@gmail.com","passwordAdmin1");
-- -----------------
-- Select Admin por id
SELECT * from admin where id_Admin= 1;
-- -----------------
-- Update Admin por id
UPDATE admin SET username="AdminCorregido",email="nuevo_mail@gmail.com",password="passwordAdmin" WHERE id_admin=1;
-- -----------------
-- Delete Admin por id
DELETE FROM admin WHERE Id_admin= 1;
-- -----------------

-- -----------------------------------------------------
-- Consultas User
-- -----------------------------------------------------
-- Insert new User
INSERT INTO user (Id_User, User, Email, Password) VALUES ("1","Usuario1","usuario@gmail.com","passwordUsuario1");
-- -----------------
-- Select User por id
SELECT * from user WHERE user.id_user = 1;
-- -----------------
-- Select de todos los datos relacionados a User, antes es necesario que User_Card y more_data tengan datos
SELECT * from user inner JOIN (more_data, user_Card) on user_card.Id_user_Card = more_data.Id_more_Data WHERE user.id_user = 1;
-- -----------------
-- Update User por id
UPDATE user SET User="UsuarioModificado", Email="usuario@gmail.com", Password="passwordNueva" WHERE Id_user=1;
-- -----------------
-- Delete User por id
DELETE FROM user WHERE Id_user= 1;
-- -----------------

-- -----------------------------------------------------
-- Consultas User More_Data
-- -----------------------------------------------------
-- Insert new more_data
INSERT INTO more_data (Id_more_data, Name, LastName, Calle, Direccion, Piso_Depto, Ciudad, Provincia, Telefono, Id_User) VALUES (1,"Fernando","Herrera","Mariano Moreno",1258,"","General Roca","Rio Negro","2984788495",1) ;
-- -----------------
-- Select more_data por id
select * from more_data WHERE more_data.Id_more_Data = 1;
-- -----------------
-- Update more_data por id  
-- ej: el usuario cambia su direccion y calle
UPDATE more_data SET Calle="Picaflor", Direccion="457", Piso_Depto="", Ciudad="General Roca", Provincia="Rio Negro", Telefono="2984788495" WHERE Id_more_data=1;
-- -----------------
-- Delete more data
-- El usuario no podrá eliminar sus datos adicionales, a excepción de que rescinda su cuenta y admin lo elimine, mas 
-- adelante se puede ver la consulta que elimina todas las tablas realacionadas a el usuario.
-- -----------------

-- -----------------------------------------------------
-- Consultas User_card
-- -----------------------------------------------------
-- Insert new user_card
INSERT INTO user_card ( Mascotas, Presentacion, Imagen,Id_more_Data,Id_user_Card) VALUES ('Perros, Gatos, Hamsters', 'Se administrar medicacion a perros y gatos, hago paseos, tengo experiencia con reptiles ', '/images/Fernando.jpg',1,1) ;
-- -----------------
-- Select user_card por id
select * from user_card WHERE user_card.Id_user_card = 1;
-- -----------------
-- Update user_card por id
UPDATE user_card SET Mascotas="Perros, Gatos", Presentacion="Se administrar medicacion a perros y gatos, hago paseos, tengo experiencia con animales de granja", Imagen="/images/FernandoNuevaImg.jpg" WHERE Id_user_Card=1;
-- -----------------
-- Delete user_card por id
-- A diferencia de more_data, el usuario si podrá eliminar su user card cuando lo desee
DELETE FROM user_card WHERE Id_user_Card=1;
-- -----------------

-- -----------------------------------------------------
-- Consultas Contacto
-- -----------------------------------------------------
-- Insert new contacto
INSERT INTO contacto (Name, Email, Message, Id_Contacto) VALUES ('Patricio','patricio@gmail.com','Como recomendación, me gustaria poder comprar cosas para mis mascotas en la web',1);
-- -----------------
-- Select contacto por id
SELECT * from contacto WHERE contacto.Id_Contacto = 1;
-- -----------------
-- Update contacto por id
-- Nadie podrá editar los contactos.
-- -----------------
-- Delete contacto por id
DELETE FROM contacto WHERE Id_Contacto=1; 
-- -----------------

