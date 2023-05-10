from parsers.src.general_serialize_functions import serialize_fincbs
from parsers.src.general_serialize_functions import serialize_ltb
from parsers.src.general_serialize_functions import serialize_dict
from parsers.src.general_serialize_functions import serialize
from parsers.src.general_serialize_functions import deserialize

from parsers.json.json_parser import JsonParser
from parsers.xml.xml_parser import XmlParser

import math
import tests.constants as constants
import pytest

test_list = [1, "qwe", 3, 22.8, (1, 2, 3), False, None]


@pytest.mark.skip
def test_mul(n):
    return n * 2


@pytest.mark.skip
def test_fact(n):
    if n == 0:
        return 1
    else:
        return n * test_fact(n - 1)


def func_with_builtin_func(arr: list):
    res = sorted(arr)

    return res


@pytest.mark.skip
def test_wrapper(n):
    return test_fact(n - 1) * n


@pytest.mark.skip
def test_vars(n):
    return test_list, n


class Human:
    test = "hi"

    def __init__(self, id=3):
        self.id = id

    def get_id(self):
        return self.id


class SomeClass:
    sity = "Minsk"

    def __init__(self, person_number=3):
        self.persons = []
        for i in range(person_number):
            self.persons.append(SomeClass(i))

    def get_info(self):
        result = 0
        for person in self.persons:
            result += person.age

        return result

c = 42


def test_fincbs_types():
    f = 0.42
    i = 42
    n = None
    c = complex(4, 2)
    b = True
    s = "42"

    assert (str(serialize_fincbs(f)) == "{'type': 'float', 'value': 0.42}")
    assert (str(serialize_fincbs(i)) == "{'type': 'int', 'value': 42}")
    assert (str(serialize_fincbs(n)) == "{'type': 'NoneType', 'value': None}")
    assert (str(serialize_fincbs(c)) == "{'type': 'complex', 'value': (4+2j)}")
    assert (str(serialize_fincbs(b)) == "{'type': 'bool', 'value': True}")
    assert (str(serialize_fincbs(s)) == "{'type': 'str', 'value': '42'}")


def test_ltb_types():
    list1 = []
    list2 = ["42", 42, -42]
    list3 = [["42", 42], True]

    tuple1 = ()
    tuple2 = ("42", 42, -42)
    tuple3 = (("42", 42), True)

    assert (str(serialize_ltb(list1)) == constants.LIST1)
    assert (str(serialize_ltb(
        list2)) == constants.LIST2)
    assert (str(serialize_ltb(
        list3)) == constants.LIST3)

    assert (str(serialize_ltb(tuple1)) == constants.TUPLE1)
    assert (str(serialize_ltb(
        tuple2)) == constants.TUPLE2)
    assert (str(serialize_ltb(
        tuple3)) == constants.TUPLE3)


def test_dict():
    dict1 = dict()
    dict2 = {4: 42, 5: 42, 2: 42}
    dict3 = {("42", "42"): ["42"], 42: "42"}
    dict4 = {1: dict1.copy(), 2: dict2.copy(), 3: dict3.copy()}
    dict5 = {"42": 42}

    assert (str(serialize_dict(dict1)) == constants.DICT1)
    assert (str(serialize_dict(dict2)) == constants.DICT2)
    assert (str(serialize_dict(dict3)) == constants.DICT3)

    assert (dict1 == deserialize(serialize(dict1)))
    assert (dict2 == deserialize(serialize(dict2)))
    assert (dict3 == deserialize(serialize(dict3)))
    assert (dict4 == deserialize(serialize(dict4)))
    assert (dict5 == deserialize(serialize(dict5)))


def test_foo():
    functions = [test_mul, test_fact, test_wrapper, test_vars]
    for some_function in functions:
        sd_function = deserialize(serialize(some_function))
        assert (sd_function(5) == some_function(5))

    sd_func_with_builtin_func = deserialize(serialize(func_with_builtin_func))
    assert (sd_func_with_builtin_func([5, 4, -1, 15]) == func_with_builtin_func([5, 4, -1, 15]))


def test_class():
    sd_class = deserialize(serialize(Human))
    sd_object = sd_class(15)
    person = Human(15)

    assert (person.test == sd_object.test)
    assert (person.get_id() == sd_object.get_id())


def test_object():
    person = Human(3)
    sd_person = deserialize(serialize(person))
    assert (sd_person.id == person.id)
    assert (sd_person.id == person.id)
    assert (sd_person.get_id() == sd_person.get_id())


def test_lambda():
    x = lambda a: a + 10
    y = deserialize(serialize(lambda a: a + 10))
    z = deserialize(serialize(x))
    assert (x(10) == y(10) == z(10))



