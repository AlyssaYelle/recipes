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
        #cur = conn.cursor()
        
        urls = query_for_urls(conn)

        update_table(conn, urls)
       
        # close the communication with the PostgreSQL
        #cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')




def query_for_urls(conn):
    ''' queries table to get list of urls '''

    # create a cursor
    cur = conn.cursor()

    # execute query
    cur.execute("""SELECT url from recipe_list where title is null""")

    urls = [url[0] for url in cur.fetchall()]
    # cur.fetchall() on its own returns list of lists -- actual url string is in 0th element of sublist

    # close communications
    cur.close()

    return urls

def update_record_with_recipe_data(conn, cur, url):
    ''' scrapes data for given url and updates record '''

    print('updating record with url = ', url)

    url_soup = prep_soup(url)
    recipe_data = scrape(url_soup)

    sql_update_query = """Update recipe_list set title = %s, tags = %s, instructions = %s, ingredients = %s where url = %s"""
    cur.execute(sql_update_query, (recipe_data['title'], recipe_data['tags'], recipe_data['instructions'], recipe_data['ingredients'], url))
    conn.commit()
    

def update_table(conn, urls_list):
    ''' updates all records with recipe data '''

    # create a cursor
    cur = conn.cursor()

    # loop over urls and scrape recipe data
    for url in urls_list:
        update_record_with_recipe_data(conn, cur, url)
    

    # close communications
    cur.close()


if __name__ == '__main__':
    connect()



