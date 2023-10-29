from typing import Optional

from core import keys
from util.hex import is_hex


def set_service_key(key: Optional[str] = None):
    if keys.validate_key(key):
        keys.SERVICE_KEY = key


def set_access_key(key: Optional[str] = None):
    if keys.validate_key(key):
        keys.ACCESS_KEY = key


def set_user_key(key: Optional[str] = None):
    if keys.validate_key(key):
        keys.USER_KEY = key
