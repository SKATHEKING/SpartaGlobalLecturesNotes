import pyodbc

class NwProducts:

    def __init__(self):
        self.server = '13.40.97.175'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_northwind = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                                  +self.server+";DATABASE="+self.database+";UID="+self.username+";PWD="+self.password)
        self.cursor = self.docker_northwind.cursor()

    def _sql_query(self, sql_query: str):
        return self.cursor.execute(sql_query)

    def print_all_product_records(self):
        query_records = self._sql_query("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        query_records = self._sql_query("SELECT * FROM Products")
        total_unit_price = []

        while True:
            record = query_records.fetchone()
            if record is None:
                break
            total_unit_price.append(record.UnitPrice)

        print(sum(total_unit_price)/len(total_unit_price))


products = NwProducts()
products.print_all_product_records()
products.print_average_unit_price()
