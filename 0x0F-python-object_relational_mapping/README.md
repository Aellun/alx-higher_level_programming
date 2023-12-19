Project name: 0x0F. Python - Object-relational mapping

This Project covers the following topics:
>>Object-relational mappers
>>mysqlclient/MySQLdb documentation
>>mysqlclient/MySQLdb
>>Introduction to SQLAlchemy
>>Flask SQLAlchemy
>>Python SQLAlchemy Cheatsheet
>>SQLAlchemy ORM 
>>Python Virtual Environments: A primer

Tasks
0-select_states.py
	a script that lists all states from the database 	hbtn_0e_0_usa:

	Your script should take 3 arguments: mysql username, mysql 		password and database name (no argument validation needed)
	You must use the module MySQLdb (import MySQLdb)
	Your script should connect to a MySQL server running on 	localhost at port 3306
	Results must be sorted in ascending order by states.id
	Results must be displayed as they are in the example below
	Your code should not be executed when imported
	
1-filter_states.sql
	 a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

	Your script should take 3 arguments: mysql username, mysql 	password and database name (no argument validation needed)
	You must use the module MySQLdb (import MySQLdb)
	Your script should connect to a MySQL server running on localhost at port 3306
	Results must be sorted in ascending order by states.id
	Results must be displayed as they are in the example below
	Your code should not be executed when imported
	
 2-my_filter_states.py
 	a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

	Your script should take 4 arguments: mysql username, mysql 	password, database name and state name searched (no argument 	validation needed)
	You must use the module MySQLdb (import MySQLdb)
	Your script should connect to a MySQL server running on localhost at port 3306
	You must use format to create the SQL query with the user input
	Results must be sorted in ascending order by states.id
	Results must be displayed as they are in the example below
	Your code should not be executed when imported
	
3-my_safe_filter_states.py
	a script that takes in arguments and displays all values in 	the states table of hbtn_0e_0_usa where name matches the argument. 	But this time, write one that is safe from MySQL injections!

	Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
	You must use the module MySQLdb (import MySQLdb)
	Your script should connect to a MySQL server running on localhost at port 3306
	Results must be sorted in ascending order by states.id
	Results must be displayed as they are in the example below
	Your code should not be executed when imported
	

4-cities_by_state.py
	script that lists all cities from the database hbtn_0e_4_usa

	Your script should take 3 arguments: mysql username, mysql 	password and database name
	You must use the module MySQLdb (import MySQLdb)
	Your script should connect to a MySQL server running on localhost at port 3306
	Results must be sorted in ascending order by cities.id
	You can use only execute() once
	Results must be displayed as they are in the example below
	Your code should not be executed when imported
	
	
##more
