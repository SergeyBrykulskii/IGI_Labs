DICT1 = "{'type': 'dict', 'value': ()}"
DICT2 = "{'type': 'dict', 'value': (((('type', 'int'), ('value', 4)), (('type', 'int'), ('value', 42))), ((('type', 'int'), ('value', 5)), (('type', 'int'), ('value', 42))), ((('type', 'int'), ('value', 2)), (('type', 'int'), ('value', 42))))}"
DICT3 = "{'type': 'dict', 'value': (((('type', 'tuple'), ('value', ((('type', 'str'), ('value', '42')), (('type', 'str'), ('value', '42'))))), (('type', 'list'), ('value', ((('type', 'str'), ('value', '42')),)))), ((('type', 'int'), ('value', 42)), (('type', 'str'), ('value', '42'))))}"

LIST1 = "{'type': 'list', 'value': ()}"
LIST2 = "{'type': 'list', 'value': ((('type', 'str'), ('value', '42')), (('type', 'int'), ('value', 42)), (('type', 'int'), ('value', -42)))}"
LIST3 = "{'type': 'list', 'value': ((('type', 'list'), ('value', ((('type', 'str'), ('value', '42')), (('type', 'int'), ('value', 42))))), (('type', 'bool'), ('value', True)))}"

TUPLE1 = "{'type': 'tuple', 'value': ()}"
TUPLE2 = "{'type': 'tuple', 'value': ((('type', 'str'), ('value', '42')), (('type', 'int'), ('value', 42)), (('type', 'int'), ('value', -42)))}"
TUPLE3 = "{'type': 'tuple', 'value': ((('type', 'tuple'), ('value', ((('type', 'str'), ('value', '42')), (('type', 'int'), ('value', 42))))), (('type', 'bool'), ('value', True)))}"