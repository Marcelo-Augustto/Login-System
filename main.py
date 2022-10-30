#Login system with database

import pymysql.cursors
import bcrypt


class User():
    def __init__(self, username=None, password=None) -> None:
        try:
            self.username = username
            self.password = bcrypt.hashpw(password, bcrypt.gensalt())
        except:
            pass
    
    def insert_user(self) -> str:
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO users (name, password) VALUES ' \
                            '(%s, %s)'
                cursor.execute(sql, (self.username, self.password))
                connection.commit()
            
            return "User was registered successfully"
        except:
            return "Error... Something went wrong"

    def autenticate_user (self, username, password) -> bool:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM users WHERE name = %s'
            rows_num = cursor.execute(sql, (username))
            res = cursor.fetchall()

        if rows_num <= 0:
            return False

        for user in res:
            if  bcrypt.checkpw(str.encode(password), str.encode(user['password'])):
                return True
           
    def validate_user (self) -> bool:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM users WHERE name = %s'
            rows_num = cursor.execute(sql, (self.username))

        if rows_num <= 0:
            return True

        return False
    
    def get_users (self):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            res = cursor.fetchall()
        
        for user in  res:
            print(user)

if __name__ == '__main__':
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='test',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    status = True

    while status:
        print(" ")
        print("Menu")
        print("0 - Shut Down")
        print("1 - Register")
        print("2- Login ")
        print("3 - Show Users ")
        print(" ")
        action = input("Type the number of a action: ")
        action = action
        print(" ")

        if action == '0':
            status = False

        elif action == '1':
            print("Register")
            print(" ")
            user = input("Username: ")
            password = input("password: ")
            new_user = User(user, str.encode(password))
            print(" ")
            if new_user.validate_user():
                print(new_user.insert_user())
            else:
                print("Invalid username")

        elif action == '2':
            print("Login")
            print(" ")
            user = input("Username: ")
            password = input("password: ")
            print(" ")
            new_user = User()
            if new_user.autenticate_user(user, password):
                print("You loged in")
            else:
                print("invalid credentials")

        elif action == '3':
            print(" ")
            print('Users')
            user = User()
            user.get_users()

        else:
            print("Invalid Action")

    connection.close()
