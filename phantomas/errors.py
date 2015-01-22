"""
Custom exceptions that phantomas "client" can raise
"""


class PhantomasError(Exception):
    """ Generic phantomas exception """
    pass


class PhantomasRunError(Exception):
    """ Phantomas exception raised from run() function """
    pass


class PhantomasResponseParsingError(Exception):
    """
    Phantomas exception raised from run() function
    when JSON can not be parsed
    """
    pass
