import logging

from autobahn.asyncio.wamp import ApplicationSession


class ZeitSonde(ApplicationSession):
    """
    TODO
    """
    async def onJoin(self, details):
        logging.info('ZeitSonde server has joined to WAMP router')

        import asyncio
        await asyncio.sleep(3)
