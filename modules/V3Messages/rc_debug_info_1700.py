import struct


class rc_debug_info_1700:
    fields = ['cur_cmd','fail_safe','vedio_lost','data_lost','app_lost','frame_lost','rec_cnt','sky_con','gnd_con','connected','m_changed','arm_status','wifi_en','in_wifi']
    message_type = 1700
    label = 'rc_debug_info'
    _length = 18    #there's more
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'cur_cmd': struct.unpack('H', payload[0:2])[0],
                'fail_safe': struct.unpack('B', payload[2:3])[0],
                'vedio_lost': struct.unpack('B', payload[3:4])[0],
                'data_lost': struct.unpack('B', payload[4:5])[0],
                'app_lost': struct.unpack('B', payload[5:6])[0],
                'frame_lost': struct.unpack('B', payload[6:7])[0],
                'rec_cnt': struct.unpack('I', payload[7:11])[0],
                'sky_con': struct.unpack('B', payload[11:12])[0],
                'gnd_con': struct.unpack('B', payload[12:13])[0],
                'connected': struct.unpack('B', payload[13:14])[0],
                'm_changed': struct.unpack('B', payload[14:15])[0],
                'arm_status': struct.unpack('B', payload[15:16])[0],
                'wifi_en': struct.unpack('B', payload[16:17])[0],
                'in_wifi': struct.unpack('B', payload[17:18])[0],
                }

        return data