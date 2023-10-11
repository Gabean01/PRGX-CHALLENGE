from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.ChallengeRepository import ChallengeRepository

class TestChallengeRepository(TestCase):
    session: Session
    challengeRepository: ChallengeRepository

    def setUp(self):
        super().setUp()
        self.session = create_autospec(Session)
        self.challengeRepository = ChallengeRepository(
            self.session
        )

    @patch("models.ChallengeModel.Challenge", autospec=True)
    def test_create(self, Challenge):
        challenge = Challenge(
                  users = "",
                  address = "",
                )
        self.challengeRepository.create(challenge)

        # Should call add method on Session
        self.session.add.assert_called_once_with(challenge)

    @patch("models.ChallengeModel.Challenge", autospec=True)
    def test_delete(self, Challenge):
        challenge = Challenge(id=1)
        self.ChallengeRepository.delete(challenge)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(challenge)

    @patch("models.ChallengeModel.Challenge", autospec=True)
    def test_get(self, Challenge):
        challenge = Challenge(id=1)
        self.challengeRepository.get(challenge)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.ChallengeModel.Challenge", autospec=True)
    def test_list(self, Challenge):
        self.challengeRepository.list(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.challengeRepository.list("Gary", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(
            Challenge
        ).filter_by.assert_called_once_with(
            users=""
        )

    @patch("models.ChallengeModel.Challenge", autospec=True)
    def test_update(self, Challenge):
        challenge = Challenge(users="")
        self.challengeRepository.update(id=1, challenge=challenge)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(challenge)