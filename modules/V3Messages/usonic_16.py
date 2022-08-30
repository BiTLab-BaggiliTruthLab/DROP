import struct


class usonic_16:
    fields = ['usonic_h','usonic_flag','usonic_cnt']
    message_type = 16
    label = 'usonic'
    _length = 4
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'usonic_h': struct.unpack('h', payload[0:2])[0],
            'usonic_flag': struct.unpack('B', payload[2:3])[0],
            'usonic_cnt': struct.unpack('B', payload[3:4])[0]
        }

        return data