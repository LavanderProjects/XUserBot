import sqlite3
import json
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
    def db2json(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = self.cursor.fetchall()
        all_data = {}

        for table_name in table_names:
            self.cursor.execute(f"PRAGMA table_info({table_name[0]})")
            column_info = self.cursor.fetchall()

            column_dict = {}
            for column in column_info:
                column_name = column[1]
                column_data_type = column[2]
                column_dict[column_name] = column_data_type

            self.cursor.execute(f"SELECT * FROM {table_name[0]}")
            table_data = self.cursor.fetchall()
            data_list = []

            for row in table_data:
                data_dict = {}
                for i, column in enumerate(column_info):
                    data_dict[column[1]] = row[i]
                data_list.append(data_dict)

            all_data[table_name[0]] = {
                "_columns": column_dict,
                "_data": data_list
            }

        return all_data
    def json2db(self, all_data):
        for table_name, data_dict in all_data.items():
            if "_columns" in data_dict:
                column_names = list(data_dict["_columns"].keys())
                columns_sql = ', '.join([f"{column_name} {data_dict['_columns'][column_name]}" for column_name in column_names])
            else:
                first_data = data_dict["_data"][0]
                column_names = list(first_data.keys())
                columns_sql = ', '.join([f"{column_name} TEXT" for column_name in column_names])

            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})")

            for row in data_dict["_data"]:
                column_placeholders = ', '.join(['?'] * len(column_names))
                values = [row[column] for column in column_names]
                self.cursor.execute(f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({column_placeholders})", values)
        self.connection.commit()


