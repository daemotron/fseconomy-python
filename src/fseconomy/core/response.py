import http
from typing import Optional, Any


class Response:
    """FSEconomy Server Response

    :param status: HTTP status code sent by the server
    :type status: int
    :param maintenance: flag signalling that server is in maintenance mode
    :type maintenance: bool
    :param ok: flag signalling a normal request flow with the server
    :type ok: bool
    :param fail: flag signalling an abnormal request flow with the server
    :type fail: bool
    :param data: data received from the server represented by native Python data types
    :param raw: raw data string received from the server
    :type raw: str
    :param message: message text detailing the status flags
    :type message: str
    """

    def __init__(self, status: int = 0, maintenance: bool = False, ok: bool = False, fail: bool = False,
                 data: Optional[Any] = None, raw: str = '', message: str = ''):
        self._status: int = status
        self._maintenance: bool = maintenance
        self._ok: bool = ok
        self._fail: bool = fail
        self._data: Any = data
        self._raw: str = raw
        self._message: str = message

    @property
    def status(self) -> int:
        """HTTP status code sent by the server"""
        return self._status

    @status.setter
    def status(self, value: int):
        self._status = http.HTTPStatus(int(value))

    @property
    def maintenance(self) -> bool:
        """Server maintenance flag

        Not used in default mode; instead, an :exc:`~fseconomy.exceptions.FseServerMaintenanceError` will be raised."""
        return self._maintenance

    @maintenance.setter
    def maintenance(self, value: bool):
        self._maintenance = bool(value)

    @property
    def ok(self) -> bool:
        """Request success flag

        Always set to ``True`` in default mode. Any abnormal situation will be signalled by raising the corresponding
        exception."""
        return self._ok

    @ok.setter
    def ok(self, value: bool):
        self._ok = bool(value)

    @property
    def fail(self) -> bool:
        """Request failure flag

        Not used in default mode; instead, an :exc:`~fseconomy.exceptions.FseServerRequestError` will be raised."""
        return self._fail

    @fail.setter
    def fail(self, value: bool):
        self._fail = bool(value)

    @property
    def data(self) -> Optional[Any]:
        """Data received from the server decoded into native Python data types"""
        return self._data

    @data.setter
    def data(self, value: Optional[Any] = None):
        self._data = value

    @property
    def raw(self) -> str:
        """Data received from the server as raw string"""
        return self._raw

    @raw.setter
    def raw(self, value: str):
        self._raw = value

    @property
    def message(self) -> str:
        """Message with details regarding the set flags"""
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = str(value)
