import psycopg2
from config import config

def create_table():
    """ create tables in PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
        	user_id INT PRIMARY KEY
            user_name INT NOT NULL,
            user_phone_number VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE posts (
                post_id INT PRIMARY KEY,
                post_title VARCHAR(255) NOT NULL
                )
        """)

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

def insert_user(user_name):
    # insert a new user into the users table
    sql = """INSERT INTO users(user_name)
             VALUES(%s) RETURNING user_id;"""
    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name,))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user_id


def update_user(user_id, user_name):
    # update user name based on the user id
    sql = """ UPDATE users
                SET user_name = %s
                WHERE user_id = %s"""
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name, user_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def delete_user(user_id):
    #delete user by user id
    conn = None
    rows_deleted = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


def get_users():
    #query data from the users table
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT user_id, user_name FROM users ORDER BY user_name")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
	#create table
    create_table()
    #insert user
    insert_user("Adewale")
    #query user table
    get_users()
    #delete user
    deleted_rows = delete_user(2)
    print('The number of deleted rows: ', deleted_rows)