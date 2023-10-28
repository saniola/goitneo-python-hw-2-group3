from field import Field
from utils.is_valid_phone import is_valid_phone

class Phone(Field):
    def __init__(self, phone):
        if not is_valid_phone(phone):
            raise ValueError("Error: The phone number must be 10 digits")
        super().__init__(phone)
