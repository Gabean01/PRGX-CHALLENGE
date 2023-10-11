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
        "schemas.pydantic.ChallengeSchema.ChallengeSchema",
        autospec=True,
    )
    def test_create(self, ChallengeSchema):
        challenge = ChallengeSchema()
        challenge.users = "Gary"
        challenge.address = "Tv 53a #65-70"
        

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
