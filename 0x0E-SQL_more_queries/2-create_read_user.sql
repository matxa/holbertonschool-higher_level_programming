-- create hbtn_0c_2 database
-- user_0d_2 in hbnt_0c_2 database
-- give user only select privilage
CREATE DATABASE IF NOT EXISTS hbtn_0c_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON * . * TO 'user_0d_2'@'localhost';