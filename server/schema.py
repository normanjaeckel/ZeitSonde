update_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'title': 'ZeitSonde item',
    'description': 'A representation for a file or customer where we want to '
                   'track time.',
    'type': 'object',
    'properties': {
        '_id': {
            'type': 'string',
        },
        'description': {
            'type': 'string',
        },
        'records': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'description': {
                        'type': 'string',
                        'minLength': 1,
                    },
                    'start': {
                        'type': 'string',
                        'format': 'date-time',
                    },
                    'end': {
                        'type': 'string',
                        'format': 'date-time',
                    },
                    'interruption': {
                        'description': 'Time in minutes that should not be '
                                       'billed.',
                        'type': 'integer',
                        'minimum': 1,
                    },
                },
                'required': [
                    'description',
                    'start',
                    'end',
                ],
                'additionalProperties': False,
            },
            'minItems': 1,
            'uniqueItems': True,
        },
        'extra_time': {
            # TODO
        },
    },
    'required': [
        '_id',
    ],
    'additionalProperties': False,
}
