import sqlparse as sql
import Tkinter
import tkFileDialog
import os
import Tkinter
import tkMessageBox

path = "indented_sql"
try:
	os.mkdir(path)
except OSError as error: 
	print "Directory Exists!"

finally:
	root = Tkinter.Tk()
	root.withdraw() 
	tempdir = ""
	currdir = os.getcwd()
	while len(tempdir) < 1:
		tempdir = tkFileDialog.askopenfilename( initialdir=currdir, title='Please select a file', filetypes=[("SQL file","*.sql")])	

		if len(tempdir) > 0:
			tkMessageBox.showinfo("Query Indented", "You can find your file at the following path: %s" % tempdir)
				
		elif tempdir == '': 
			tkMessageBox.showinfo("Exit", "Quitting software:")
			tkMessageBox.showinfo("Not able to open", "File You chose %s" % tempdir)
			os._exit(0)
		else:
			tkMessageBox.showinfo("Error", "You selected a different file extension!")
			os._exit(0)

	filename = tempdir
	outname = filename.split('/')[-1].split('.')[0]
	fileout = path + "/" + outname + '_indented.sql'
	print fileout
	fileQuery = open(filename, 'r')
	fileOutput = open(fileout, 'w')
	query = " ".join(fileQuery.readlines())

	fileQuery.close()
	query = query.replace('\t', '')
	query = query.replace('\n', ' ')
	query = query.replace('    ', ' ')
	#print query

	fileOutput.write(sql.format(query, reindent=True, keyword_case='upper'))
	fileOutput.close()
