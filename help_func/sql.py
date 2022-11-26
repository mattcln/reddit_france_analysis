import sqlite3
import pandas as pd
from sqlalchemy import create_engine


def create_connection_cursor(db_name:str):
    connection = sqlite3.connect(f'{db_name}.db')
    print(f'Connection {db_name} created.')
    return connection.cursor()

def get_column_dtypes(df:pd.DataFrame):
    dataList = []
    for x in df.dtypes:
        if(x == 'int64'):
            dataList.append('int')
        elif (x == 'float64'):
            dataList.append('float')
        elif (x == 'bool'):
            dataList.append('boolean')
        else:
            dataList.append('varchar')
    return dataList

def create_table_from_df(name_db:str, df:pd.DataFrame):
    columns_names = list(df.columns.values)
    columns_types = get_column_dtypes(df)
    create_table_statement = f'CREATE TABLE IF NOT EXISTS {name_db} (index int,'
    for i in range(len(columns_types)):
        create_table_statement = create_table_statement + '\n' + columns_names[i] + ' ' + columns_types[i] + ','
    return (create_table_statement[:-1] + ' );')

def insert_df_table(path_db:str, table_name:str, df:pd.DataFrame):
    engine = create_engine(path_db)
    df.to_sql(table_name, con=engine, if_exists='append')
    return engine
