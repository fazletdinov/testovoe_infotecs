"""Скрипт позволяет автоматически заполнить вашу базу
данных на основе sqlite3, данными из текстового файла RU.txt,
можете не запускать скрипт, так как база уже заполнена"""
import sqlite3

connect = sqlite3.connect('database/database.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS geoname
               (geonameid INTEGER PRIMARY KEY,
                name TEXT,
                asciiname TEXT,
                alternatenames TEXT,
                latitude REAL,
                longitude REAL,
                feature_class TEXT,
                feature_code TEXT,
                country_code TEXT,
                cc2 TEXT,
                admin1_code TEXT,
                admin2_code TEXT,
                admin3_code TEXT,
                admin4_code TEXT,
                population INTEGER,
                elevation INTEGER,
                dem INTEGER,
                timezone TEXT,
                modification_date TEXT
                )
               """)

data = []
with open("RU.txt", "r") as file:
    for line in file:
        line = line.strip().split('\t')
        data.append(line)

cursor.executemany("""INSERT INTO geoname
                   VALUES (?, ?, ?, ?, ?, ?, ?,
                   ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)
connect.commit()
cursor.execute("SELECT * FROM geoname")
print(cursor.fetchone())
cursor.close()
connect.close()
