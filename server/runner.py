
import logging
import os

import txaio
from autobahn.asyncio.wamp import ApplicationRunner

from .component import ZeitSonde


def run():
    """
    Main entry point for ZeitSonde server application.
    """
    txaio.start_logging(level=os.environ.get(
        'ZEITSONDE_LOGLEVEL',
        'info'
    ))
    logging.info('Starting ZeitSonde server')

    runner_kwargs = {
        'url': os.environ.get(
            'ZEITSONDE_WAMP_ROUTER_URL',
            'ws://localhost:8080/ws'
        ),
        'realm': os.environ.get(
            'ZEITSONDE_WAMP_REALM',
            'realm1'
        ),
    }
    runner = ApplicationRunner(**runner_kwargs)
    runner.run(ZeitSonde)


if __name__ == '__main__':
    run()
