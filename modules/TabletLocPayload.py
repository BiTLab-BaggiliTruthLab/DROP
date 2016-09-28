# Devon Clark
# Tablet Location Class
import struct

class TabletLocPayload:
    fields = ['latitudeTablet', 'longitudeTablet']
    _type = 0xc1
    _subtype = 0x2b
    _length = None
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def parse(self, payload):
        data = {}

        data['longitudeTablet'] = struct.unpack('d', payload[155:163])[0]
        data['latitudeTablet'] = struct.unpack('d', payload[163:171])[0]

        # only output legitimate location data
        if data['latitudeTablet'] == 0 or data['longitudeTablet'] == 0 or abs(data['latitudeTablet']) <= 0.0175 or abs(data['longitudeTablet']) <= 0.0175 or abs(data['latitudeTablet']) >= 181.0 or abs(data['longitudeTablet']) >= 181.0:
            data['longitudeTablet'] = ''
            data['latitudeTablet'] = ''
        return data