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
-- Table `mydb`.`artista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`artista` (
  `id_artista` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NULL,
  `genero` VARCHAR(50) NULL,
  PRIMARY KEY (`id_artista`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`album` (
  `id_album` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(150) NULL,
  `ano_lancamento` INT NULL,
  `id_artista` INT NULL,
  `artista_id_artista` INT NOT NULL,
  PRIMARY KEY (`id_album`),
  INDEX `fk_album_artista_idx` (`artista_id_artista` ASC) VISIBLE,
  CONSTRAINT `fk_album_artista`
    FOREIGN KEY (`artista_id_artista`)
    REFERENCES `mydb`.`artista` (`id_artista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`musica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`musica` (
  `id_musica` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(80) NULL,
  `duracao` VARCHAR(10) NULL,
  `id_album` INT NULL,
  `album_id_album` INT NOT NULL,
  PRIMARY KEY (`id_musica`),
  INDEX `fk_musica_album1_idx` (`album_id_album` ASC) VISIBLE,
  CONSTRAINT `fk_musica_album1`
    FOREIGN KEY (`album_id_album`)
    REFERENCES `mydb`.`album` (`id_album`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist` (
  `id_playlist` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `id_usuario` INT NULL,
  PRIMARY KEY (`id_playlist`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `playlist_id_playlist` INT NOT NULL,
  PRIMARY KEY (`id_usuario`),
  INDEX `fk_usuario_playlist1_idx` (`playlist_id_playlist` ASC) VISIBLE,
  CONSTRAINT `fk_usuario_playlist1`
    FOREIGN KEY (`playlist_id_playlist`)
    REFERENCES `mydb`.`playlist` (`id_playlist`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`musica_playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`musica_playlist` (
  `id_musica` INT NULL,
  `id_playlist` INT NULL,
  `playlist_id_playlist` INT NOT NULL,
  `musica_id_musica` INT NOT NULL,
  INDEX `fk_musica_playlist_playlist1_idx` (`playlist_id_playlist` ASC) VISIBLE,
  INDEX `fk_musica_playlist_musica1_idx` (`musica_id_musica` ASC) VISIBLE,
  CONSTRAINT `fk_musica_playlist_playlist1`
    FOREIGN KEY (`playlist_id_playlist`)
    REFERENCES `mydb`.`playlist` (`id_playlist`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_musica_playlist_musica1`
    FOREIGN KEY (`musica_id_musica`)
    REFERENCES `mydb`.`musica` (`id_musica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
