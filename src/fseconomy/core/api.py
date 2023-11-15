from .data import aircraft
from .data import aliases
from .data import assignment
from .data import commodity
from .data import config
from .data import facility
from .data import status


#: FSEconomy APIs and versions
API_VERSIONS = {
    'data': 'https://server.fseconomy.net/data',
    'fse': 'https://server.fseconomy.net/rest/fse/api',
    'v1': 'https://server.fseconomy.net/rest/api',
    'v2': 'https://server.fseconomy.net/rest/api/v2'
}


#: Server maintenance token string
MAINTENANCE = "Currently Closed for Maintenance"


#: FSEconomy Data Feeds with their respective parameters and parser function
DATA_FEEDS = {
    'aircraft status by registration': {
        'query': 'aircraft',
        'search': 'status',
        'params': ['aircraftreg'],
        'decode': status.decode
    },
    'aircraft configs': {
        'query': 'aircraft',
        'search': 'configs',
        'decode': config.decode
    },
    'aircraft aliases': {
        'query': 'aircraft',
        'search': 'aliases',
        'decode': aliases.decode
    },
    'aircraft for sale': {
        'query': 'aircraft',
        'search': 'forsale',
        'decode': aircraft.decode
    },
    'aircraft by makemodel': {
        'query': 'aircraft',
        'search': 'makemodel',
        'params': ['makemodel'],
        'decode': aircraft.decode
    },
    'aircraft by ownername': {
        'query': 'aircraft',
        'search': 'ownername',
        'params': ['ownername'],
        'decode': aircraft.decode
    },
    'aircraft by registration': {
        'query': 'aircraft',
        'search': 'registration',
        'params': ['aircraftreg'],
        'decode': aircraft.decode
    },
    'aircraft by id': {
        'query': 'aircraft',
        'search': 'serialnumber',
        'params': ['serialnumber'],
        'decode': aircraft.decode
    },
    'aircraft by key': {
        'query': 'aircraft',
        'search': 'key',
        'decode': aircraft.decode
    },
    'assignments by key': {
        'query': 'assignments',
        'search': 'key',
        'decode': assignment.decode
    },
    'commodities by key': {
        'query': 'commodities',
        'search': 'key',
        'decode': commodity.decode
    },
    'facilities by key': {
        'query': 'Facilities',
        'search': 'key',
        'decode': facility.decode
    }
}
