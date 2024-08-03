import pymysql

# Query for creating a table
USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP
)"""


DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

if __name__ == '__main__':

    try:
        # Creating a connection to MySQL by using an object connect type
        connection = pymysql.Connect(host='127.0.0.1',
                        port=3306, user='root',
                        passwd='Ozkr64109*', db='pythondb')

        print('Connected to MySQL!')

        # If i used the following script, it isn't necessary to close the cursor
        with connection.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

    except pymysql.MySQLError as e:
        print(f"Was impossible to connect to MySQL: {e}")

    finally:
        # cursor.close()
        connection.close()
        print('Disconnected from MySQL!')



    