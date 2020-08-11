import re
import psycopg2
from config import config

def extract_names(file):
	file_open = open(file, "r")
	file_content = file_open.read()
	file_open.close()
	
	pattern = r"<td>([A-z]+)</td>"
	return re.findall(pattern, file_content)


def create_table():
    """ create tables in PostgreSQL database"""
    command = (
        """
        CREATE TABLE baby (
        	baby_id INT PRIMARY KEY
            baby_name VARCHAR(255) NOT NULL
          	)
        """
        )

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_baby_list(babies_list):
    #insert multiple babies into the baby table
    sql = "INSERT INTO babies(baby_name) VALUES(%s)"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql,baby_list)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_table()
    #insert user
    insert_user(extract_names("baby2008.html"))