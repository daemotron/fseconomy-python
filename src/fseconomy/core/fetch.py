from typing import Union, Optional

import requests

from . import keys
from .api import DATA_FEEDS, MAINTENANCE, API_VERSIONS
from ..response import Response
from ..exceptions import FseDataFeedInvalidError, FseServerMaintenanceError, FseServerRequestError, \
    FseDataFeedParamError


def fetch(feed: str, params: Optional[dict] = None, binary: bool = False) -> Union[None, Response]:
    """Fetch data feed and parse response

    The *feed* parameter needs to represent a data field as defined in the :mod:`~fseconomy.core.api` module.

    If the requested feed requires additional parameters, these need to be provided via the ``params`` dictionary.

    :raises FseDataFeedInvalidError: in case ``feed`` is not a valid data feed
    :raises FseDataFeedParamError: in case a required additional parameter is missing
    :raises FseServerRequestError: in case the communication with the server fails
    :raises FseServerMaintenanceError: in case the server is in maintenance mode
    :raises FseDataParseError: in case the data received are malformed or cannot be parsed for other reasons

    :param feed: the data feed to fetch
    :type feed: str
    :param params: optional dictionary with additional parameters specific to the requested data feed
    :type params: dict
    :param binary: expect binary content from the server
    :type binary: bool
    :return: FSEconomy Server Response object
    :rtype: Response
    """
    # ensure params is a dictionary
    if params is None:
        params = {}

    # check if feed exists
    if feed not in DATA_FEEDS:
        raise FseDataFeedInvalidError(message="{} is not a valid FSEconomy Data Feed".format(feed))

    # check if all required params were passed
    if 'params' in DATA_FEEDS[feed]:
        for param in DATA_FEEDS[feed]['params']:
            if param not in params:
                raise FseDataFeedParamError("required parameter {} not provided".format(param))

    # create payload
    payload = {'format': 'xml', 'query': DATA_FEEDS[feed]['query'], 'search': DATA_FEEDS[feed]['search']}
    payload.update(params)
    payload.update(keys.get_data_keys())

    # execute request and check for a good response
    try:
        response = requests.get(API_VERSIONS['data'], params=payload)
    except requests.exceptions.ConnectionError:
        raise FseServerRequestError

    # detect possible server maintenance
    if MAINTENANCE in response.text:
        raise FseServerMaintenanceError

    # detect other server communication issues
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise FseServerRequestError

    # process data
    if binary:
        raw = response.content
    else:
        raw = response.text
    return Response(
        status=response.status_code,
        data=DATA_FEEDS[feed]['decode'](raw),
        raw=raw,
        ok=True
    )
