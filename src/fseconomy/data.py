"""
fseconomy.data
~~~~~~~~~~~~~~

This module contains public functions to access the FSEconomy Data Feeds.
"""
from .response import Response
from .core.fetch import fetch, fetch_file


def aircraft_status_by_registration(registration: str) -> Response:
    """Aircraft Status by Registration

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
    return fetch('aircraft status by registration', {'aircraftreg': registration})


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


def assignments_by_key() -> Response:
    """Assignments by Key

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('assignments by key')


def commodities_by_key() -> Response:
    """Commodities by Key

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('commodities by key')


def facilities_by_key() -> Response:
    """Facilities by Key

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('facilities by key')


def fbos_by_key() -> Response:
    """FBOs by Key

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('fbos by key')


def fbos_for_sale() -> Response:
    """FBOs for Sale

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('fbos for sale')


def fbo_monthly_summary_by_icao(month: int, year: int, icao: str) -> Response:
    """FBO Monthly Summary by ICAO

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :param month: the month as numeric value (1 = January, 12 = December)
    :type month: int
    :param year: the year as numeric value
    :type year: int
    :param icao: the (FSE) ICAO code of the airport or airfield the FBO is at
    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch('fbo monthly summary by icao', {'month': month, 'year': year, 'icao': icao})


def fse_icao_data() -> Response:
    """FSE ICAO Data

    :raises FseDataFileInvalidError: in case ``file`` is not a valid data file
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :return: Response object with data retrieved from the FSEconomy server
    :rtype: Response
    """
    return fetch_file('airports')
