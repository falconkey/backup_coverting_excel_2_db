import sqlite3
import pandas as pd

con = sqlite3.connect('sv.db')
wb = pd.read_excel('ssc_full_v02.xlsx',sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()