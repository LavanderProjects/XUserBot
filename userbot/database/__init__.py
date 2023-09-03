import json

class JsonBase:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            self.data = {
    "snips": [],
    "filters": [],
    "pmpermit": [],
    "gban": [],
    "gmute": []
}
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)
            return self.data
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def insert_record(self, table, record):
        self.data[table].append(record)
        self.save_data()

    def get_record_by_key(self, table, key, value):
        for record in self.data[table]:
            if record.get(key) == value:
                return record
        return None

    def update_record(self, table, key, value, new_data):
        record = self.get_record_by_key(table, key, value)
        if record:
            record.update(new_data)
            self.save_data()
        else:
            print("Kayıt bulunamadı.")

    def delete_record(self, table, key, value):
        record = self.get_record_by_key(table, key, value)
        if record:
            self.data[table].remove(record)
            self.save_data()
        else:
            print("Kayıt bulunamadı.")
