# -*- coding: utf-8 -*-

# Import Python libs
from __future__ import absolute_import

# Import Salt libs
from salt.utils.schema import (EventSchema,
                               StringItem,
                               BooleanItem)


def schemas():
    return [SaltKeyEventSchema]


class SaltKeyEventSchema(EventSchema):
    tag = 'salt/key'
    title = 'Key Event'
    description = 'Event fired when a minion performs an authentication check with the master'

    id = BooleanItem(title='result',
                    description='True if the function was correct',
                    required=True)

    act = StringItem(title='act',
                    description='The current status of the minion key',
                    required=True,
                    enum=('accept', 'delete', 'reject'))

    key = StringItem(title='key',
                    description='The minion key',
                    min_length=1,
                    required=True)
