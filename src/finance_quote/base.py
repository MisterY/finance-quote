import datetime
from decimal import Decimal
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
        symbol = ("{namespace}:{symbol}".format(namespace=self.namespace, symbol=self.symbol) 
                    if self.namespace else self.symbol)
        symbol = "{symbol:<13}".format(symbol)

        value = "{value:>6}".format(self.value)
        return ("<Quote ('{symbol}',date:{datetime},value:{value},currency:{currency})>".format(symbol, datetime=self.datetime, value, currency=self.currency))

class Source:
    """Class to represent a source of symbols or quotes"""
    def __init__(self, session=None):
        self.session = session if session else Session()

    def get_latest(self, symbol) -> Quote:
        """Return the latest quote for a symbol"""
        raise NotImplementedError

    def get_historical(self, symbol, date_from, date_to, tz=None) -> Quote:
        """Return the historical of quotes for a symbol"""
        raise NotImplementedError

    def get_symbol(self, symbol) -> Symbol:
        """Return information about a symbol"""
        raise NotImplementedError

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
