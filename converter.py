"""Utility module for currency conversion using forex_python."""

from forex_python.converter import CurrencyRates, CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

def convert_currency(from_currency, to_currency, amount):
    """Converts an amount from one currency to another and returns the result."""
    converted = cr.convert(from_currency, to_currency, float(amount))
    rounded = round(converted, 2)
    symbol = cc.get_symbol(to_currency)
    return f"{symbol} {rounded}"
