from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.UsersRepository import UsersRepository
from services.UsersService import UsersService

class TestUsersService(TestCase):
    usersRepository: UsersRepository
    usersService: UsersService

    def setUp(self):
        super().setUp()
        self.usersRepository = create_autospec(UsersRepository)
        self.usersService = UsersService(self.usersRepository)

    
    @patch(
        "schemas.Schema.UsersSchema",
        autospec=True,
    )
    def test_create(self, UsersSchema):
        users = UsersSchema()
        users.firts_name = "Gary"
        users.last_name = "Bean"
        users.email = "gbeanrenteria@gmail.com"
        users.password ="123456789"

        self.usersService.create(users)

        # Should call delete method on Users Repository
        self.usersRepository.create.assert_called_once() 
    
    def test_delete(self):
        self.usersService.delete(users_id=1)

        # Should call delete method on Users Repository
        self.usersRepository.delete.assert_called_once()

    def test_get(self):
        self.usersService.get(users_id=1)

        # Should call get method on Users Repository
        self.usersRepository.get.assert_called_once()   
       
    def test_list(self):
        name = "Users1"
        pageSize = 10
        startIndex = 2

        self.usersService.list(name, pageSize, startIndex)

        # Should call list method on Users Repository
        self.usersRepository.list.assert_called_once_with(
            name, pageSize, startIndex
        ) 


    @patch(
        "schemas.Schema.UsersSchema",
        autospec=True,
    )      
    def test_update(self, UsersSchema):
        users = UsersSchema()
        users.firts_name = "Alexander"

        self.usersService.update(
            users_id=1, users_body=users
        )
        # Should call update method on Users Repository
        self.usersRepository.update.assert_called_once()