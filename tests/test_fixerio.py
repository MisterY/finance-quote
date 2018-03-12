""" Tests for fixerio module """
import logging
from finance_quote import App

def test_if_alive():
    app = App()
    result = app.fixerio("eur", "usd")
    logging.debug(result)

    assert result != None
