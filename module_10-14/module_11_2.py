from inspect import getmodule
from pprint import pprint

def introspection_info(obj):
    obj_info = {}
    obj_info['type'] = type(obj).__name__

    attributes_and_methods = dir(obj)
    attributes = []
    methods = []
    for item in attributes_and_methods:
        if callable(getattr(obj, item)):
            methods.append(item)
        else:
            attributes.append(item)
    obj_info['attributes'] = attributes
    obj_info['methods'] = methods
    obj_info['module'] = getmodule(obj).__name__ if getmodule(obj) else None
    return obj_info

if __name__ == '__main__':
    number_info = introspection_info(42)
    pprint(number_info)