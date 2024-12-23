import csv
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import List


class Contact:
    def __init__(
        self, full_name: str, email: str, phone_number: str, is_friend: bool
    ) -> None:
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_friend = is_friend


class FileReader(ABC):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @abstractmethod
    def read(self) -> str:
        pass


class ContactsAdapter(ABC):
    def __init__(self, data_source: FileReader) -> None:
        self.data_source = data_source

    @abstractmethod
    def get_contacts(self) -> List[Contact]:
        pass


class XMLContactsAdapter(ContactsAdapter):
    def get_contacts(self) -> List[Contact]:
        root = ET.fromstring(self.data_source.read())
        contacts = []

        for elem in root.iter():
            if elem.tag == "contact":
                contacts.append(
                    Contact(
                        full_name=elem.find("full_name").text,
                        email=elem.find("email").text,
                        phone_number=elem.find("phone_number").text,
                        is_friend=elem.find("is_friend").text.lower() == "true",
                    )
                )

        return contacts


class JSONContactsAdapter(ContactsAdapter):
    def get_contacts(self) -> List[Contact]:
        data_dict = json.loads(self.data_source.read())
        contacts = []

        for contact_data in data_dict["contacts"]:
            contacts.append(
                Contact(
                    full_name=contact_data["full_name"],
                    email=contact_data["email"],
                    phone_number=contact_data["phone_number"],
                    is_friend=contact_data["is_friend"],
                )
            )

        return contacts


class CSVContactsAdapter(ContactsAdapter):
    def get_contacts(self) -> List[Contact]:
        contacts = []

        for row in csv.reader(self.data_source.read(), delimiter=","):
            print(f"row: {",".join(row)}")

        return contacts


class XMLReader(FileReader):
    def read(self) -> str:
        with open(self.file_name, "r") as f:
            return f.read()


class JSONReader(FileReader):
    def read(self) -> str:
        with open(self.file_name, "r") as f:
            return f.read()


class CSVReader(FileReader):
    def read(self) -> str:
        with open(self.file_name, "r") as f:
            return f.read()


def print_contact_data(contacts_source: ContactsAdapter):
    print("=== START ===")
    for contact in contacts_source.get_contacts():
        print(contact)


"""
xml_reader = XMLReader("contacts.xml")
xml_adapter = XMLContactsAdapter(xml_reader)
print_contact_data(xml_adapter)

json_reader = JSONReader("contacts.json")
json_adapter = JSONContactsAdapter(json_reader)
print_contact_data(json_adapter)
"""

csv_reader = CSVReader("contacts.csv")
csv_adapter = CSVContactsAdapter(csv_reader)
print(csv_adapter.get_contacts())
