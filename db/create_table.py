
import psycopg2
from config import config




def connect():
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
        

        # create table
        create_table(cur, conn)
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_table(cur, conn):

    cur.execute("""CREATE TABLE recipe_list(
        id integer PRIMARY KEY,
        recipe_name text,
        url text,
        category text,
        subcategory text,
        special_equipment text
    )
    """)
    conn.commit()

if __name__ == '__main__':
    connect()