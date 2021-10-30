import struct


class MVO_29:
    fields = ['visionObservationCount','Vel_X','Vel_Y','Vel_Z','Pos_X','Pos_Y','Pos_Z','hoverPointUncertainty1',
              'hoverPointUncertainty2','hoverPointUncertainty3','hoverPointUncertainty4','hoverPointUncertainty5',
              'hoverPointUncertainty6','velocityUncertainty1','velocityUncertainty2','velocityUncertainty3',
              'velocityUncertainty4','velocityUncertainty5','velocityUncertainty6','height','heightUncertainty','flags']
    message_type = 29
    label = 'MVO'
    _length = 80
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'visionObservationCount': struct.unpack('H',payload[0:2])[0],
            'Vel_X': struct.unpack('h',payload[2:4])[0],
            'Vel_Y': struct.unpack('h',payload[4:6])[0],
            'Vel_Z': struct.unpack('h',payload[6:8])[0],
            'Pos_X': struct.unpack('f',payload[8:12])[0],
            'Pos_Y': struct.unpack('f',payload[12:16])[0],
            'Pos_Z': struct.unpack('f',payload[16:20])[0],
            'hoverPointUncertainty1': struct.unpack('f',payload[20:24])[0],
            'hoverPointUncertainty2': struct.unpack('f',payload[24:28])[0],
            'hoverPointUncertainty3': struct.unpack('f',payload[28:32])[0],
            'hoverPointUncertainty4': struct.unpack('f',payload[32:36])[0],
            'hoverPointUncertainty5': struct.unpack('f',payload[36:40])[0],
            'hoverPointUncertainty6': struct.unpack('f',payload[40:44])[0],
            'velocityUncertainty1': struct.unpack('f',payload[44:48])[0],
            'velocityUncertainty2': struct.unpack('f',payload[48:52])[0],
            'velocityUncertainty3': struct.unpack('f',payload[52:56])[0],
            'velocityUncertainty4': struct.unpack('f',payload[56:60])[0],
            'velocityUncertainty5': struct.unpack('f',payload[60:64])[0],
            'velocityUncertainty6': struct.unpack('f',payload[64:68])[0],
            'height': struct.unpack('f',payload[68:72])[0],
            'heightUncertainty': struct.unpack('f',payload[72:76])[0],
            'flags': struct.unpack('B',payload[76:77])[0]
        }

        return data