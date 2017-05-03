import logging
import os

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

logger = logging.getLogger(__name__)
logger.setLevel(int(os.environ.get(
    'ZEITSONDE_LOGLEVEL',
    logging.DEBUG
)))


class ZeitSonde(ApplicationSession):

    #logger = logging.getLogger(__name__)

    def __init__(self, config):
        logger.debug('Init')
        super().__init__(config)

    async def onJoin(self, details):
        #logger.setLevel(10)
        logger.debug('ZeitSonde server has joined to WAMP router')

        import asyncio
        await asyncio.sleep(3)

        logger.debug('ZeitSonde server has joined to WAMP router 2')
