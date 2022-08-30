import struct


class svo_debug_101:
    fields = ['VisionDebug1','VisionDebug2','VisionDebug3','VisionDebug4','VisionDebug5','VisionDebug6','VisionDebug7','VisionDebug8']
    message_type = 101
    label = 'svo_debug'
    _length = 32
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'VisionDebug1': struct.unpack('f',payload[0:4])[0],
            'VisionDebug2': struct.unpack('f',payload[4:8])[0],
            'VisionDebug3': struct.unpack('f',payload[8:12])[0],
            'VisionDebug4': struct.unpack('f',payload[12:16])[0],
            'VisionDebug5': struct.unpack('f',payload[16:20])[0],
            'VisionDebug6': struct.unpack('f',payload[20:24])[0],
            'VisionDebug7': struct.unpack('f',payload[24:28])[0],
            'VisionDebug8': struct.unpack('f',payload[28:32])[0],
        }

        return data