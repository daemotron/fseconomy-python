from typing import Optional
from ..util.hex import is_hex


#: FSEconomy Access Key
ACCESS_KEY: Optional[str] = None


#: FSEconomy Service Key
SERVICE_KEY: Optional[str] = None


#: FSEconomy User Key
USER_KEY: Optional[str] = None


def validate_key(key: Optional[str]) -> bool:
    """validates a new style FSEconomy API key

    :param key: string to validate
    :return: True if string is a valid API key, otherwise False
    """
    try:
        return key and (len(key) == 16) and is_hex(key)
    except (ValueError, TypeError):
        return False
