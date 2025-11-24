# %% [markdown]
# # Data Preprocessing: Create DB and Load CSV into SQLite

# %%
import sqlite3
import pandas as pd
import os

df = pd.read_csv(r"C:\Users\erxat\OneDrive\Documents\ST CLAIR 主要的\111 python 周一+周五（下）\big project\processing\us_census_income_data_clean.csv")
df.head()

# %%
import os
import sqlite3


db_path = os.path.join('..', 'database', 'income.db')


os.makedirs(os.path.dirname(db_path), exist_ok=True)


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
)
""")

conn.commit()
print("Database and table created successfully!")

# %%
conn = sqlite3.connect('income.db')

df.to_sql('income', conn, if_exists='replace', index=False)

# %%
# Insert data into income table
df.to_sql('income', conn, if_exists='append', index=False)
print("Data inserted successfully.")

# %%
cursor.execute("SELECT * FROM income").fetchall()

# %%
conn.commit()
conn.close()


