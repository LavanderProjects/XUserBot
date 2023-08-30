import sqlite3

class Database:
    def __init__(self):
        self.connection = None

    def connect(self, user_id):
        self.connection = sqlite3.connect(user_id)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.close()

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.connection.commit()

    def insert(self, table_name, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['?' for _ in data.values()])
        query = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()

    def select_all(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, data, condition):
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()



