import struct

class air_compensate_data_10100:
    fields = ['air_vbx','air_vby','comp_alti','wind_spd','wind_x','wind_y','MotorSpd','vel_level']
    message_type = 10100
    label = 'air_compensate_data'
    _length = -1    # there's more
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        if len(payload) == 29 or len(payload) == 31:
            data = {
                'air_vbx': struct.unpack('f', payload[0:4])[0],
                'air_vby': struct.unpack('f', payload[4:8])[0],
                'comp_alti': struct.unpack('f', payload[8:12])[0],
                'wind_spd': struct.unpack('f', payload[12:16])[0],
                'wind_x': struct.unpack('f', payload[16:20])[0],
                'wind_y': struct.unpack('f', payload[20:24])[0],
                'MotorSpd': struct.unpack('f', payload[24:28])[0],
                'vel_level': struct.unpack('B', payload[28:29])[0],
            }
        elif len(payload) == 23:
            data = {
                'comp_alti': struct.unpack('f', payload[0:4])[0],
                'wind_spd': struct.unpack('f', payload[4:8])[0],
                'wind_x': struct.unpack('f', payload[8:12])[0],
                'wind_y': struct.unpack('f', payload[12:16])[0],
                'MotorSpd': struct.unpack('f', payload[16:20])[0],
                'vel_level': struct.unpack('B', payload[20:21])[0],
            }
        else:
            print(self.label + " missing length definition for length of " + str(len(payload)))
            data = {}

        return data