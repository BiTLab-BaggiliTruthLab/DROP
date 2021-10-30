import struct

class svo_avoid_obstacle:
    fields = ['SVO_stop_flag','SVO_p_front','SVO_p_right','SVO_p_back','SVO_p_left','SVO_v_limit','SVO_cnt']
    message_type = 100
    label = 'svo_avoid_obstacle'
    _length = -1        # 27, but had to choose a file -> use 11
    verboseOnly = True
    payload = []
    data = {}

    def __init__(self, payload):
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {
            'SVO_stop_flag': struct.unpack('B', payload[0:1])[0],
            'SVO_p_front': struct.unpack('H', payload[1:3])[0],
            'SVO_p_right': struct.unpack('H', payload[3:5])[0],
            'SVO_p_back': struct.unpack('H', payload[5:7])[0],
            'SVO_p_left': struct.unpack('H', payload[7:9])[0],
            'SVO_v_limit': struct.unpack('B', payload[9:10])[0],
            'SVO_cnt': struct.unpack('B', payload[10:11])[0],
        }

        return data