# Devon Clark
# Battery Class
import struct

class BatteryPayload:
    fields = ['batteryUsefulTime', 'voltagePercent']
    _type = 0x1e
    _subtype = 0x12
    _length = 0x59
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def parse(self, payload):
        data = {}

        data['batteryUsefulTime'] = struct.unpack('h', payload[0:2])[0]
        data['voltagePercent'] = payload[72]
        return data