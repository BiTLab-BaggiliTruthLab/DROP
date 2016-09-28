# Devon Clark
# Home Point Class
import struct
import math

class HPPayload:
    fields = ['longitudeHP', 'latitudeHP']
    _type = 0xc6
    _subtype = 0x0d
    _length = 0x2E
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def convertpos(self, pos):
        # convert position from radians to degrees
        return math.degrees(pos)

    def parse(self, payload):
        data = {}

        longitude = struct.unpack('d', payload[0:8])[0]     # parse double (float) longitude
        data['longitudeHP'] = self.convertpos(longitude)

        latitude = struct.unpack('d', payload[8:16])[0]     # parse double (float) latitude
        data['latitudeHP'] = self.convertpos(latitude)

        # only output legitimate location data
        if data['latitudeHP'] == 0 or data['longitudeHP'] == 0 or abs(data['latitudeHP']) <= 0.0175 or abs(data['longitudeHP']) <= 0.0175 or abs(data['latitudeHP']) >= 181.0 or abs(data['longitudeHP']) >= 181.0:
            data['longitudeHP'] = ''
            data['latitudeHP'] = ''
        return data