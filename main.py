import pymysql

if __name__ == '__main__':
    pymysql.Connect(host='localhost',
                    port=3306, user='root',
                    passwd='', db='pythondb')

    