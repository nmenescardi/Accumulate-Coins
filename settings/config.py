"""Helper structure to set default config"""  # pylint: disable=line-too-long


default_config = [
    {
        "arg": "--cooldown",
        "type": int,
        "default": 1440,  # A day
        "dest": "minutes_between_trades",
        "help": "It determine the amount of minutes that the trader should wait between trades of the same symbol",
    },
    {
        "arg": "--sleep",
        "type": int,
        "default": 35,
        "dest": "sleep_between_calls",
        "help": "Time in seconds to sleep between calls to the Binance API",
    },
]
