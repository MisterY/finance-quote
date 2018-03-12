"""
CLI interface to F::Q
"""
import logging

import click
import click_log

from .app import App

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

@click.group()
@click_log.simple_verbosity_option(logger)
def cli():
    """ entry point """
    pass

@click.command()
def alphavantage():
    """ test """
    app = App()
    app.logger = logger
    # TODO: invoke a/v module

@click.command()
@click.argument("base", "Base currency ISO symbol (i.e. EUR)")
@click.argument("symbols", "List of symbols to fetch the rates for")
def fixerio(base: str, symbols: str):
    """ Fixerio currency rates """
    base = base.upper()

    app = App()
    app.logger = logger
    quote = app.fixerio(base, symbols)
    # TODO display fixerio quote
    print(quote)

#############################################
cli.add_command(alphavantage)
cli.add_command(fixerio)
