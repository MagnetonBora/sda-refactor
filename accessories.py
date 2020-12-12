import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('accessories_application')


class FileFormatException(Exception):
    pass


def read_products(path: str):
    with open(path) as file:
        for line in file:
            splitted = line.split(":")
            if len(splitted) != 2:
                raise FileFormatException("Line cannot be split by ':'")
            product_id, accessories = splitted
            yield int(product_id), len(accessories.split(","))


def get_max_accessories(path: str):
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
        product_id_max = None
        accessories_max = 0
        for product_id, accessories_count in read_products(path):
            if accessories_count >= accessories_max:
                accessories_max = accessories_count
                product_id_max = product_id
        return product_id_max, accessories_max
    except IOError:
        logger.info("Some I/O Problems")
    except FileFormatException:
        logger.info("Bad input file. Please check format of your file")
        raise
    return []


if __name__ == "__main__":
    print(get_max_accessories("accessories.txt"))
