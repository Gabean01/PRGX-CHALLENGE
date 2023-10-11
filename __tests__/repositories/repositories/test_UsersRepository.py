from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.UsersRepository import UsersRepository

class TestUsersRepository(TestCase):
    session: Session
    usersRepository: UsersRepository

    def setUp(self):
        super().setUp()
        self.session = create_autospec(Session)
        self.usersRepository = UsersRepository(
            self.session
        )

    @patch("models.UsersModel.Users", autospec=True)
    def test_create(self, Users):
        users = Users(
                    firts_name = "Gary",
                    last_name = "Bean",
                    email = "gbeanrenteria@gmail.com",
                    password = "123456789",
                )
        self.usersRepository.create(users)

        # Should call add method on Session
        self.session.add.assert_called_once_with(users)

    @patch("models.UsersModel.Users", autospec=True)
    def test_delete(self, Users):
        users = Users(id=1)
        self.usersRepository.delete(users)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(users)

    @patch("models.UsersModel.Users", autospec=True)
    def test_get(self, Users):
        users = Users(id=1)
        self.usersRepository.get(users)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.UsersModel.Users", autospec=True)
    def test_list(self, Users):
        self.usersRepository.list(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.usersRepository.list("Gary", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(
            Users
        ).filter_by.assert_called_once_with(
            firts_name="Gary"
        )

    @patch("models.UsersModel.Users", autospec=True)
    def test_update(self, Users):
        users = Users(firts_name="Ray Dalio")
        self.usersRepository.update(id=1, users=users)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(users)