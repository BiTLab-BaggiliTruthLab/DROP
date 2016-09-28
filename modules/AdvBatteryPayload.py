# Devon Clark
# Advanced Battery Class
import struct
import math

class AdvBatteryPayload:
    fields = ['current', 'volt1', 'volt2', 'volt3', 'volt4', 'volt5', 'volt6', 'totalVolts', 'voltSpread', 'Watts', 'batteryTemp(C)', 'ratedCapacity', 
    'remainingCapacity', 'percentageCapacity']
    _type = 0x44
    _subtype = 0x11
    _length = 0x39
    payload = []
    data = {}

    def __init__(self, payload):
        self.payload = payload
        self.data = self.parse(self.payload)

    def parse(self, payload):
        data = {}

        data['ratedCapacity'] = struct.unpack('h', payload[2:4])[0]
        data['remainingCapacity'] = struct.unpack('h', payload[4:6])[0]
        data['totalVolts'] = float(struct.unpack('h', payload[6:8])[0]/1000.0)
        data['current'] = -(float((struct.unpack('H', payload[8:10])[0] - 65536)/1000.0))
        data['percentageCapacity'] = payload[11]
        data['batteryTemp(C)'] = payload[12]
        data['volt1'] = float(struct.unpack('h', payload[18:20])[0]/1000.0)
        data['volt2'] = float(struct.unpack('h', payload[20:22])[0]/1000.0) 
        data['volt3'] = float(struct.unpack('h', payload[22:24])[0]/1000.0) 
        data['volt4'] = float(struct.unpack('h', payload[24:26])[0]/1000.0) 
        # Only DJI Inspire has 6 cell battery, comment out for DJI Phantom 3
        #data['volt5'] = float(struct.unpack('h', payload[26:28])[0]/1000.0) 
        #data['volt6'] = float(struct.unpack('h', payload[28:30])[0]/1000.0)
        
        voltMax = max(data['volt1'], max(data['volt2'], max(data['volt3'], data['volt4'])))
        voltMin = min(data['volt1'], min(data['volt2'], min(data['volt3'], data['volt4'])))
        data['voltSpread'] = voltMax - voltMin

        data['Watts'] = data['totalVolts'] * data['current']
        
        return data