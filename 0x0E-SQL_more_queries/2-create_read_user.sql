--  creates the database hbtn_0d_2 and the user user_0d_2
CREATE USER if not EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_2_pwd';
CREATE DATABASE if not EXISTS hbtn_0c_0;
GRANT SELECT ON hbtn_0c_0.* TO 'user_0d_2'@'localhost';

