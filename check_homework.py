#!/usr/bin/env python3
"""Simple runner that performs 30 basic checks against `main.py`.
This is not a pytest suite — it prints a concise pass/fail summary.
"""
import traceback
import sys

try:
    import main
except Exception:
    print("Failed to import main.py:")
    traceback.print_exc()
    sys.exit(2)

from collections import UserDict


tests = []


def add_test(fn):
    tests.append(fn)
    return fn


@add_test
def t1_field_exists():
    assert hasattr(main, 'Field')


@add_test
def t2_name_is_subclass():
    assert issubclass(main.Name, main.Field)


@add_test
def t3_phone_is_subclass():
    assert issubclass(main.Phone, main.Field)


@add_test
def t4_record_exists():
    r = main.Record('X')
    assert isinstance(r, main.Record)


@add_test
def t5_addressbook_is_userdict():
    assert issubclass(main.AddressBook, UserDict)


@add_test
def t6_phone_valid_saved():
    p = main.Phone('0123456789')
    assert p.value == '0123456789'


@add_test
def t7_phone_invalid_chars():
    try:
        main.Phone('abcdefghij')
        raise AssertionError('Expected ValueError')
    except ValueError:
        pass


@add_test
def t8_phone_too_short():
    try:
        main.Phone('123')
        raise AssertionError('Expected ValueError')
    except ValueError:
        pass


@add_test
def t9_phone_too_long():
    try:
        main.Phone('01234567890')
        raise AssertionError('Expected ValueError')
    except ValueError:
        pass


@add_test
def t10_record_has_add():
    assert hasattr(main.Record, 'add_phone')


@add_test
def t11_record_has_remove():
    assert hasattr(main.Record, 'remove_phone')


@add_test
def t12_record_has_edit():
    assert hasattr(main.Record, 'edit_phone')


@add_test
def t13_record_has_find():
    assert hasattr(main.Record, 'find_phone')


@add_test
def t14_ab_has_add_record():
    assert hasattr(main.AddressBook, 'add_record')


@add_test
def t15_ab_has_find():
    assert hasattr(main.AddressBook, 'find')


@add_test
def t16_ab_has_delete():
    assert hasattr(main.AddressBook, 'delete')


@add_test
def t17_ab_add_and_find():
    ab = main.AddressBook()
    r = main.Record('Bob')
    r.add_phone('0123456789')
    ab.add_record(r)
    found = ab.find('Bob')
    assert isinstance(found, main.Record)


@add_test
def t18_ab_find_missing_none():
    ab = main.AddressBook()
    assert ab.find('NoName') is None


@add_test
def t19_ab_delete_existing():
    ab = main.AddressBook()
    r = main.Record('Tom')
    ab.add_record(r)
    ab.delete('Tom')
    assert ab.find('Tom') is None


@add_test
def t20_ab_delete_nonexistent_noerror():
    ab = main.AddressBook()
    # should not raise
    ab.delete('Nobody')


@add_test
def t21_record_add_phone_string():
    r = main.Record('A')
    r.add_phone('0123456789')
    p = r.find_phone('0123456789')
    assert isinstance(p, main.Phone)


@add_test
def t22_record_find_existing():
    r = main.Record('B')
    r.add_phone('0123456789')
    assert r.find_phone('0123456789') is not None


@add_test
def t23_record_find_missing_none():
    r = main.Record('C')
    assert r.find_phone('0987654321') is None


@add_test
def t24_record_edit_existing():
    r = main.Record('D')
    r.add_phone('0123456789')
    r.edit_phone('0123456789', '0987654321')
    assert r.find_phone('0987654321') is not None


@add_test
def t25_record_edit_missing_raises():
    r = main.Record('E')
    try:
        r.edit_phone('0000000000', '1111111111')
        raise AssertionError('Expected ValueError')
    except ValueError:
        pass


@add_test
def t26_record_remove_existing():
    r = main.Record('F')
    r.add_phone('0123456789')
    r.remove_phone('0123456789')
    assert r.find_phone('0123456789') is None


@add_test
def t27_after_remove_not_found():
    r = main.Record('G')
    r.add_phone('0123456789')
    r.remove_phone('0123456789')
    assert r.find_phone('0123456789') is None


@add_test
def t28_add_phone_accepts_phone_instance():
    r = main.Record('H')
    p = main.Phone('0123456789')
    r.add_phone(p)
    assert r.find_phone('0123456789') is not None


@add_test
def t29_record_str_contains_name_and_phone():
    r = main.Record('I')
    r.add_phone('0123456789')
    s = str(r)
    assert 'I' in s and '0123456789' in s


@add_test
def t30_ab_stores_under_name_key():
    ab = main.AddressBook()
    r = main.Record('KeyName')
    ab.add_record(r)
    assert 'KeyName' in ab.data


def run():
    passed = 0
    failed = 0
    results = []
    for i, fn in enumerate(tests, 1):
        name = fn.__name__
        try:
            fn()
            print(f"{i:02d}. {name}: PASS")
            passed += 1
            results.append((name, True, None))
        except AssertionError as e:
            print(f"{i:02d}. {name}: FAIL - {e}")
            failed += 1
            results.append((name, False, e))
        except Exception as e:
            print(f"{i:02d}. {name}: ERROR - {e}")
            traceback.print_exc(limit=1)
            failed += 1
            results.append((name, False, e))

    print('\nSummary:')
    print(f'Passed: {passed}')
    print(f'Failed: {failed}')
    if failed:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    run()
