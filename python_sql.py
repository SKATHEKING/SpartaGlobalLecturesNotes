import pyodbc as pyodbc

server = '13.40.97.175'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


docker_northwind = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                                  +server+";DATABASE="+database+";UID="+username+";PWD="+password)
cursor = docker_northwind.cursor()


rows = cursor.execute('SELECT * FROM Products')

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)

