from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.AddressRepository import AddressRepository
from services.AddressService import AddressService

class TestAddressService(TestCase):
    addressRepository: AddressRepository
    addressService: AddressService

    def setUp(self):
        super().setUp()
        self.addressRepository = create_autospec(AddressRepository)
        self.addressService = AddressService(self.addressRepository)

    
    @patch(
        "schemas.pydantic.AddressSchema.AddressSchema",
        autospec=True,
    )
    def test_create(self, AddressSchema):
        address = AddressSchema()
        address.address_1 = "Tv 53a #65-70"
        address.address_2 = "T1 AP 1506"
        address.city = "Medellin"
        address.state ="Antioquia"
        address.zip ="050031"
        address.state ="Colombia"

        self.addressService.create(address)

        # Should call delete method on Address Repository
        self.addressRepository.create.assert_called_once() 
    
    def test_delete(self):
        self.addressService.delete(address_id=1)

        # Should call delete method on Address Repository
        self.addressRepository.delete.assert_called_once()

    def test_get(self):
        self.addressService.get(address_id=1)

        # Should call get method on Address Repository
        self.addressRepository.get.assert_called_once()   
       
    def test_list(self):
        name = "Address1"
        pageSize = 10
        startIndex = 2

        self.addressService.list(name, pageSize, startIndex)

        # Should call list method on Address Repository
        self.addressRepository.list.assert_called_once_with(
            name, pageSize, startIndex
        ) 


    @patch(
        "schemas.pydantic.UsersSchema.UserSchema",
        autospec=True,
    )      
    def test_update(self, UsersSchema):
        users = UsersSchema()
        users.firts_name = "Alexander"

        self.usersService.update(
            users_id=1, users_body=users
        )
        # Should call update method on Product Repository
        self.productRepository.update.assert_called_once()