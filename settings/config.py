"""Helper structure to set default config"""  # pylint: disable=line-too-long


default_config = [
    {
        "arg": "--tx-amount",
        "type": float,
        "default": 0.003,
        "dest": "tx_amount",
        "help": "Amount to be transfer from Futures to spot",
    },
]
