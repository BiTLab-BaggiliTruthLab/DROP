import math
import struct


class GPS_2096:
    fields = ['latitude', 'longitude', 'altitude', 'velN', 'velE', 'velD', 'date', 'time', 'hdop', 'pdop', 'hacc', 'sacc', 'numGPS', 'numGLN', 'numSV']
    message_type = 2096
    label = 'GPS'
    _length = 72   # there's more
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        datTime = struct.unpack('I', payload[4:8])[0]
        hour = round(datTime / 10000)
        resid = datTime - hour * 10000
        min = math.floor(resid / 100)
        sec = resid - min * 100
        data = {
            'date': struct.unpack('I', payload[0:4])[0],
            'time': str(hour) + ':' + str(min) + ':' + str(sec),
            'longitude': struct.unpack('i', payload[8:12])[0]/1.0E7,
            'latitude': struct.unpack('i', payload[12:16])[0]/1.0E7,
            'altitude': struct.unpack('i', payload[16:20])[0]/1000.0,
            'velN': struct.unpack('f', payload[20:24])[0]/100.0,
            'velE': struct.unpack('f', payload[24:28])[0]/100.0,
            'velD': struct.unpack('f', payload[28:32])[0]/100.0,
            'hdop': struct.unpack('f', payload[32:36])[0]/100.0,
            'pdop': struct.unpack('f', payload[36:40])[0]/100.0,
            'hacc': struct.unpack('f', payload[40:44])[0]/100.0,
            'sacc': struct.unpack('f', payload[44:48])[0]/100.0,
            'numGPS': struct.unpack('I', payload[56:60])[0],
            'numGLN': struct.unpack('I', payload[60:64])[0],
            'numSV': struct.unpack('H', payload[64:66])[0],
        }
        # print(data)
        return data
