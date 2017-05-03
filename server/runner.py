
import logging
import os
import sys

from autobahn.asyncio.wamp import ApplicationRunner

from .component import ZeitSonde

logging.basicConfig(level=int(os.environ.get(
    'ZEITSONDE_LOGLEVEL',
    logging.DEBUG
)))
logger = logging.getLogger(__name__)


def run():
    """
    Main entry point for ZeitSonde server application.
    """
    logger.info('Starting ZeitSonde server')

    runner_kwargs = {
        'url': os.environ.get(
            'ZEITSONDE_WAMP_ROUTER_URL',
            'ws://localhost:8080/ws'
        ),
        'realm': os.environ.get(
            'ZEITSONDE_WAMP_REALM',
            'realm1'
        ),
        'extra': {
            'logger': logger,
        },
    }
    runner = ApplicationRunner(**runner_kwargs)
    runner.run(ZeitSonde)


if __name__ == '__main__':
    run()
