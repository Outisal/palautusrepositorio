from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password or not password_confirmation:
            raise UserInputError("Username, password and password confirmation are required")
        if len(username) < 3 or not username.isalpha():
            raise UserInputError("Username must contain only letters a-z and be at least three characters long")
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")
        if password.isalpha():
            raise UserInputError("Password cannot contain only letters")
        if password != password_confirmation:
            raise UserInputError("Password and password confirmation do not match")
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already in use")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
