import datetime

import requests


class FinanceQuoteError(Exception):
    pass

class SymbolNotFoundError(FinanceQuoteError):
    pass

class SourceConnectionError(FinanceQuoteError):
    pass

class Symbol:
    """Class to represent a symbol (currency, stock, index, ...)"""
    pass

class Quote:
    """Class to represent a quote (price, ...)"""
    def __init__(self):
        self.datetime: datetime = None
        self.namespace: str = None
        self.symbol: str = None
        self.value: Decimal = Decimal(0)
        self.currency: str = None

    def __repr__(self):
        symbol = f"{self.namespace}:{self.symbol}" if self.namespace else self.symbol
        symbol = f"{symbol:<13}"

        value = f"{self.value:>6}"
        return f"<Quote ('{symbol}',date:{self.datetime},value:{value},currency:{self.currency})>"

class Source:
    """Class to represent a source of symbols or quotes"""

    def get_latest(self, symbol) -> Quote:
        """Return the latest quote for a symbol"""
        raise NotImplemented

    def get_historical(self, symbol, date_from, date_to, tz=None) -> Quote:
        """Return the historical of quotes for a symbol"""
        raise NotImplemented

    def get_symbol(self, symbol) -> Symbol:
        """Return information about a symbol"""
        raise NotImplemented

def normalize(d):
    if isinstance(d, datetime.datetime):
        pass
    elif isinstance(d, datetime.date):
        d = datetime.datetime.combine(d, datetime.time(0))
    else:
        d = datetime.datetime.strptime(d, "%Y-%m-%d")
    if not d.tzinfo:
        pass
        # assert tz
        # todo: understand yahoo behavior as even in the browser, I get
        # weird results ...
        # d = d.replace(tzinfo=tz)
    return d


# can be monkey patched if needed
Session = requests.Session