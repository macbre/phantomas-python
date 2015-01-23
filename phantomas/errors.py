"""
Custom exceptions that phantomas "client" can raise
"""


class PhantomasError(Exception):
    """ Generic phantomas exception """
    pass


class PhantomasRunError(PhantomasError):
    """ Phantomas exception raised from run() function """
    pass


class PhantomasResponseParsingError(PhantomasError):
    """
    Phantomas exception raised from run() function
    when JSON can not be parsed
    """
    pass


class PhantomasFailedError(PhantomasError):
    """
    Phantomas exception raised from run() function
    when JSON can not be parsed
    """
    pass
