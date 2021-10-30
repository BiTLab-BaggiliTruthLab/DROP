import struct


class RecSmartBatt_1712:
    fields = ['goHome', 'land', 'goHomeTime', 'landTime']
    message_type = 1712
    label = 'bat'
    _length = 10
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'goHome': struct.unpack('H', payload[2:4])[0],
                'land': struct.unpack('H', payload[4:6])[0],
                'goHomeTime': struct.unpack('H', payload[6:8])[0],
                'landTime': struct.unpack('H', payload[8:10])[0]
        }

        return data