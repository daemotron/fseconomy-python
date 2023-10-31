from .data import aircraft


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
    'payments': {
        'query': 'payments',
        'search': 'id',
        'params': ['fromid']
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
    }
}
