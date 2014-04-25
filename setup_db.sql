# run me with mysql --force -u root -p < setup_db.sql

CREATE DATABASE demo;

CREATE USER 'demouser'@'localhost' IDENTIFIED BY '12345';
GRANT SELECT, UPDATE, INSERT, DELETE, EXECUTE, SHOW VIEW, CREATE, ALTER, INDEX, CREATE VIEW, CREATE TEMPORARY TABLES
ON demo.* TO 'demouser'@'localhost';

FLUSH PRIVILEGES;
