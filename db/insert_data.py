
import psycopg2
from config import config




def connect(csv_file, table_name):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        

        # insert the data into table
        insert_data(cur, conn, csv_file, table_name)
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_data(cur, conn, data, table):

    with open(data, 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, table, sep=',')

    conn.commit()

if __name__ == '__main__':
    csv = './data/recipe_data.csv'
    table = 'recipe_list'
    connect(csv, table)