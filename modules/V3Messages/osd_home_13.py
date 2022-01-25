import struct

class osd_home_13:
    fields = ['osd_lon','osd_lat','osd_alt','osd_home_state','fixed_altitude','course_lock_torsion']
    message_type = 13
    label = 'osd_home'
    _length = -1       # 69 but that doesn't exist, this version hat no length in the name
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'osd_lon': struct.unpack('d', payload[0:8])[0],
            'osd_lat': struct.unpack('d', payload[8:16])[0],
            'osd_alt': struct.unpack('f', payload[16:20])[0],
            'osd_home_state': struct.unpack('H', payload[20:22])[0],
            'fixed_altitude': struct.unpack('H', payload[22:24])[0],
            'course_lock_torsion': struct.unpack('h', payload[24:26])[0],
        }
        return data