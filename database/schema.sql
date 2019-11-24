-- MySQL Script generated by MySQL Workbench
-- Sun Nov 24 09:17:55 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gitlabrs
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gitlabrs
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gitlabrs` DEFAULT CHARACTER SET utf8 ;
USE `gitlabrs` ;

-- -----------------------------------------------------
-- Table `gitlabrs`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gitlabrs`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL COMMENT 'Gitlab username',
  `access_token` VARCHAR(128) NULL COMMENT 'Retrieved via OAuth.',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gitlabrs`.`Type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gitlabrs`.`Type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gitlabrs`.`Badge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gitlabrs`.`Badge` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  `image` VARCHAR(255) NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gitlabrs`.`Badge_has_Type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gitlabrs`.`Badge_has_Type` (
  `Badge_id` INT NOT NULL,
  `Type_id` INT NOT NULL,
  PRIMARY KEY (`Badge_id`, `Type_id`),
  INDEX `fk_Badge_has_Type_Type1_idx` (`Type_id` ASC) VISIBLE,
  INDEX `fk_Badge_has_Type_Badge_idx` (`Badge_id` ASC) VISIBLE,
  CONSTRAINT `fk_Badge_has_Type_Badge`
    FOREIGN KEY (`Badge_id`)
    REFERENCES `gitlabrs`.`Badge` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Badge_has_Type_Type1`
    FOREIGN KEY (`Type_id`)
    REFERENCES `gitlabrs`.`Type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gitlabrs`.`User_has_Badge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gitlabrs`.`User_has_Badge` (
  `User_id` INT NOT NULL,
  `Badge_id` INT NOT NULL,
  `earned_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`User_id`, `Badge_id`),
  INDEX `fk_User_has_Badge_Badge1_idx` (`Badge_id` ASC) VISIBLE,
  INDEX `fk_User_has_Badge_User1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_User_has_Badge_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `gitlabrs`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Badge_Badge1`
    FOREIGN KEY (`Badge_id`)
    REFERENCES `gitlabrs`.`Badge` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
