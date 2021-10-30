import struct


class GPS_GLNS_5:
    fields = ['gps_date', 'gps_time', 'gps_lon', 'gps_lat']
    message_type = 5
    label = 'GPS'
    _length = 68
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'gps_date': struct.unpack('I', payload[0:4])[0],
                'gps_time': struct.unpack('I', payload[4:8])[0],
                'gps_lon': struct.unpack('i', payload[8:12])[0],
                'gps_lat': struct.unpack('i', payload[12:16])[0]
                }
        return data