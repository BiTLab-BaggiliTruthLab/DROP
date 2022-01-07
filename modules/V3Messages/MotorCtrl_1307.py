import struct


class MotorCtrl_1307:
    fields = ['pwm1','pwm2','pwm3','pwm4','pwm5','pwm6','pwm7','pwm8']
    message_type = 1307
    label = 'MotorCtrl'
    _length = 16    # there's more
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'pwm1': struct.unpack('H', payload[0:2])[0],
            'pwm2': struct.unpack('H', payload[2:4])[0],
            'pwm3': struct.unpack('H', payload[4:6])[0],
            'pwm4': struct.unpack('H', payload[6:8])[0],
            'pwm5': struct.unpack('H', payload[8:10])[0],
            'pwm6': struct.unpack('H', payload[10:12])[0],
            'pwm7': struct.unpack('H', payload[12:14])[0],
            'pwm8': struct.unpack('H', payload[14:16])[0]
        }

        return data