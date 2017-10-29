# -*- coding: utf-8 -*-

# Import Python libs
from __future__ import absolute_import

# Import Salt libs
from salt.utils.schema import (EventSchema,
                               StringItem,
                               BooleanItem)


def schemas():
    return []
    # return [SaltLoaderEventSchema]


class SaltLoaderEventSchema(EventSchema):
    tag = 'salt/minion/minion_mod_complete'
    title = 'Modules loaded Event'
    description = 'Event fired when a minion has completed loading modules'

    complete = BooleanItem(title='complete',
                    description='True after modules are loaded',
                    required=True)
