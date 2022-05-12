import psycopg2
from configparser import ConfigParser
import csv

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


def main(commands):
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(commands)
        cursor.close()
        connection.commit()
        # with cursor.cursor() as cursor:
        #     cursor.execute(commands)
    except Exception as e:
        print(str(e))
    finally:
        if connection is not None:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def add_num(user_name, phone_numb):
    commands = (
        f"""
		INSERT INTO phonebook(user_name, phone_numb)
		VALUES('{user_name}', '{phone_numb}');
		"""
    )
    main(commands)


def del_num(user_name):
    commands = (
        f"""
		DELETE FROM phonebook WHERE phonebook.username = '{user_name}';
		"""
    )
    main(commands)


def change_num(user_name, phone_numb):
    commands = (
        f"""
		UPDATE phonebook SET phone_numb = '{phone_numb}' WHERE user_name = '{user_name}';
		"""
    )
    main(commands)


def change_name(user_name, phone_numb):
    commands = (
        f"""
		UPDATE phonebook SET user_name = '{user_name}' WHERE phone_numb = '{phone_numb}';
		"""
    )
    main(commands)


def show(list):
    commands = [
        """
        select * from phonebook;
        """,
        """
        select * from phonebook
        order by user_name;
        """,
        """
        select * from phonebook
        order by phone_numb;
        """
    ]
    connection = None
    try:
        params = config()
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(commands[list])
        print(*cursor.fetchall(), '\n')
        cursor.close()
        # with connection.cursor() as cursor:
        #     cursor.execute(commands[list])
        #     print(cursor.fetchall(), '\n')
        connection.commit()
    except Exception as e:
        print(str(e))
    if connection is not None:
        connection.close()


while True:
    station = int(input('1) Add a Person to the PhoneBook\n2) Delete a Person from the PhoneBook\n'
                        '3) Update the PhoneBook\n4) Exit\n5) List of the PhoneBook\n6) Add from CSV file\n'))
    if station == 1:
        user_name = str(input('Name:\n'))
        phone_numb = str(input('Phone Number:\n'))
        try:
            add_num(user_name, phone_numb)
            print("[INFO] The person has been added successfully!\n")
        except:
            print("[INFO] Error with first station")
            break
    elif station == 2:
        user_name = str((input('Name:\n')))
        try:
            del_num(user_name)
            print("[INFO] The person has been deleted successfully!\n")
        except:
            print("[INFO] Error with second station")
            break
    elif station == 3:
        ch = int(input('1) Change Name\n2) Change Phone number\n'))
        try:
            if ch == 1:
                phone_numb = str(input('Phone number:\n'))
                user_name = str(input('Name:\n'))
                change_name(user_name, phone_numb)
            else:
                user_name = str(input('Name:\n'))
                phone_numb = str(input('Phone number:\n'))
                change_num(user_name, phone_numb)
            print("[INFO] The PhoneBook has been updated successfully!\n")
        except:
            print("[INFO] Error with third station")
            break
    elif station == 4:
        print("[INFO] Exiting...\n")
        break
    elif station == 5:
        list = int(input(
            'List of the PhoneBook: \nPress 0 to sort by date\n Press 1 to sort by Name\n Press 2 to sort by Phone number\n'))
        show(list)
    elif station == 6:
        with open("data.csv") as f:
            read = csv.reader(f)
            for i in read:
                add_num(i[0], i[1])
