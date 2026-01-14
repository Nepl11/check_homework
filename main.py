from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # тут валідація не вимагалась, просто зберігаємо ім'я
    pass


class Phone(Field):
    # ВАЖЛИВО: рівно 10 цифр, інакше ValueError
    def __init__(self, value: str):
        value = str(value)
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Додати телефон (рядок або Phone)."""
        phone_obj = phone if isinstance(phone, Phone) else Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        """Видалити телефон (за значенням)."""
        phone_str = phone.value if isinstance(phone, Phone) else str(phone)
        self.phones = [p for p in self.phones if p.value != phone_str]

    def edit_phone(self, old_phone, new_phone):
        """Замінити old_phone на new_phone. Якщо old_phone не знайдено -> ValueError."""
        old_str = old_phone.value if isinstance(old_phone, Phone) else str(old_phone)
        new_obj = new_phone if isinstance(new_phone, Phone) else Phone(new_phone)

        for i, p in enumerate(self.phones):
            if p.value == old_str:
                self.phones[i] = new_obj
                return

        raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        """Знайти телефон. Повертає об'єкт Phone або None."""
        phone_str = phone.value if isinstance(phone, Phone) else str(phone)
        for p in self.phones:
            if p.value == phone_str:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        """Додати Record у книгу (ключ = ім'я)."""
        self.data[record.name.value] = record

    def find(self, name):
        """Знайти запис за ім'ям. Повертає Record або None."""
        return self.data.get(str(name))

    def delete(self, name):
        """Видалити запис за ім'ям."""
        self.data.pop(str(name), None)
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # тут валідація не вимагалась, просто зберігаємо ім'я
    pass


class Phone(Field):
    # ВАЖЛИВО: рівно 10 цифр, інакше ValueError
    def __init__(self, value: str):
        value = str(value)
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Додати телефон (рядок або Phone)."""
        phone_obj = phone if isinstance(phone, Phone) else Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        """Видалити телефон (за значенням)."""
        phone_str = phone.value if isinstance(phone, Phone) else str(phone)
        self.phones = [p for p in self.phones if p.value != phone_str]

    def edit_phone(self, old_phone, new_phone):
        """Замінити old_phone на new_phone. Якщо old_phone не знайдено -> ValueError."""
        old_str = old_phone.value if isinstance(old_phone, Phone) else str(old_phone)
        new_obj = new_phone if isinstance(new_phone, Phone) else Phone(new_phone)

        for i, p in enumerate(self.phones):
            if p.value == old_str:
                self.phones[i] = new_obj
                return

        raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        """Знайти телефон. Повертає об'єкт Phone або None."""
        phone_str = phone.value if isinstance(phone, Phone) else str(phone)
        for p in self.phones:
            if p.value == phone_str:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        """Додати Record у книгу (ключ = ім'я)."""
        self.data[record.name.value] = record

    def find(self, name):
        """Знайти запис за ім'ям. Повертає Record або None."""
        return self.data.get(str(name))

    def delete(self, name):
        """Видалити запис за ім'ям."""
        self.data.pop(str(name), None)
