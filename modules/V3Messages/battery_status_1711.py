import struct


class battery_status_1711:
    fields = ['not_ready','comm_err','first_auth','auth_fail','need_re','volVerylow','volNotsafe','volLevel1','vollevel2','capLevel1','capLevel2','smartCap1',
              'smartCap2','d_flg','ccsc','all']
    message_type = 1711
    label = 'battery_status'
    _length = 19    #there's more
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'not_ready': struct.unpack('B',payload[0:1])[0],
            'comm_err': struct.unpack('B',payload[1:2])[0],
            'first_auth': struct.unpack('B',payload[2:3])[0],
            'auth_fail': struct.unpack('B',payload[3:4])[0],
            'need_re': struct.unpack('B',payload[4:5])[0],
            'volVerylow': struct.unpack('B',payload[5:6])[0],
            'volNotsafe': struct.unpack('B',payload[6:7])[0],
            'volLevel1': struct.unpack('B',payload[7:8])[0],
            'vollevel2': struct.unpack('B',payload[8:9])[0],
            'capLevel1': struct.unpack('B',payload[9:10])[0],
            'capLevel2': struct.unpack('B',payload[10:11])[0],
            'smartCap1': struct.unpack('B',payload[11:12])[0],
            'smartCap2': struct.unpack('B',payload[12:13])[0],
            'd_flg': struct.unpack('B',payload[13:14])[0],
            'ccsc': struct.unpack('B',payload[14:15])[0],
            'all': struct.unpack('I',payload[15:19])[0]
        }

        return data