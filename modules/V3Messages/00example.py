import struct

class NAME:
    fields = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    message_type = -1
    label = ''
    _length = -1
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            #: struct.unpack('h', payload[0:2])[0],
        }

        return data