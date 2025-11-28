
import sqlite3
import pandas as pd
import os




csv_path = os.path.join('data_collection', 'gym_cleaned.csv')  
df = pd.read_csv(csv_path)
print(df.head())

db_path = os.path.join('database', 'gym.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)


conn = sqlite3.connect(db_path)


df.to_sql('gym', conn, if_exists='replace', index=False)
print("数据已成功插入 SQLite 数据库。")


cursor = conn.cursor()
result = cursor.execute("SELECT * FROM gym LIMIT 10").fetchall()
print("数据库中的前 10 行：")
print(result)


conn.commit()
conn.close()

