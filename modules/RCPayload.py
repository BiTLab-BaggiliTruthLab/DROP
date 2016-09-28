# Devon Clark
# Remote Control Class
import struct

class RCPayload:
    fields = ['aileron', 'elevator', 'throttle', 'rudder', 'modeSwitch', 'gpsHealth']
    _type = 0x98
    _subtype = 0x0
    _length = 0x37
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def parse(self, payload):
        data = {}

        data['aileron'] = struct.unpack('h', payload[4:6])[0]
        data['elevator'] = struct.unpack('h', payload[6:8])[0]
        data['throttle'] = struct.unpack('h', payload[8:10])[0]
        data['rudder'] = struct.unpack('h', payload[10:12])[0]
        data['modeSwitch'] = payload[31]
        data['gpsHealth'] = payload[41]
        return data