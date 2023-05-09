def serialize_xml(obj) -> str:
    if type(obj) == tuple:
        serialized = []
        for i in obj:
            if type(i) != tuple:
                serialized.append(
                    f"<str>{serialize_xml(i)}</str> ")
            else:
                serialized.append(
                    f"{serialize_xml(i)}")
        ans = "".join(serialized)
        return f"<{type(obj).__name__}>{ans}</{type(obj).__name__}> "
        # return f"{ans}"
    else:
        return obj


# def deserialize_xml(obj: str):
#     # <tuple><str>type</str><str>int</str></tuple><tuple><str>value</str><int>1</int></tuple>
#     # <tuple><tuple><str><str>type</str><str>int</str></str></tuple><tuple><int><str>value</str><int>5</int></int></tuple></tuple>
#     # (('type','int'),('value','4'))
#     # [["type", "int"], ["value", "4"]]
#     if len(obj) == 0:
#         return tuple()
#     if obj[0] == '<':
#         ind = obj.find('>')
#         tag = obj[1:ind]
#         obj = obj[ind+1:len(obj)]
#         deserialized_obj = []
#         depth = 1
#         substr = ""
#         i = 0
#         while i < len(obj):

#             if obj[i] == '<' and obj[i+1:i+len(tag)+1] == tag:
#                 if depth == 0:
#                     obj = obj[ind+1:len(obj)]
#                     i = 0
#                 depth += 1
#             elif obj[i] == '/' and obj[i+1:i+len(tag)+1] == tag:
#                 depth -= 1
#             elif depth == 0:
#                 deserialized_obj.append(
#                     deserialize_xml(substr[0:len(substr)-2]))
#                 i += len(tag) + 1
#                 obj = obj[i:len(obj)]
#                 i = 0
#                 substr = ""
#                 ind = obj.find('>')
#                 tag = obj[1:ind]
#                 continue

#             substr += obj[i]
#             i += 1

#         deserialized_obj.append(deserialize_xml(substr))
#         deserialized_obj.pop()
#         return tuple(deserialized_obj)
#     else:
#         return obj
    

def deserialize_xml(obj: str):
    if obj == '<tuple></tuple>':
        return tuple()
    elif obj[:7] == '<tuple>':
        obj = obj[7:-9]
        if obj[-1] == ' ':
            obj = obj[:-1]

        parsed = []
        depth = 0
        substr = ""
        for i in obj:
            if i == '<' or i == '>':
                depth += 1
            elif i == '/':
                depth -= 4
            elif depth == 0:
                parsed.append(deserialize_xml(substr))
                substr = ""
                continue

            substr += i
        parsed.append(deserialize_xml(substr))
        return tuple(parsed)
    
    elif obj[:5] == '<str>':
        parsed = []
        ind = obj.find('</str>')
        if obj[ind + 6:] != "":
            parsed.append(deserialize_xml(obj[5:ind]))
            parsed.append(deserialize_xml(obj[ind + 6:]))
        else:
            return obj[5:ind]
        return tuple(parsed)
    else:
        return obj