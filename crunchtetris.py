#!/usr/bin/python

from PyTom.Tetris import mysql
from PyTom.Tcrypt.Utilities import io
import sys
import getopt
import string

# main method
if __name__ == "__main__":
	
	name = ""
	streak = ""
	beg = ""
	end = ""
	output = ""
	call = ""
	
	i = [2,3,4]
	for x in i:
		conn = mysql.connect()
		cursor = conn.cursor()
		call = 'CALL player_perf_streaks((%s))' % x
		cursor.execute(call)
		result = cursor.fetchall()
	
		output += 'Longest Wrank Win Streaks in %sP Games, All-Time' % x 
		output += '\n\n'
		output += 'Player'.ljust(10)+'Stk'.ljust(5)+'Start'.ljust(18)+'End'+'\n'
		for row in result:
			name = str(row[0]).ljust(10)
			streak = str(row[1]).ljust(5)
			beg = str(row[2]).ljust(10)+'- '+str(row[3]).ljust(3)
			end = str(row[4]).ljust(10)+'- '+str(row[5]).ljust(3)
			output += name+streak+beg+'   '+end+'\n'
		output += '\n\n'
		conn.close()
	
	io.writeDataToFile('tetris',output)
	
	#print output
