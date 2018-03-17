"""
Entry point to the library.
This main class is called from the cli and it is the
entry point for the users of the library.
"""
import logging
from typing import List
from finance_quote.modules.fixerio import FixerioSource

class App:
    """ The main entry point to the F::Q library """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.modules = ['alphavantage']

    def download(self, provider: str, symbols, currency: str):
        """ A generic method that takes the provider as a string parameter """
        provider = provider.lower()
        currency = currency.upper()

        if provider == "alphavantage":
            return self.alphavantage(symbols)
        elif provider == "fixerio":
            return self.fixerio(currency, symbols)
        else:
            raise ValueError("Provider not supported: " + provider)

    def alphavantage(self, symbols):
        """ example using av as provider """
        # TODO invoke av module for fetching price
        # from .modules import av
        if isinstance(symbols, str):
            # handle single symbol
            pass
        elif isinstance(symbols, List):
            # handle list of symbols
            pass
        else:
            raise ValueError("Invalid argument sent")

    def fixerio(self, base_currency: str, symbol: str):
        """ fixerio currency rates """
        agent = FixerioSource()
        result = agent.download("CURRENCY", symbol, base_currency)
        return result
