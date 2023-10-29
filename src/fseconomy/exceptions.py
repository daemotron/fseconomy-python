"""
fseconomy.exceptions
~~~~~~~~~~~~~~~~~~~~

This module contains the set of FSEconomy's exceptions.
"""


class FseBaseException(Exception):
    """Common base class for all fseconomy errors

    :param message: Optional error message
    :type message: str
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            message = self.__getattribute__('message')
            if not message:
                raise AttributeError
        except AttributeError:
            self.message = self.__doc__
        if not self.message:
            self.message = self.__doc__

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


class FseError(FseBaseException):
    """There was an ambiguous exception while accessing the FSEconomy API"""
    pass


class FseAuthKeyError(FseBaseException):
    """Could not find a valid authentication key (user or service key)"""
    pass


class FseDataKeyError(FseBaseException):
    """Could not find a valid data access key (user or access key)"""
    pass


class FseDataFeedInvalidError(FseBaseException):
    """Invalid data feed"""
    pass


class FseDataFeedParamError(FseBaseException):
    """One or several required parameters are missing to query the requested data feed"""
    pass


class FseDataParseError(FseBaseException):
    """Unable to parse XML data received from the FSEconomy server"""


class FseServerMaintenanceError(FseBaseException):
    """The FSEconomy server is currently down for maintenance"""
    pass


class FseServerRequestError(FseBaseException):
    """Request to the FSEconomy server failed"""
    pass
