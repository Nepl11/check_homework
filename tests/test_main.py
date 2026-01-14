import pytest
from collections import UserDict

from main import Field, Name, Phone, Record, AddressBook


def test_class_hierarchy():
    assert 'Field' in globals() or Field is not None
    assert issubclass(Name, Field)
    assert issubclass(Phone, Field)
    assert isinstance(Record('A'), Record)
    assert issubclass(AddressBook, UserDict)


def test_phone_validation_valid():
    p = Phone('0123456789')
    assert p.value == '0123456789'


@pytest.mark.parametrize('bad', ['123', 'abcdefghij', '12345678901', '12345-6789'])
def test_phone_validation_invalid(bad):
    with pytest.raises(ValueError):
        Phone(bad)


def test_required_methods_exist():
    for m in ('add_phone', 'remove_phone', 'edit_phone', 'find_phone'):
        assert hasattr(Record, m), f"Record missing {m}"

    for m in ('add_record', 'find', 'delete'):
        assert hasattr(AddressBook, m), f"AddressBook missing {m}"


def test_addressbook_functionality():
    ab = AddressBook()
    rec = Record('Bob')
    rec.add_phone('0123456789')

    ab.add_record(rec)
    found = ab.find('Bob')
    assert isinstance(found, Record)

    assert ab.find('NonExistent') is None

    ab.delete('Bob')
    assert ab.find('Bob') is None

    # deleting non-existent should not raise
    ab.delete('Nobody')


def test_record_phone_operations():
    r = Record('Alice')
    r.add_phone('0123456789')
    p = r.find_phone('0123456789')
    assert isinstance(p, Phone)

    assert r.find_phone('0987654321') is None

    # edit existing
    r.edit_phone('0123456789', '0987654321')
    assert r.find_phone('0123456781') is None
    assert r.find_phone('0987654321') is not None

    # editing non-existent should raise
    with pytest.raises(ValueError):
        r.edit_phone('0000000000', '1111111111')

    # remove phone
    r.remove_phone('0987654321')
    assert r.find_phone('0987654321') is None
