from abc import ABC, abstractmethod


class User:
    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.email_address = None
        self.age = None
        self.phone_number = None
        self.address = None


class UserBuilder(ABC):
    @abstractmethod
    def add_first_name(self, first_name):
        pass

    @abstractmethod
    def add_last_name(self, last_name):
        pass

    @abstractmethod
    def add_email_address(self, email_address):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_phone_number(self, phone_number):
        pass

    @abstractmethod
    def add_address(self, address):
        pass


class CustomUserBuilder(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def add_first_name(self, first_name):
        self.user.first_name = first_name

    def add_last_name(self, last_name):
        self.user.last_name = last_name

    def add_email_address(self, email_address):
        self.user.email_address = email_address

    def add_age(self, age):
        self.user.age = age

    def add_phone_number(self, phone_number):
        self.user.phone_number = phone_number

    def add_address(self, address):
        self.user.address = address


class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self.builder = builder

    def build_user(self, specs: dict) -> None:
        self.builder.add_first_name(specs["first_name"])
        self.builder.add_last_name(specs["last_name"])
        self.builder.add_email_address(specs["email_address"])
        self.builder.add_age(specs["age"])
        self.builder.add_phone_number(specs["phone_number"])
        self.builder.add_address(specs["address"])


test_specs = {
    "first_name": "Guillermo",
    "last_name": "Moran",
    "email_address": "g.a.moran.arreola@gmail.com",
    "age": 52,
    "phone_number": "6199999999",
    "address": "123 Main St",
}

builder = CustomUserBuilder()
director = UserDirector(builder)
director.build_user(test_specs)
user = builder.user
print(user.__dict__)
