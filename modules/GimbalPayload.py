# Devon Clark
# Gimbal Attitude Class
# Derived from DatCon - Record44_52
import struct
import math
from modules.Quaternion import Quaternion

class GimbalPayload:
    fields = ['quatW', 'quatX', 'quatY', 'quatZ','Gimbal:roll', 'Gimbal:pitch', 'Gimbal:yaw',  'rFront', 'lFront', 'lBack', 'rBack',
    'Gimbal:Xroll', 'Gimbal:Xpitch', 'Gimbal:Xyaw']
    _type = 0x2c
    _subtype = 0x34
    _length = 0xF7
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def parse(self, payload):
        data = {}

        quatW = struct.unpack('f', payload[78:82])[0]
        quatX = struct.unpack('f', payload[82:86])[0]
        quatY = struct.unpack('f', payload[86:90])[0]
        quatZ = struct.unpack('f', payload[90:94])[0]

        qGimbal = Quaternion(quatX, quatY, quatZ, quatW)
        rpy = qGimbal.toEuler()
        data['Gimbal:Xpitch'] = math.degrees(rpy[0])
        data['Gimbal:Xroll'] = math.degrees(rpy[1])
        data['Gimbal:Xyaw'] = math.degrees(rpy[2])

        data['Gimbal:yaw'] = math.degrees(struct.unpack('f', payload[94:98])[0])
        data['Gimbal:roll'] = math.degrees(struct.unpack('f', payload[98:102])[0])
        data['Gimbal:pitch'] = math.degrees(struct.unpack('f', payload[102:106])[0])

        data['rFront'] = struct.unpack('h', payload[219:221])[0]
        data['lFront'] = struct.unpack('h', payload[221:223])[0]
        data['lBack'] = struct.unpack('h', payload[223:225])[0]
        data['rBack'] = struct.unpack('h', payload[225:227])[0]
        return data