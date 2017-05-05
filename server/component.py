import logging

from autobahn.asyncio.wamp import ApplicationSession
from autobahn.wamp.exception import ApplicationError
from jsonschema import FormatChecker, ValidationError, validate

from .schema import update_schema


class ZeitSonde(ApplicationSession):
    """
    ZeitSonde application.
    """
    root_uri = 'zeitsonde'

    def __init__(self, config):
        self.database = config.extra['database']
        return super().__init__(config)

    async def onJoin(self, details):
        """
        Coroutine that is called when this appliction joined to WAMP router.

        Handels registration of our procedures.
        """
        logging.info('ZeitSonde server joined to WAMP router')
        await self.register(self.get_data, '{}.get_data'.format(self.root_uri))
        logging.debug(
            'Procedure {}.get_data has been registered'.format(self.root_uri))
        await self.register(self.update, '{}.update'.format(self.root_uri))
        logging.debug(
            'Procedure {}.update has been registered'.format(self.root_uri))

    async def get_data(self):
        """
        Coroutine to retrieve all data from database.
        """
        logging.debug('ZeitSonde.get_data() called')
        cursor = self.database.items.find()
        data = await cursor.to_list(length=None)
        return data

    async def update(self, item):
        """
        Coroutine to create or update a single item.
        """
        logging.debug('ZeitSonde.update() called with {}'.format(item))
        try:
            validate(item, update_schema, format_checker=FormatChecker())
        except ValidationError as e:
            logging.debug('Invalid item: {}'.format(e))
            error = ' '.join(str(e).split('\n'))
            raise ApplicationError(ApplicationError.INVALID_ARGUMENT, error)
        # TODO: Save item in DB
        # TODO: Publish updated item
        return 'Item successfully created/updated.'


#  'extra_time': [
#     {'description': '...',
#      'estimated_time': '...',
#      'duration': 'timedelta',
#     }
#  ],
