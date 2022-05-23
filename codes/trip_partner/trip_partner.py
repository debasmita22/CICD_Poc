import os
import sys
import snowflake.connector

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
      "where Model_Name = '{0}' order by CREATION_DATE_TIME DESC;".format(model_name)
results = conn.cursor().execute(sql)

for rec in results:
    completeness_rate = float(rec[0])
    coverage = float(rec[1])
print("Completeness_Rate and Coverage for {0} - {1}, {2}".
      format(model_name, completeness_rate, coverage))

if round(completeness_rate, 2) < 95.00 or round(coverage, 2) < 95.00:
    raise Exception("Either completeness_rate or coverage is not satisfying")
    sys.exit(1)