"""Helper structure to set default config"""  # pylint: disable=line-too-long


default_config = [
    {
        "arg": "--tx-amount",
        "type": float,
        "default": 0.003,
        "dest": "tx_amount",
        "help": "Amount to be transfer from Futures to spot",
    },
    {
        "arg": "--cooldown",
        "type": int,
        "default": 1440, # A day
        "dest": "minutes_between_trades",
        "help": "It determine the amount of minutes that the trader should wait between trades of the same symbol",
    },
]
