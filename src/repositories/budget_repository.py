
from user_repository import get_user_id_for_new_table
from database_connection import get_database_connection

class BudgetRepository:


    def __init__(self, connection):
        self._connection = connection

    def create_budget_table_for_user(self, userid):
        new_table = get_user_id_for_new_table
        cursor = self._connection.cursor()
        