-- MySQL Script generated by MySQL Workbench
-- Tue Jun  6 20:24:37 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `userName` VARCHAR(15) NOT NULL,
  `userPass` VARCHAR(255) NOT NULL,
  `reviewsNum` INT NOT NULL,
  `role` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `productName` VARCHAR(50) NOT NULL,
  `price` DECIMAL NOT NULL,
  `from_class` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`review` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_by` INT NOT NULL,
  `for_product` INT NOT NULL,
  `content` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `review_by_idx` (`created_by` ASC) VISIBLE,
  INDEX `for_product_idx` (`for_product` ASC) VISIBLE,
  CONSTRAINT `created_by`
    FOREIGN KEY (`created_by`)
    REFERENCES `mydb`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `for_product`
    FOREIGN KEY (`for_product`)
    REFERENCES `mydb`.`product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `className` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`product_in_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`product_in_category` (
  `product_id` INT NOT NULL,
  `product_class_id` INT NOT NULL,
  PRIMARY KEY (`product_id`, `product_class_id`),
  INDEX `fk_product_has_product_class_product_class1_idx` (`product_class_id` ASC) VISIBLE,
  INDEX `fk_product_has_product_class_product1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_product_has_product_class_product1`
    FOREIGN KEY (`product_id`)
    REFERENCES `mydb`.`product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_has_product_class_product_class1`
    FOREIGN KEY (`product_class_id`)
    REFERENCES `mydb`.`categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
