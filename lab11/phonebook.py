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
        raise Exception("[INFO] Error with config function!")
    return db


def act(commands):
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        cur.execute(commands)
        cur.close()
        connection.commit()
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    if connection is not None:
        connection.close()


while True:
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        c = int(input('1) Show\n2) Add\n3) List\n4) Que\n5) Del\n6) Quite\n'))
        if c == 1:
            try:
                cur.execute(f'SELECT * FROM show();')
                answer = cur.fetchall()
                print(answer)
            except:
                print("Error")
                cur.close()
                connection.commit()
                if connection is not None:
                    connection.close()
                break
        elif c == 2:
            f = True
            cur.execute(f'select * from show();')
            answer = cur.fetchall()
            name = str(input('Name:\n'))
            num = str(input('Number:\n'))
            for i in answer:
                if i[0] == name:
                    cur.execute(f"call add_user1('{name}', '{num}');")
                    f = False
                    break
            if f:
                cur.execute(f"call add_user('{name}', '{num}');")
        elif c == 3:
            t = True
            l = []
            n = int(input('Number of objects:\n'))
            for k in range(n):
                name = input(f'{k + 1}: Name: \n')
                num = input(f'{k + 1}: Number: \n')
                for j in num:
                    if '9' >= j >= '0':
                        continue
                    else:
                        l.append((name, num))
                        t = False
                        break
                if t:
                    f = True
                    cur.execute(f'select * from show();')
                    answer = cur.fetchall()
                    for i in answer:
                        if i[0] == name:
                            cur.execute(f"call add_user1('{name}', '{num}');")
                            f = False
                            break
                    if f:
                        cur.execute(f"call add_user('{name}', '{num}');")
            print("WRONG conntacts: ", l)
        elif c == 4:
            try:
                limit = int(input('Limit:\n'))
                offset = int(input('Offset:\n'))
                cur.execute(f"select * from que('{limit}', '{offset}');")
                answer = cur.fetchall()
                print(answer)
            except:
                print("Error")
                cur.close()
                connection.commit()
                if connection is not None:
                    connection.close()
                break
        elif c == 5:
            flag = int(input('1) By name\n 2) By number\n'))
            try:
                if flag == 1:
                    name = input('Name: \n')
                    cur.execute(f"call del('{name}');")
                else:
                    num = input('Number:\n')
                    cur.execute(f"call del1('{num}');")
            except:
                print("Error")
                cur.close()
                connection.commit()
                if connection is not None:
                    connection.close()
                break
        else:
            cur.close()
            connection.commit()
            if connection is not None:
                connection.close()
            break
        cur.close()
        connection.commit()
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    if connection is not None:
        connection.close()
