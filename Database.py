import sqlite3
import time


class Connector:
    def __init__(self, database_name):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(database_name)
        self.cur = self.connection.cursor()

    # def __enter__(self):
    #     return self.cur

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def fill_table(self, timer):
        """execute a row of data to current cursor"""
        unix_time = time.time()
        self.cur.execute('INSERT INTO result VALUES (?, ?);', (unix_time, timer))

    def get_last_result(self):
        """execute a row of data to current cursor"""
        return self.cur.execute('ELECT * FROM result ORDER BY date DESC LIMIT 1;')

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS result("date" INTEGER, "timer" INTEGER);''')

    def commit(self):
        """commit changes to database"""
        self.connection.commit()