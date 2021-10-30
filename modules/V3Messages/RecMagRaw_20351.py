import struct


class RecMagRaw_20351:
    fields = ['magX','magY','magZ']
    message_type = 20351
    label = 'RecMagRaw'
    _length = 6
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'magX': struct.unpack('h', payload[0:2])[0],
            'magY': struct.unpack('h', payload[2:4])[0],
            'magZ': struct.unpack('h', payload[4:6])[0]
        }

        return data