### SQLAlchemy : 
:: An Object Relational Mapping library for python. It provides a way to interact with relational databases using python objects instead of writing raw SQL queries. 

#### Working template
1. Define the database as python classes. 
2. The classes should be singular i.e. user.py will match to the table users. 
3. The class attributes will then be mapped to the columns in the database table.

### support 
SQLite, PostgreSQL , MySQL. 

### ALEMBIC :: 
Migrations : Detailed plans or instructions that help in safely making changes to the db structure without losing important data or breaking the database schema 
Alembic is SQLAlchemy database migration tool 

Usages 
1. Creating new tables 
2. Modifying the structure of existing tables 
3. Adding new columns. 

### Flask SQLAlchemy 
This is an extension to support usage of SQLAlchemy in flask applications.
Flask alembic is then the extension that sets up alembic commands in flask applications.  

alembic upgrade : making changes 
alembic downgrade : to support rollbacks. 



## JUST USING SQLALCHEMY 
1. pip install sqlalchemy alembic.  
2. Define our models.
3. Intialize alembic : create a directory for our alembic migrations : alembic init alembic : python -m alembic init alembic 
4. On creation of the alembic folder/files , edit the alembic.ini file to configure our database connection. Update 
'sqlachemy.url' =  set it to our db connection string/
5. Generate initial migration : alembic revision --autogenerate -m " tag migration message "
6. Apply the migration : alembic upgrade head 























