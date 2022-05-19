import os
import snowflake.connector

# import pandas as pd
model_name = 'PSP_FEE'

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

sql = "select Completeness_Rate,Coverage from model_metrics " \
      "where Model_Name = '{0}';".format(model_name)
results = conn.cursor().execute(sql)

# curs.execute("select getdate();")
# print("Result is here -- ")
# print(curs.fetchone()[0])

for rec in results:
    completeness_rate = rec[0]
    coverage = rec[1]
print("Completeness_Rate and Coverage for {0} - {1}, {2}".
      format(model_name, completeness_rate, coverage))

