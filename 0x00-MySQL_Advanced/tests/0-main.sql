#!/bin/bash
# Make table and insert data

echo "SELECT * FROM users;" | mysql -uroot -p holberton
# ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist

cat 0-uniq_users.sql | mysql -uroot -p holberton
echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
# ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'

echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
