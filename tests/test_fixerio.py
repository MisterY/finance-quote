""" Tests for fixerio module """
import logging
from finance_quote import App

def test_if_alive():
    app = App()
    result = app.fixerio("eur", "usd")
    logging.debug(result)

    assert result != None

def test_latest_quotes():
    app = App()
    actual = app.fixerio("eur", "aud")

    assert actual != None
    logging.debug(actual)
    print(actual)
