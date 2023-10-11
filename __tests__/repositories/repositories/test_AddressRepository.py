from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.AddressRepository import AddressRepository

class TestAddressRepository(TestCase):
    session: Session
    addressRepository: AddressRepository

    def setUp(self):
        super().setUp()
        self.session = create_autospec(Session)
        self.addressRepository = AddressRepository(
            self.session
        )

    @patch("models.AddressModel.Address", autospec=True)
    def test_create(self, Address):
        address = Address(
                    address_1 = "tv 53a #65-70",
                    address_2 = "t1 ap 1506",
                    city = "Medellin",
                    state = "Antioquia",
                    zip = "050031"
                    country = "Colombia"
                )
        self.addressRepository.create(address)

        # Should call add method on Session
        self.session.add.assert_called_once_with(address)

    @patch("models.AddressModel.Address", autospec=True)
    def test_delete(self, Address):
        address = Address(id=1)
        self.addressRepository.delete(address)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(address)

    @patch("models.AddressModel.Users", autospec=True)
    def test_get(self, Address):
        address = Address(id=1)
        self.addressRepository.get(address)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.AddressModel.Address", autospec=True)
    def test_list(self, Address):
        self.addressRepository.list(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.addressRepository.list("tv 53a #65-70", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(
            Address
        ).filter_by.assert_called_once_with(
            address_1="tv 53a #65-70"
        )

    @patch("models.AddressModel.Address", autospec=True)
    def test_update(self, Address):
        address = Address(addres_1="Center mall")
        self.addressRepository.update(id=1, address=address)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(address)