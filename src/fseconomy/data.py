"""
fseconomy.data
~~~~~~~~~~~~~~

This module contains public functions to access the FSEconomy Data Feeds.
"""
from .core.response import Response
from .core.fetch import fetch


def aircraft_configs() -> Response:
    """Aircraft Configurations

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft configs')


def aircraft_aliases() -> Response:
    """Aircraft Aliases

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft aliases')


def aircraft_for_sale() -> Response:
    """Aircraft for Sale

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft for sale')


def aircraft_by_makemodel(makemodel: str) -> Response:
    """Aircraft by MakeModel

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :param makemodel: the make/model as string
    :type makemodel: str
    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft by makemodel', {'makemodel': makemodel})


def aircraft_by_ownername(ownername: str) -> Response:
    """Aircraft by Owner Name

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :param ownername: the owner name as string
    :type ownername: str
    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft by ownername', {'ownername': ownername})


def aircraft_by_registration(registration: str) -> Response:
    """Aircraft by Registration

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :param registration: the aircraft registration as string
    :type registration: str
    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft by registration', {'aircraftreg': registration})


def aircraft_by_id(serialnumber: int) -> Response:
    """Aircraft by Id

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :param serialnumber: the aircraft numeric ID
    :type serialnumber: int
    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft by id', {'serialnumber': serialnumber})


def aircraft_by_key() -> Response:
    """Aircraft by Key

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('aircraft by key')
