'''

1 - creates new recipe info table
id, title, ingredients, instructions, tags

2 - creates two new empty tables

tags
id, tag

recipes_tags
tag_id, recipe_id

3 - inserts data into tables


'''


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
        #cur = conn.cursor()
        
        # urls = query_for_urls(conn)

        # update_table(conn, urls)
       
        # close the communication with the PostgreSQL
        #cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')







if __name__ == '__main__':
    connect()