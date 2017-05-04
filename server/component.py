import logging

from autobahn.asyncio.wamp import ApplicationSession


class ZeitSonde(ApplicationSession):
    """
    ZeitSonde application.
    """
    root_uri = 'zeitsonde'

    async def onJoin(self, details):
        logging.info('ZeitSonde server has joined to WAMP router')
        await self.register(self.get_data(), '{}.get_data'.format(self.root_uri))

    def get_data(self):
        """
        TODO
        """
        logging.debug('ZeitSonde.get_data() called')
        return [{'all': 'data'}]


# {'id': '3240',
#  'description': 'foo bar baz',
#  'records': [
#     {'description': 'Work on xyz',
#      'start': 'timestamp',
#      'end': 'timestamp',
#      'interruption': 'timedelta'
#     },
#     {'description': 'Work on something else',
#      'start': 'timestamp',
#      'end': 'timestamp',
#      'interruption': 'timedelta'
#     },
#  ],
#  'extra_time': [
#     {'description': '...',
#      'estimated_time': '...',
#      'duration': 'timedelta',
#     }
#  ],
# }
