from database_connection import get_database_connection


class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM user;')

    def get_user_by_name(self, username):
        cursor = self._connection.cursor()
        name = cursor.execute(
            'SELECT * FROM users WHERE username = ?', (username,))
        return name.fetchone()

    def create_new_user(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO user (username, password) VALUES (:username, :password)',
                       {'username': username, 'password': password})
        self._connection.commit()

    def check_credentials(self, username, password):
        cursor = self._connection.cursor()
        query = cursor.execute('SELECT * NAME FROM user WHERE username=:username AND password=:password',
                               {'username': username, 'password': password})
        return query.fetchone()
