import struct


class CtrlVelVert_1202:
    fields = ['vel_cmd','vel_before','vel_after','vel_fdbk','vel_tag']
    message_type = 1202
    label = 'CtrlVelVert'
    _length = 9
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'vel_cmd': struct.unpack('h', payload[0:2])[0],
            'vel_before': struct.unpack('h', payload[2:4])[0],
            'vel_after': struct.unpack('h', payload[4:6])[0],
            'vel_fdbk': struct.unpack('h', payload[6:8])[0],
            'vel_tag': struct.unpack('B', payload[8:9])[0],
        }

        return data