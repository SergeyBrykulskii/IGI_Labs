import parsers.src.constants as constants
import re
import inspect

def create_serializer(obj):
    if isinstance(obj, (float, int, complex, bool, str, type(None))):
        return serialize_fincbs
    elif isinstance(obj, (list, tuple, bytes)):
        return serialize_ltb
    elif isinstance(obj, dict):
        return serialize_dict
    elif inspect.isfunction(obj):
        return serialize_function
    elif inspect.isclass(obj):
        return serialize_class


def serialize(obj):
    serializer = create_serializer(obj)
    serialized = serializer(obj)
    serialized = tuple((k, serialized[k]) for k in serialized)

    return serialized

def deserialize(obj):
    pass


def serialize_fincbs(fincbs):
    """
    serialize ficbs to dict of type and value
    :param fincbs: float, int, none, complex, bool, str
    :return: dict with ["type"] and ["value"]
    """
    serialized_ficbs = dict()
    serialized_ficbs[constants.TYPE] = re.search(constants.REGEX_TYPE, str(type(fincbs))).group(1)
    serialized_ficbs[constants.VALUE] = fincbs

    return serialized_ficbs


def serialize_ltb(objects):
    """
    serialize objects to dict of type and value
    :param objects: list, tuple, bytes
    :return: dict with ["type"] and ["value"]
    """
    serialized_list = dict()
    serialized_list[constants.TYPE] = re.search(constants.REGEX_TYPE, str(type(objects))).group(1)
    serialized_list[constants.VALUE] = tuple([serialize(obj) for obj in objects])

    return serialized_list


def serialize_dict(dict_object):
    """
    serialize dict_object to dict of type and value
    :param dict_object: dict
    :return: dict with ["type"] and ["value"]
    """
    serialized_dict = dict()
    serialized_dict[constants.TYPE] = constants.DICT
    serialized_dict[constants.VALUE] = {}

    for i in dict_object:
        key = serialize(i)
        value = serialize(dict_object[i])
        serialized_dict[constants.VALUE][key] = value

    serialized_dict[constants.VALUE] = tuple((k, serialized_dict[constants.VALUE][k])
                                             for k in serialized_dict[constants.VALUE])

    return serialized_dict


def serialize_function(function_object):
    ans = dict()
    ans[constants.TYPE] = constants.FUNCTION
    ans[constants.VALUE] = {}
    members = inspect.getmembers(function_object)
    members = [i for i in members if i[0] in constants.FUNCTION_ATTRIBUTES]
    for i in members:
        key = serialize(i[0])
        if i[0] != constants.CLOSURE:
            value = serialize(i[1])
        else:
            value = serialize(None)

        ans[constants.VALUE][key] = value
        if i[0] == constants.CODE:
            key = serialize(constants.GLOBALS)
            ans[constants.VALUE][key] = {}
            names = i[1].__getattribute__("co_names")
            glob = function_object.__getattribute__(constants.GLOBALS)
            glob_dict = {}
            for name in names:
                if name == function_object.__name__:
                    glob_dict[name] = function_object.__name__
                elif name in glob and not inspect.ismodule(name) and name not in __builtins__:
                    glob_dict[name] = glob[name]
            ans[constants.VALUE][key] = serialize(glob_dict)

    ans[constants.VALUE] = tuple((k, ans[constants.VALUE][k]) for k in ans[constants.VALUE])
    return ans


def serialize_class(class_obj):
    ans = dict()
    ans[constants.TYPE] = constants.CLASS
    ans[constants.VALUE] = {}
    ans[constants.VALUE][serialize(constants.NAME_NAME)] = serialize(class_obj.__name__)
    members = []
    for i in inspect.getmembers(class_obj):
        if not (i[0] in constants.NOT_CLASS_ATTRIBUTES):
            members.append(i)

    for i in members:
        key = serialize(i[0])
        val = serialize(i[1])
        ans[constants.VALUE][key] = val
    ans[constants.VALUE] = tuple((k, ans[constants.VALUE][k]) for k in ans[constants.VALUE])

    return ans


