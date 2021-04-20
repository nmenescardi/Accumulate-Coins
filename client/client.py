"""Handles client related functionality."""

import os

from binance.client import Client as BinanceClient  # type: ignore

from helpers.singleton import singleton


@singleton
class Client:
    """Main module class."""

    def __init__(self):
        self.client = BinanceClient(
            os.getenv("BINANCE_API"), os.getenv("BINANCE_SECRET")
        )

    def get(self):
        """Get client instance."""
        return self.client
