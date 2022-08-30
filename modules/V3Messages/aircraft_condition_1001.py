import struct


class aircraft_condition_1001:
    fields = ['int_fsm','fsm_state','last_fsm','near_gnd','UP_state','land_state','safe_fltr']
    message_type = 1001
    label = 'aircraft_condition'
    _length = 8
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'int_fsm': struct.unpack('B',payload[0:1])[0],
            'fsm_state': struct.unpack('B',payload[1:2])[0],
            'last_fsm': struct.unpack('B',payload[2:3])[0],
            'near_gnd': struct.unpack('B',payload[3:4])[0],
            'UP_state': struct.unpack('B',payload[4:5])[0],
            'land_state': struct.unpack('B',payload[5:6])[0],
            'safe_fltr': struct.unpack('h',payload[6:8])[0],
        }

        return data