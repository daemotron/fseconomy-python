"""
fseconomy.core.data.aircraft
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains data handling functions for the aircraft data feed.
"""
from ...exceptions import FseDataParseError
from ...util import xml, time


def decode(raw_data: str) -> list:
    """Decode FSEconomy aircraft data

    :raises FseDataParseError: in case of malformed data provided

    :param raw_data: string with raw XML data representing an aircraft data feed
    :type raw_data: str
    :return: list of dictionaries representing each an aircraft from the data feed
    :rtype: list
    """
    data = xml.to_python(raw_data)
    result = []
    try:
        for aircraft in data['AircraftItems']['Aircrafts']:
            result.append({
                'Registration': aircraft['Aircraft']['Registration'],
                'MonthlyFee': float(aircraft['Aircraft']['MonthlyFee']),
                'RentalTime': int(aircraft['Aircraft']['RentalTime']),
                'SerialNumber': int(aircraft['Aircraft']['SerialNumber']),
                'FuelPct': float(aircraft['Aircraft']['FuelPct']),
                'RentalDry': float(aircraft['Aircraft']['RentalDry']),
                'Equipment': aircraft['Aircraft']['Equipment'],
                'Location': aircraft['Aircraft']['Location'],
                'Home': aircraft['Aircraft']['Home'],
                'RentalWet': float(aircraft['Aircraft']['RentalWet']),
                'NeedsRepair': bool(int(aircraft['Aircraft']['NeedsRepair'])),
                'Bonus': float(aircraft['Aircraft']['Bonus']),
                'LeasedFrom': aircraft['Aircraft']['LeasedFrom'],
                'LocationName': aircraft['Aircraft']['LocationName'],
                'SalePrice': float(aircraft['Aircraft']['SalePrice']),
                'Owner': aircraft['Aircraft']['Owner'],
                'RentalType': aircraft['Aircraft']['RentalType'],
                'FeeOwed': float(aircraft['Aircraft']['FeeOwed']),
                'AirframeTime': time.parse_hobbs(aircraft['Aircraft']['AirframeTime']),
                'EngineTime': time.parse_hobbs(aircraft['Aircraft']['EngineTime']),
                'TimeLast100hr': time.parse_hobbs(aircraft['Aircraft']['TimeLast100hr']),
                'MakeModel': aircraft['Aircraft']['MakeModel'],
                'SellbackPrice': float(aircraft['Aircraft']['SellbackPrice']),
                'RentedBy': aircraft['Aircraft']['RentedBy']
            })
    except (KeyError, IndexError):
        raise FseDataParseError
    return result
