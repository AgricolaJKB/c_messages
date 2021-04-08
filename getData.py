import mariadb
import sys
import datetime
import pandas as pd
from env import env


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

def getData(day=yesterday):
    # db config
    hostname = 'localhost'
    username = env('DB_USERNAME')
    password = env('DB_PASSWORD')  # your password
    database = env('DB_DATABASE')
    port = int(env('DB_PORT'))

    # connect to db
    try:
        connection = mariadb.connect(host=hostname, user=username, password=password, database=database, port=port)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # get data
    df = pd.read_sql_query(f"""SELECT * FROM {env('DB_TABLE')} WHERE eintragungsdatum = '{yesterday}' AND NOT region = 'Deutschland';""", connection)

    # close db connection
    connection.close()

    # return output
    return df


if __name__ == '__main__':
    print(getData().subtitle)