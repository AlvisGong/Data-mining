import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.100\\sql;DATABASE=testDB;UID=sa;PWD=myPassword')
print cnxn