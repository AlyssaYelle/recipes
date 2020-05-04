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
        
        #create_table_as_select(conn)
        create_tags_recipes_table(conn)
        create_tags_table(conn)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_tags_table(conn):
    '''
    creates new table to list tags
    '''
    cur = conn.cursor()

    cur.execute("""CREATE TABLE tags(
        id integer PRIMARY KEY,
        tag_name text
    )
    """)
    conn.commit()

    cur.close()


def create_tags_recipes_table(conn):
    '''
    creates new table for tags_recipes joining
    '''
    cur = conn.cursor()

    cur.execute("""CREATE TABLE tags_recipes(
        tag_id integer,
        recipe_id integer,
        PRIMARY KEY (tag_id, recipe_id)
    )
    """)
    conn.commit()

    cur.close()


def create_table_as_select(conn):
    '''
    creates new table from recipes_list without unneccesary data
    '''
    cur = conn.cursor()

    cur.execute("""CREATE TABLE recipes AS
        SELECT title, ingredients, instructions, tags
        FROM recipe_list""")




if __name__ == '__main__':


    connect()