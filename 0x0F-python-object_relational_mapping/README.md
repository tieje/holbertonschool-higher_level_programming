Project for learning about sqlalchemy

IF YOU DON'T KNOW THE PASSWORD TO THE ROOT USER FOR YOUR SSH INSTANCE, follow these instructions.
After sshing into your instance:

service mysql stop

sudo mysqld_safe --skip-grant-tables --skip-syslog --skip-networking

This terminal will lock up so open another terminal and ssh from there.

mysql -u root

ALTER USER 'root'@'localhost' IDENTIFIED BY 'fullmetal';

exit

service mysql stop

service mysql start

mysql -u root -p


BELOW IS HOW TO BUILD YOUR OWN INSTANCE IN DOCKER ON A LINUX DESKTOP.

docker run --privileged --name=fullmetal holbertonschool/ubuntu-1404-python3:latest

Open a second terminal and run this to get into the container

docker exec -it fullmetal bash

service mysql stop

sudo mysqld_safe --skip-grant-tables --skip-syslog --skip-networking

The terminal will lock up, so you'll need to open up a third terminal with

docker exec -it fullmetal bash

service mysql start

mysql -u root

Update the password with whatever you want.

UPDATE mysql.user SET authentication_string=PASSWORD('password') WHERE User='root';
FLUSH PRIVILEGES;

exit

service mysql stop

service mysql start

mysql -u root -p

You should be able to log in an out of the container now.
This container is equipped with git so it's possible to pull and then run your scripts from there.

To determine mysql status, use:
service mysql status

