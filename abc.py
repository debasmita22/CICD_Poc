import os
import snowflake.connector
# import pandas as pd

# print("sf_username -> {0}".format(os.environ['sf_username']))
# print("sf_password -> {0}".format(os.environ['sf_password']))

sf_username = os.environ['sf_username']
sf_password = os.environ['sf_password']
sf_account = os.environ['sf_account']
sf_wh = os.environ['sf_wh']
sf_db = os.environ['sf_db']
sf_schema = 'EY'

conn = snowflake.connector.connect(
                user=sf_username,
                password=sf_password,
                account=sf_account,
                warehouse=sf_wh,
                database=sf_db,
                schema=sf_schema
                )

curs = conn.cursor()
curs.execute("select getdate();")
print("Result is here -- ")
print(curs.fetchone()[0])