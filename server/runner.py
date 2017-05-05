import logging
import os
import sys

import txaio
from autobahn.asyncio.wamp import ApplicationRunner
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError

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

    # Setup connection to MongoDB.
    mongodb_connection_uri = os.environ.get(
        'ZEITSONDE_MONGODB_CONNECTION_URI',
        'mongodb://localhost:27017'
    )
    mongodb_database_name = os.environ.get(
            'ZEITSONDE_MONGODB_DATABASE_NAME',
            'ZeitSonde'
        )
    client = AsyncIOMotorClient(
        mongodb_connection_uri,
        serverSelectionTimeoutMS=5000
    )
    try:
        client.is_mongos
    except ServerSelectionTimeoutError:
        logging.error(
            'Cannot connect to MongoDB (ServerSelectionTimeoutError)')
        sys.exit(1)
    logging.info(
        'Connected to MongoDB database %s at %s',
        *[mongodb_database_name, mongodb_connection_uri]
    )
    database = client[mongodb_database_name]

    # Setup kwargs for application runner.
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
            'database': database,
        },
    }

    # Create application runner and let it run forever using our main
    # component ZeitSonde.
    runner = ApplicationRunner(**runner_kwargs)
    runner.run(ZeitSonde)


if __name__ == '__main__':
    run()
