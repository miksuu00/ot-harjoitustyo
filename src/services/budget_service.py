from repositories.user_repository import (
    UserRepository as default_user_repository
)
from user import User


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class BudgetService:

    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = default_user_repository

    def login(self, username, password):
        user = self._user_repository.get_user_by_name(username)
        if not user or user.password != password:
            raise InvalidCredentialsError(
                'Check you credentials! Invalid input!')
        self._user = user
        return user

    def create_user(self, username, password):
        existing_user = self._user_repository.get_user_by_name(username)
        if existing_user is None:
            raise UsernameExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        return user


budget_service = BudgetService()
