from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.ChallengeRepository import ChallengeRepository
from services.ChallengeService import ChallengeService

class TestChallengeService(TestCase):
    challengeRepository: ChallengeRepository
    challengeService: ChallengeService

    def setUp(self):
        super().setUp()
        self.challengeRepository = create_autospec(ChallengeRepository)
        self.challengeService = ChallengeService(self.challengeRepository)

    
    @patch(
        "schemas.Schema.UsersSchema",
        "schemas.Schema.ChallengeSchema",
        "schemas.Schema.AddressSchema",
        autospec=True,
    )
    def test_create(self, ChallengeSchema, UsersSchema, AddressSchema):
        challenge = ChallengeSchema()
        user = UsersSchema()
        address = AddressSchema()

        user.firts_name = "Gary"
        user.last_name = "Bean"
        user.email = "gbeanrenteria@gmail.com"
        user.password ="123456789"

        address.address_1 = "Tv 53a #65-70"
        address.address_2 = "T1 AP 1506"
        address.city = "Medellin"
        address.state ="Antioquia"
        address.zip ="050031"
        address.state ="Colombia"

        challenge.user = user
        challenge.address = address
        

        self.challengeService.create(challenge)

        # Should call delete method on Challenge Repository
        self.challengeRepository.create.assert_called_once() 
    
    def test_delete(self):
        self.challengeService.delete(challenge_id=1)

        # Should call delete method on Challenge Repository
        self.challengeRepository.delete.assert_called_once()

    def test_get(self):
        self.challengeService.get(challenge_id=1)

        # Should call get method on Challenge Repository
        self.challengeRepository.get.assert_called_once()   
       
    def test_list(self):
        name = ""
        pageSize = 10
        startIndex = 2

        self.challengeService.list(name, pageSize, startIndex)

        # Should call list method on Challenge Repository
        self.challengeRepository.list.assert_called_once_with(
            name, pageSize, startIndex
        ) 
