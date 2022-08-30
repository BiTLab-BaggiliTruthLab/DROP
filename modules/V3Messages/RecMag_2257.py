import struct


class RecMag_2257:
    fields = ['magX','magY','magZ']
    message_type = 2257
    label = 'RecMag'
    _length = -1 #6,8,12
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