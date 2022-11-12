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
-- Consultas
-- -----------------------------------------------------

