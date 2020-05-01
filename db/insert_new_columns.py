import requests
from bs4 import BeautifulSoup

from scraper import prep_soup, scrape

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
        
        print('calling insert columns')
        insert_columns(cur, conn, 'recipe_list')
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_columns(cur, conn, table_name):
    ''' 
    inserts new columns into db
    title text
    tags text[] 
    instructions text[]
    ingredients text[][]
    '''

    cur.execute('ALTER TABLE %s ADD COLUMN %s text' % (table_name, 'title'))
    cur.execute('ALTER TABLE %s ADD COLUMN %s text[]' % (table_name, 'tags'))
    cur.execute('ALTER TABLE %s ADD COLUMN %s text[]' % (table_name, 'instructions'))
    cur.execute('ALTER TABLE %s ADD COLUMN %s text[][]' % (table_name, 'ingredients'))

    conn.commit()






if __name__ == "__main__":
    connect()