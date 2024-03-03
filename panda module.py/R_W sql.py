import pandas as pd
import sqlalchemy

#________ to build connection with mysql ________
engine = sqlalchemy.create_engine('mysql+pymysql://root:1234@localhost:3306/new_schema')


#________read from sql table________
df = pd.read_sql_table("customer",engine)
print(df,"\n")

df = pd.read_sql_table("customer",engine,columns=["name","phone_no"])
print(df,"\n")  


#________query for specific output from table________
df = pd.read_sql_query("select id,name from new_schema.customer",engine)
print(df,"\n")

query = '''
  SELECT customer.name , customer.phone_no , orders.name , orders.amount 
  FROM new_schema.customer INNER JOIN new_schema.`orders` ON customer.id = orders.customer_id;
'''
df=pd.read_sql_query(query,engine)
print(df,"\n")


#________ write the content of other table into sql table________
# for that : 1) Both tables must have the same name of column 
#            2) Here csv table does not have id column , so sql table's id column should be auto incrementable 

df = pd.read_csv("panda module.py\customers.csv")
print(df,"\n")

df.rename(columns={
    'Customer Name':'name',
    'Customer Phone':'phone_no',
},inplace=True)

print(df,"\n")

df.to_sql(
    name='customer',    # database table name
    con=engine,          # connection
    if_exists='append',
    index=False
    )

new_df = pd.read_sql_table("customer",engine)
print(new_df,"\n")
#if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
#How to behave if the table already exists.
#fail: Raise a ValueError.
#replace: Drop the table before inserting new values.
#append: Insert new values to the existing table