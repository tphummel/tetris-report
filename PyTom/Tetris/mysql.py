#!/usr/bin/python
import MySQLdb

def connect():
	DATABASE = "shloginc_thenewtetris"
	USER ="dice"
	HOST = "localhost"
	PASSWORD = "dice"
	SOCKET = "/opt/lampp/var/mysql/mysql.sock"
	
	connection = MySQLdb.connect(host=HOST, db=DATABASE, user=USER, passwd=PASSWORD, unix_socket=SOCKET)
	
	return connection
