import parsers.src.constants as constants
import re
import inspect

def create_serializer(obj):
    if isinstance(obj, (float, int, complex, bool, str, type(None))):
        return serialize_fincbs
    if isinstance(obj, (list, tuple, bytes)):
        return serialize_ltb
    if inspect.isclass(obj):
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


