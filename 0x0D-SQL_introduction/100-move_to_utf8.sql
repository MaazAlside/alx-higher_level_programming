-- script that converts hbtn_0c_0 database to UTF8
USE hbtn_0c_0;
ALTER TABLE first_table
MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

