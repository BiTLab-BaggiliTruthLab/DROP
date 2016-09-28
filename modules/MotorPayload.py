# Devon Clark
# Motor Class
import struct
import math

class MotorPayload:
    fields = ['rFrontSpeed', 'lFrontSpeed', 'lBackSpeed', 'rBackSpeed', 'rFrontLoad', 'lFrontLoad', 'lBackLoad', 'rBackLoad', 

    'thrustAngle'
    ]
    _type = 0xda
    _subtype = 0xf1
    _length = None
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def parse(self, payload):
        data = {}

        data['rFrontLoad'] = struct.unpack('h', payload[1:3])[0]
        data['rFrontSpeed'] = struct.unpack('h', payload[3:5])[0]
        data['lFrontLoad'] = struct.unpack('h', payload[20:22])[0]
        data['lFrontSpeed'] = struct.unpack('h', payload[22:24])[0]
        data['lBackLoad'] = struct.unpack('h', payload[39:41])[0]
        data['lBackSpeed'] = struct.unpack('h', payload[41:43])[0]
        data['rBackLoad'] = struct.unpack('h', payload[58:60])[0]
        data['rBackSpeed'] = struct.unpack('h', payload[60:62])[0]

        lbrfdiff = data['lBackSpeed'] - data['rFrontSpeed']
        rblfdiff = data['rBackSpeed'] - data['lFrontSpeed']

        thrust1 = math.degrees(math.atan2(lbrfdiff, rblfdiff))
        thrust2 = (thrust1 + 315.0) % 360
        data['thrustAngle'] = thrust2
        if thrust2 > 180.0:
            data['thrustAngle'] = thrust2 - 360.0

        return data