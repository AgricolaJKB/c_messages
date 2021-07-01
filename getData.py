import mariadb
import sys
import datetime
import pandas as pd
from env import env


def getData(day=None):
    if day is None:
        today = datetime.date.today()
        time_filter = today - datetime.timedelta(days=int(env('TIMEDELTA')))
    else:
        time_filter = day

    # db config, connect to mariaDB-database
    hostname = 'localhost'
    username = env('DB_USERNAME')
    password = env('DB_PASSWORD')
    database = env('DB_DATABASE')
    port = int(env('DB_PORT'))

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
