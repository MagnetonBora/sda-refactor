#!/usr/bin/python
from logging import info


class FileFormatException(IOError):
    pass


def get_max_accessories():
    """
    Function, that finds product ID with the highest number of accessories.
    For example, if accessories.txt contains:
    1: 8,17
    12: 2,3,4,5,6,7
    13:
    15: 1,11
    Returns (12, 6)
    """
    try:
        f = open("/home/some_user/accessories.txt")
        products = {}
        for line in f.readlines():
            line_splited = line.split(":")
            if len(line_splited) != 2:
                raise FileFormatException("Line cannot be split by ':'")
            product_id, accessories = line_splited
            accessories = accessories.split(",")
            products[product_id] = len(accessories)
        f.close()
        return sorted(products.iteritems(), key=lambda x: x[1], reverse=True)[0]
    except IOError:
        info("Some I/O Problems")
    except FileFormatException:
        info("Bad input file. Please check format of your file")
        raise
    return []


print(get_max_accessories())
