'''
This is an abstract example of Loading in an ETL pipeline. 

Inspired from the "Introduction to Data Engineering" course on Datacamp.com
Author: Alex Nakagawa
'''
import pandas as pd

# Write the pandas DataFrame to parquet
pandas_df.to_parquet('pandas_df.parquet')

# Write the PySpark DataFrame to parquet
spark_df.write.parquet('spark_df.parquet')

# Finish the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine_dwh = sqlalchemy.create_engine(connection_uri)
# Transformation step, join with recommendations data
film_pdf_joined = film_pdf.join(recommendations)
# Finish the .to_sql() call to write to store.film
film_pdf_joined.to_sql("film", db_engine_dwh,
                       schema="store", if_exists="replace")
# Run the query to fetch the data
pd.read_sql("SELECT film_id, recommended_film_ids FROM store.film", db_engine_dwh)
