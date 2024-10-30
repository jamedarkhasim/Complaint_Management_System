import sqlite3

class ConnectionDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('complaints.db', check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.setup_table()

    def setup_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS complaints (
                ID INTEGER PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Address TEXT NOT NULL,
                Gender TEXT CHECK(Gender IN ('Male', 'Female')),
                Comment TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def List(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM complaints')
        return cursor.fetchall()

    def AddText(self, first_name, last_name, address, gender, comment):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO complaints (FirstName, LastName, Address, Gender, Comment)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, address, gender, comment))
        self.conn.commit()

    def DeleteComplaint(self, complaint_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM complaints WHERE ID = ?', (complaint_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
