import mariadb
import sys
import os
import datetime
import pandas as pd

def getData(day=None):
    if day is None:
        today = datetime.date.today()
        time_filter = today - datetime.timedelta(days=int(os.environ.get('TIMEDELTA')))
    else:
        time_filter = day
    
    # db config, connect to mariaDB-database
    hostname = 'localhost'
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    database = os.environ.get('DB_DATABASE')
    port = int(os.environ.get('DB_PORT'))

    # connect to db
    try:
        connection = mariadb.connect(host=hostname, user=username, password=password, database=database, port=port)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # get data
    df = pd.read_sql_query(
        f"""SELECT * FROM {env('DB_TABLE')} WHERE eintragungsdatum = '{time_filter}' AND NOT region = 'Deutschland';""",
        connection)

    # close db connection
    connection.close()

    # return output
    return df


if __name__ == '__main__':
    print(getData().subtitle)
