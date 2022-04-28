import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('[INFO] ERROR with config file')
    return db




def create_table():
    commands = (
        """
        CREATE TABLE PhoneBook(
            user_name VARCHAR (20) UNIQUE NOT NULL,
            phone_numb VARCHAR (20) UNIQUE NOT NULL
        );
        """
    )
    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(commands)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection is not None:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


create_table()
