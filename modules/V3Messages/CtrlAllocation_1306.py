import struct


class CtrlAllocation_1306:
    fields = ['raw_tilt_x','raw_tilt_y','raw_tors','raw_lift','fix_tilt_x','fix_tilt_y','fix_tor','fix_lift','bound_max','bound_min','tors_limit_scale','tilt_scale']
    message_type = 1306
    label = 'CtrlAllocation'
    _length = 48
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'raw_tilt_x': struct.unpack('f', payload[0:4])[0],
            'raw_tilt_y': struct.unpack('f', payload[4:8])[0],
            'raw_tors': struct.unpack('f', payload[8:12])[0],
            'raw_lift': struct.unpack('f', payload[12:16])[0],
            'fix_tilt_x': struct.unpack('f', payload[16:20])[0],
            'fix_tilt_y': struct.unpack('f', payload[20:24])[0],
            'fix_tor': struct.unpack('f', payload[24:28])[0],
            'fix_lift': struct.unpack('f', payload[28:32])[0],
            'bound_max': struct.unpack('f', payload[32:36])[0],
            'bound_min': struct.unpack('f', payload[36:40])[0],
            'tors_limit_scale': struct.unpack('f', payload[40:44])[0],
            'tilt_scale': struct.unpack('f', payload[44:48])[0],
        }

        return data